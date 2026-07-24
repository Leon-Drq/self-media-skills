/**
 * 微信发布模块
 * 调用微信公众号 API 发布草稿
 */

const axios = require('axios');
const fs = require('fs');
const path = require('path');

// 读取配置
function loadConfig() {
  const configPath = path.join(process.cwd(), 'config', 'config.json');
  if (!fs.existsSync(configPath)) {
    throw new Error('配置文件不存在，请复制 config.example.json 为 config.json 并填写');
  }
  return JSON.parse(fs.readFileSync(configPath, 'utf-8'));
}

/**
 * 获取微信 access_token
 */
async function getAccessToken() {
  const config = loadConfig();
  const { appId, appSecret } = config.wechat;

  const url = `https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=${appId}&secret=${appSecret}`;

  const response = await axios.get(url);
  if (response.data.errcode) {
    throw new Error(`获取 token 失败: ${response.data.errmsg}`);
  }

  return response.data.access_token;
}

/**
 * 上传封面图片
 */
async function uploadCover(accessToken, imagePath) {
  // 如果没有提供封面，使用默认封面或生成纯色封面
  // 这里简化处理，实际应该上传图片
  const url = `https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=${accessToken}&type=thumb`;

  // 返回一个默认的 media_id
  // 实际使用时需要上传真实图片
  return 'default_thumb_media_id';
}

/**
 * 发布草稿
 */
async function publish(html, title, author) {
  try {
    const accessToken = await getAccessToken();

    // 上传封面（简化版）
    const thumbMediaId = await uploadCover(accessToken);

    // 创建草稿
    const url = `https://api.weixin.qq.com/cgi-bin/draft/add?access_token=${accessToken}`;

    const data = {
      articles: [{
        title: title || '未命名文章',
        author: author || 'AI Pioneer',
        thumb_media_id: thumbMediaId,
        content: html,
        digest: html.replace(/<[^>]+>/g, '').substring(0, 100) + '...',
        need_open_comment: 1,
        only_fans_can_comment: 0
      }]
    };

    const response = await axios.post(url, data);

    if (response.data.errcode) {
      throw new Error(`发布失败: ${response.data.errmsg}`);
    }

    return {
      mediaId: response.data.media_id,
      url: `https://mp.weixin.qq.com`
    };

  } catch (error) {
    throw new Error(`发布到微信失败: ${error.message}`);
  }
}

module.exports = {
  publish
};