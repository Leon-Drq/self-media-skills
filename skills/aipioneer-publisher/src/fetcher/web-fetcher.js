/**
 * 网页内容获取器
 * 使用 axios + cheerio 抓取网页
 */

const axios = require('axios');
const cheerio = require('cheerio');

class WebFetcher {
  async fetch(url) {
    try {
      const response = await axios.get(url, {
        timeout: 30000,
        headers: {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
      });

      const $ = cheerio.load(response.data);

      // 移除脚本和样式
      $('script, style, nav, footer, header').remove();

      // 提取标题
      const title = $('h1').first().text() ||
                    $('title').text() ||
                    $('meta[property="og:title"]').attr('content') ||
                    '';

      // 提取正文
      let text = '';

      // 尝试常见正文容器
      const selectors = [
        'article',
        '[role="main"]',
        '.post-content',
        '.entry-content',
        '.content',
        'main',
        '.article-body'
      ];

      for (const selector of selectors) {
        const el = $(selector);
        if (el.length && el.text().length > 500) {
          text = el.text();
          break;
        }
      }

      // 如果没找到，取 body 文本
      if (!text) {
        text = $('body').text();
      }

      // 清理文本
      text = text
        .replace(/\s+/g, ' ')
        .replace(/\n+/g, '\n')
        .trim();

      return {
        title: title.trim(),
        text,
        source: 'web',
        url
      };

    } catch (error) {
      throw new Error(`获取网页内容失败: ${error.message}`);
    }
  }
}

module.exports = new WebFetcher();