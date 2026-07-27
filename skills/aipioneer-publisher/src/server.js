/**
 * API 服务
 * 提供 HTTP API 接口
 */

const express = require('express');
const fetcher = require('./fetcher');
const writer = require('./writer');
const formatter = require('./formatter');
const publisher = require('./publisher');

function createServer(port = 3000) {
  const app = express();

  app.use(express.json());

  // 健康检查
  app.get('/health', (req, res) => {
    res.json({ status: 'ok', version: require('../package.json').version });
  });

  // 获取内容
  app.post('/api/fetch', async (req, res) => {
    try {
      const { url } = req.body;
      const content = await fetcher.fetch(url);
      res.json({ success: true, data: content });
    } catch (error) {
      res.status(500).json({ success: false, error: error.message });
    }
  });

  // 改写内容
  app.post('/api/rewrite', async (req, res) => {
    try {
      const { content, style = 'khazix' } = req.body;
      const article = await writer.rewrite(content, style);
      res.json({ success: true, data: article });
    } catch (error) {
      res.status(500).json({ success: false, error: error.message });
    }
  });

  // 排版
  app.post('/api/format', (req, res) => {
    try {
      const { article, style = 'ai-pioneer-black' } = req.body;
      const html = formatter.format(article, style);
      res.json({ success: true, data: { html } });
    } catch (error) {
      res.status(500).json({ success: false, error: error.message });
    }
  });

  // 发布
  app.post('/api/publish', async (req, res) => {
    try {
      const { html, title, author } = req.body;
      const result = await publisher.publish(html, title, author);
      res.json({ success: true, data: result });
    } catch (error) {
      res.status(500).json({ success: false, error: error.message });
    }
  });

  // 一键发布
  app.post('/api/publish-one-click', async (req, res) => {
    try {
      const { url, style = 'ai-pioneer-black', writer = 'khazix', author = 'AI Pioneer' } = req.body;

      // 1. 获取
      const content = await fetcher.fetch(url);

      // 2. 改写
      const article = await writer.rewrite(content, writer);

      // 3. 排版
      const html = formatter.format(article, style);

      // 4. 发布
      const result = await publisher.publish(html, article.title, author);

      res.json({
        success: true,
        data: {
          title: article.title,
          mediaId: result.mediaId,
          url: result.url
        }
      });
    } catch (error) {
      res.status(500).json({ success: false, error: error.message });
    }
  });

  app.listen(port, () => {
    console.log(`🚀 AIPioneer API 服务启动成功`);
    console.log(`📡 http://localhost:${port}`);
    console.log(`📖 API 文档: http://localhost:${port}/health`);
  });

  return app;
}

module.exports = createServer;