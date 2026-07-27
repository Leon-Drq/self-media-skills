---
name: aipioneer-publisher
description: |
  AIPioneer 公众号发布器 - 一键完成：素材获取 → 卡兹克风格改写 → AI Pioneer 纯黑样式排版 → 微信草稿箱发布。
  支持 X/Twitter、网页文章、PDF 等多种素材来源。
---

# AIPioneer 公众号发布器

全自动文章发布工作流，一键完成从素材到微信草稿的完整流程。

## 触发场景

- 帮我发布这篇文章
- 用 AI Pioneer 排版发布
- 卡兹克风格发布
- 一键发布到公众号
- 发公众号

## 依赖

- `wechat-typesetting`
- `openclaw-gateway`

## 工作流程

```
素材链接 → 内容获取 → 卡兹克改写 → AI Pioneer 排版 → 微信草稿箱
```

## 使用方式

### 命令行

```bash
# 发布 X/Twitter 文章
npx aipioneer-publisher publish "https://x.com/用户名/status/推文ID"

# 发布网页文章
npx aipioneer-publisher publish "https://example.com/article"

# 指定风格
npx aipioneer-publisher publish "链接" --style khazix
```

### OpenClaw Skill

```
@666Claw 帮我发布这篇文章：https://x.com/用户名/status/推文ID
```

## 核心模块

### 1. 内容获取 (Fetcher)

- **x-article-fetcher**: X/Twitter 文章获取
- **web-fetcher**: 网页内容抓取
- **pdf-fetcher**: PDF 文档解析

### 2. 写作风格 (Writer)

- **khazix-writer**: 卡兹克活人感写作风格
  - 口语化表达
  - 真实场景切入
  - 长短句交替
  - 文化升维

### 3. 排版样式 (Formatter)

**AI Pioneer 纯黑样式**:
- 标签: `#000000` 背景 + `#ffffff` 文字
- 章节标题: 80px 浅黑数字 + 24px 纯黑标题
- 强调文字: `#000000`
- 引用块: `rgba(0,0,0,0.06)` 背景

### 4. 发布功能 (Publisher)

- 微信素材上传
- 草稿创建
- 封面生成

## 配置

### 必需

```json
{
  "wechat": {
    "appId": "wx...",
    "appSecret": "..."
  }
}
```

### 可选

- 自定义样式
- 自定义写作风格
- 自动发布设置

## 依赖

- Node.js >= 16
- wechat-typesetting 服务
- OpenClaw gateway (可选，用于 X/Twitter 获取)

## 示例

**输入**:
```
@666Claw 帮我发布这篇文章：https://x.com/garrytan/status/2044479509874020852
```

**输出**:
```
✅ 文章发布成功！

📄 标题: Resolver：AI Agent 系统的路由表
🎨 样式: AI Pioneer 纯黑
✍️ 风格: 卡兹克 (Khazix)
📤 Media ID: 48zUvSeqdqRiaCswIqCxX...

🔗 请在微信公众平台查看草稿
```
