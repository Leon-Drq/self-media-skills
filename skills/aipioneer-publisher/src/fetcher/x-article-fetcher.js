/**
 * X/Twitter 文章获取器
 * 使用 Puppeteer 模拟浏览器访问
 */

const puppeteer = require('puppeteer');

class XArticleFetcher {
  constructor() {
    this.browser = null;
  }

  async init() {
    if (!this.browser) {
      this.browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox']
      });
    }
  }

  async fetch(url) {
    await this.init();

    const page = await this.browser.newPage();

    try {
      // 设置 UA
      await page.setUserAgent(
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
      );

      // 访问页面
      await page.goto(url, { waitUntil: 'networkidle2', timeout: 30000 });

      // 等待内容加载
      await page.waitForTimeout(5000);

      // 提取内容
      const content = await page.evaluate(() => {
        // 获取推文作者
        const authorEl = document.querySelector('[data-testid="User-Name"]');
        const author = authorEl ? authorEl.textContent : '';

        // 获取推文内容
        const tweetEl = document.querySelector('[data-testid="tweetText"]');
        const text = tweetEl ? tweetEl.innerText : '';

        // 获取文章标题（长文章）
        const titleEl = document.querySelector('h2[role="heading"]');
        const title = titleEl ? titleEl.textContent : '';

        // 获取互动数据
        const stats = {
          likes: document.querySelector('[data-testid="like"]')?.textContent || '0',
          retweets: document.querySelector('[data-testid="retweet"]')?.textContent || '0',
          replies: document.querySelector('[data-testid="reply"]')?.textContent || '0'
        };

        return {
          author,
          title,
          text,
          stats,
          source: 'x',
          url: window.location.href
        };
      });

      return content;

    } catch (error) {
      throw new Error(`获取 X 内容失败: ${error.message}`);
    } finally {
      await page.close();
    }
  }

  async close() {
    if (this.browser) {
      await this.browser.close();
      this.browser = null;
    }
  }
}

// 导出单例
const fetcher = new XArticleFetcher();

module.exports = {
  fetch: (url) => fetcher.fetch(url)
};