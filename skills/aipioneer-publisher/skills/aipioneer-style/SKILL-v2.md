---
name: aipioneer-style-v2
description: |
  AI Pioneer 公众号排版样式 v2.0 - 深海宝蓝配色版
  品牌头图 + 深海宝蓝(#0E61AC)主色 + 奶润米杏(#FAF2E0)引用背景
---

# AI Pioneer 样式 v2.0（深海宝蓝版）

## 版本信息

- **版本**: v2.0.0
- **名称**: AI Pioneer 深海宝蓝
- **配色**: 深海宝蓝 + 奶润米杏
- **基于**: v1.0 结构 + 品牌头图

## 配色方案

| 用途 | 色值 | 说明 |
|------|------|------|
| 主色 | `#0E61AC` | 深海宝蓝，强调文字、标题 |
| 引用背景 | `#FAF2E0` | 奶润米杏，引用块背景 |
| 章节数字 | `#E8F4FC` | 浅蓝灰，装饰性数字 |
| 正文 | `#333333` | 深灰，正文内容 |
| 次要 | `#666666` | 中灰，caption、辅助 |

## 与 v1 的区别

```
v1: [标签] → [正文 - 纯黑强调] → [浅灰背景引用]
v2: [品牌头图] → [正文 - 宝蓝强调] → [奶润米杏背景引用]
```

## 核心样式

### 品牌头图
```html
<p style="margin:0;text-align:center;">
  <img src="header.png" style="max-width:100%;height:auto;display:block;" alt="AI PIONEER">
</p>
```

### 强调文字
```html
<b style="color:#0E61AC;">强调内容</b>
```

### 引用块（奶润米杏背景）
```html
<p style="font-size:16px;color:#0E61AC;font-weight:700;line-height:2.0;margin:0 0 16px;padding:12px 16px;background:#FAF2E0;border-radius:8px;">
  引用内容
</p>
```

### 章节标题
```html
<p style="margin:0 0 8px;">
  <span style="display:block;font-size:80px;font-weight:700;color:#E8F4FC;line-height:1;letter-spacing:-2px;">01</span>
  <span style="display:block;font-size:24px;font-weight:700;color:#0E61AC;line-height:1.3;margin-top:-48px;">章节标题</span>
</p>
```

### 图片
```html
<p style="text-align:center;margin:20px 0;">
  <img src="image.jpg" style="max-width:100%;border-radius:8px;" alt="描述">
</p>
<p style="font-size:14px;color:#666;text-align:center;margin:0 0 20px;">图片说明</p>
```

### 结尾
```html
<p style="border-top:1px solid rgba(0,0,0,0.1);margin:0;"><br></p>
<p style="margin:0;padding:24px 0;text-align:center;">
  <b style="font-size:16px;color:#333;display:block;margin-bottom:10px;">觉得有用？</b>
  <span style="font-size:14px;color:#666;line-height:1.8;display:block;margin-bottom:16px;">点个<span style="color:#0E61AC;">❤️</span><b style="color:#0E61AC;">在看</b>，转给还不知道的朋友</span>
  <span style="font-size:14px;color:#666;line-height:2;display:block;">关注「AI Pioneer」，下次更新第一时间收到</span>
</p>
```

## 完整结构

```html
<!-- 1. 品牌头图 -->
<p style="margin:0;text-align:center;">
  <img src="header.png" style="max-width:100%;height:auto;display:block;" alt="AI PIONEER">
</p>

<!-- 2. 正文（深海宝蓝强调） -->
<p style="font-size:16px;color:#333;line-height:2.0;margin:0 0 16px;">
  正文内容<b style="color:#0E61AC;">强调</b>
</p>

<!-- 3. 引用块（奶润米杏背景） -->
<p style="font-size:16px;color:#0E61AC;font-weight:700;line-height:2.0;margin:0 0 16px;padding:12px 16px;background:#FAF2E0;border-radius:8px;">
  引用内容
</p>

<!-- 4. 章节标题 -->
<p style="margin:0 0 8px;">
  <span style="display:block;font-size:80px;font-weight:700;color:#E8F4FC;line-height:1;letter-spacing:-2px;">01</span>
  <span style="display:block;font-size:24px;font-weight:700;color:#0E61AC;line-height:1.3;margin-top:-48px;">章节标题</span>
</p>

<!-- 5. 图片 -->
<p style="text-align:center;margin:20px 0;">
  <img src="image.jpg" style="max-width:100%;border-radius:8px;" alt="描述">
</p>

<!-- 6. 结尾 -->
...
```

## 版本对比

| 版本 | 主色 | 引用背景 | 特点 |
|------|------|----------|------|
| v1.0 | `#000000` 纯黑 | `rgba(0,0,0,0.06)` 浅灰 | 极简现代 |
| v2.0 | `#0E61AC` 深海宝蓝 | `#FAF2E0` 奶润米杏 | 温暖专业 |

## 使用方式

```bash
# 使用 v1.0
npx aipioneer-publisher publish "链接" --theme ai-pioneer-v1

# 使用 v2.0
npx aipioneer-publisher publish "链接" --theme ai-pioneer-v2
```
