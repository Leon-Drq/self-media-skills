#!/usr/bin/env node

/**
 * AIPioneer 公众号发布器
 * 主入口文件
 */

const { program } = require('commander');
const packageJson = require('../package.json');
const fetcher = require('./fetcher');
const writer = require('./writer');
const formatter = require('./formatter');
const publisher = require('./publisher');

program
  .name('aipioneer-publisher')
  .description('AIPioneer 公众号发布器 - 一键完成素材获取、改写、排版、发布')
  .version(packageJson.version);

// 发布命令
program
  .command('publish <url>')
  .description('发布文章到微信公众号')
  .option('-s, --style <style>', '排版样式', 'ai-pioneer-black')
  .option('-w, --writer <writer>', '写作风格', 'khazix')
  .option('-a, --author <author>', '文章作者', 'AI Pioneer')
  .action(async (url, options) => {
    try {
      console.log('🚀 AIPioneer 公众号发布器');
      console.log('======================');

      // 1. 获取内容
      console.log('\n📡 步骤 1/4: 获取内容...');
      const content = await fetcher.fetch(url);
      console.log('✅ 内容获取成功');

      // 2. 改写内容
      console.log('\n✍️  步骤 2/4: 改写内容...');
      const article = await writer.rewrite(content, options.writer);
      console.log('✅ 改写完成');

      // 3. 排版
      console.log('\n🎨 步骤 3/4: 排版...');
      const html = formatter.format(article, options.style);
      console.log('✅ 排版完成');

      // 4. 发布
      console.log('\n📤 步骤 4/4: 发布到微信...');
      const result = await publisher.publish(html, article.title, options.author);

      console.log('\n✅ 发布成功！');
      console.log('======================');
      console.log(`📄 标题: ${article.title}`);
      console.log(`🎨 样式: ${options.style}`);
      console.log(`✍️  风格: ${options.writer}`);
      console.log(`🆔 Media ID: ${result.mediaId}`);
      console.log('\n🔗 请在微信公众平台查看草稿');

    } catch (error) {
      console.error('\n❌ 错误:', error.message);
      process.exit(1);
    }
  });

// 仅获取内容
program
  .command('fetch <url>')
  .description('仅获取内容，不发布')
  .action(async (url) => {
    try {
      const content = await fetcher.fetch(url);
      console.log(JSON.stringify(content, null, 2));
    } catch (error) {
      console.error('❌ 错误:', error.message);
      process.exit(1);
    }
  });

// 仅改写
program
  .command('rewrite <file>')
  .description('改写本地文件')
  .option('-w, --writer <writer>', '写作风格', 'khazix')
  .action(async (file, options) => {
    try {
      const fs = require('fs');
      const content = fs.readFileSync(file, 'utf-8');
      const article = await writer.rewrite({ text: content }, options.writer);
      console.log(JSON.stringify(article, null, 2));
    } catch (error) {
      console.error('❌ 错误:', error.message);
      process.exit(1);
    }
  });

// 启动服务
program
  .command('serve')
  .description('启动 API 服务')
  .option('-p, --port <port>', '端口号', '3000')
  .action((options) => {
    require('./server')(parseInt(options.port));
  });

program.parse();