---
name: aipioneer-style
description: |
  AI Pioneer 公众号排版样式 v1.0 - 纯黑极简风格
  特点：80px 大号章节数字、纯黑强调、圆角图片、清晰层次
---

# AI Pioneer 样式 v1.0

## 版本信息

- **版本**: v1.0
- **名称**: AI Pioneer 纯黑样式
- **状态**: 当前默认样式
- **创建时间**: 2026-04-17

## 设计原则

1. **极简** - 纯黑主色，无多余装饰
2. **层次** - 大号章节数字创造视觉节奏
3. **专注** - 内容优先，排版服务于阅读
4. **统一** - 所有元素遵循同一套设计系统

## 视觉规范

### 颜色系统

| 用途 | 色值 | 说明 |
|------|------|------|
| 主色 | `#000000` | 标签、强调、标题 |
| 正文 | `#333333` | 段落文字 |
| 次要 | `#666666` | caption、辅助信息 |
| 背景强调 | `rgba(0,0,0,0.06)` | 引用块、高亮 |
| 章节数字 | `rgba(0,0,0,0.08)` | 装饰性大数字 |

### 字体规范

| 元素 | 字号 | 字重 | 颜色 |
|------|------|------|------|
| 标签 | 11px | normal | #fff (白底黑字) |
| 正文 | 16px | normal | #333 |
| 强调 | 16px | 700 (bold) | #000 |
| 章节数字 | 80px | 700 | rgba(0,0,0,0.08) |
| 章节标题 | 24px | 700 | #000 |
| caption | 14px | normal | #666 |

### 间距系统

- 段落间距: `margin: 0 0 16px`
- 图片间距: `margin: 20px 0`
- 章节间距: `margin: 0 0 8px` (数字区域)
- 容器内边距: `padding: 10px 16px` (引用块)

## 组件规范

### 1. 标签 (Tag)

```html
<p style="margin:0 0 10px;">
  <span style="display:inline-block;background:#000000;color:#ffffff;font-size:11px;padding:3px 12px;border-radius:20px;letter-spacing:1.5px;">
    AI Pioneer · 深度观点
  </span>
</p>
```

### 2. 章节标题 (Section Header)

```html
<p style="margin:0 0 8px;">
  <span style="display:block;font-size:80px;font-weight:700;color:rgba(0,0,0,0.08);line-height:1;letter-spacing:-2px;">01</span>
  <span style="display:block;font-size:24px;font-weight:700;color:#000000;line-height:1.3;margin-top:-48px;">章节标题</span>
</p>
```

### 3. 引用块 (Quote Block)

```html
<p style="font-size:16px;color:#000000;font-weight:700;line-height:2.0;margin:0 0 16px;padding:10px 16px;background:rgba(0,0,0,0.06);border-radius:8px;">
  引用内容
</p>
```

### 4. 图片 + Caption

```html
<p style="text-align:center;margin:20px 0;">
  <img src="图片URL" style="max-width:100%;border-radius:8px;" alt="描述">
</p>
<p style="font-size:14px;color:#666;text-align:center;margin:0 0 20px;">图片说明</p>
```

### 5. 结尾引导 (CTA)

```html
<p style="border-top:1px solid rgba(0,0,0,0.1);margin:0;"><br></p>
<p style="margin:0;padding:24px 0;text-align:center;">
  <b style="font-size:16px;color:#333;display:block;margin-bottom:10px;">觉得有用？</b>
  <span style="font-size:14px;color:#666;line-height:1.8;display:block;margin-bottom:16px;">
    点个<span style="color:#000000;">❤️</span><b style="color:#000000;">在看</b>，转给还不知道的朋友
  </span>
  <span style="font-size:14px;color:#666;line-height:2;display:block;">
    关注「AI Pioneer」，下次更新第一时间收到
  </span>
</p>
```

## 完整示例

```html
<!-- 标签 -->
<p style="margin:0 0 10px;">
  <span style="display:inline-block;background:#000000;color:#ffffff;font-size:11px;padding:3px 12px;border-radius:20px;letter-spacing:1.5px;">AI Pioneer · 产品发布</span>
</p>

<!-- 钩子段落 -->
<p style="font-size:16px;color:#333;line-height:2.0;margin:0 0 16px;">你的最难的编程任务，现在可以交给 AI 了。</p>

<!-- 章节标题 -->
<p style="margin:0 0 8px;">
  <span style="display:block;font-size:80px;font-weight:700;color:rgba(0,0,0,0.08);line-height:1;letter-spacing:-2px;">01</span>
  <span style="display:block;font-size:24px;font-weight:700;color:#000000;line-height:1.3;margin-top:-48px;">核心观点</span>
</p>

<!-- 正文 + 强调 -->
<p style="font-size:16px;color:#333;line-height:2.0;margin:0 0 16px;">
  这是普通文本，<b style="color:#000000;">这是重点强调</b>。
</p>

<!-- 引用块 -->
<p style="font-size:16px;color:#000000;font-weight:700;line-height:2.0;margin:0 0 16px;padding:10px 16px;background:rgba(0,0,0,0.06);border-radius:8px;">
  这是引用或重点内容
</p>

<!-- 图片 -->
<p style="text-align:center;margin:20px 0;">
  <img src="图片URL" style="max-width:100%;border-radius:8px;" alt="描述">
</p>
<p style="font-size:14px;color:#666;text-align:center;margin:0 0 20px;">图片说明</p>
```

## 使用方式

### 命令行

```bash
npx aipioneer-publisher publish "链接" --theme ai-pioneer-black
```

### OpenClaw

```
@666Claw 发布这篇文章：https://example.com/article
```

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-04-17 | 初始版本，纯黑极简风格 |

## 弃用样式

- ~~ai-pioneer-blue~~ (Frakta 蓝 #0051A8) - 已弃用
- ~~ai-fan~~ (橙红主色) - 已弃用
