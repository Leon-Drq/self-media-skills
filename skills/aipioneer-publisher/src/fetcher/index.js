/**
 * 内容获取模块
 * 支持 X/Twitter、网页文章、PDF
 */

const xFetcher = require('./x-article-fetcher');
const webFetcher = require('./web-fetcher');

/**
 * 根据 URL 自动选择获取方式
 */
async function fetch(url) {
  // X/Twitter
  if (url.includes('x.com') || url.includes('twitter.com')) {
    return await xFetcher.fetch(url);
  }

  // 网页
  return await webFetcher.fetch(url);
}

module.exports = {
  fetch
};