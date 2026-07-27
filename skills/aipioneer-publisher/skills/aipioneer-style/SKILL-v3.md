---
name: aipioneer-style-v3
description: |
  AI Pioneer 公众号排版样式 v3.0 - 章节数字优化版
  基于 v1.0，章节数字放到标题上方，避免遮挡
---

# AI Pioneer 样式 v3.0（章节数字优化版）

## 版本信息

- **版本**: v3.0.0
- **名称**: AI Pioneer 章节数字优化
- **基于**: v1.0 纯黑样式
- **改进**: 章节数字位置优化

## 与 v1 的区别

```
v1: [80px 数字 -48px 偏移] → [标题被遮挡]
v3: [80px 数字] → [标题在下方] 无遮挡
```

## 章节标题样式（v3 改进）

### v1 旧版（有遮挡）
```html
<p style="margin:0 0 8px;">
  <span style="display:block;font-size:80px;font-weight:700;color:rgba(0,0,0,0.08);line-height:1;letter-spacing:-2px;">01</span>
  <span style="display:block;font-size:24px;font-weight:700;color:#000000;line-height:1.3;margin-top:-48px;">章节标题</span>
</p>
```

### v3 新版（无遮挡）
```html
<!-- 章节数字 -->
<p style="margin:0;font-size:80px;font-weight:700;color:rgba(0,0,0,0.08);line-height:1;letter-spacing:-2px;">01</p>
<!-- 章节标题 -->
<p style="margin:8px 0 16px;font-size:24px;font-weight:700;color:#000000;line-height:1.3;">章节标题</p>
```

## 完整结构

```html
<!-- 标签 -->
<p style="margin:0 0 10px;">
  <span style="display:inline-block;background:#000000;color:#ffffff;font-size:11px;padding:3px 12px;border-radius:20px;letter-spacing:1.5px;">AI Pioneer · 深度观点</span>
</p>

<!-- 正文 -->
<p style="font-size:16px;color:#333;line-height:2.0;margin:0 0 16px;">
  正文内容<b style="color:#000000;">强调</b>
</p>

<!-- 章节数字（独立一行） -->
<p style="margin:0;font-size:80px;font-weight:700;color:rgba(0,0,0,0.08);line-height:1;letter-spacing:-2px;">01</p>
<!-- 章节标题（独立一行，无负 margin） -->
<p style="margin:8px 0 16px;font-size:24px;font-weight:700;color:#000000;line-height:1.3;">章节标题</p>

<!-- 正文继续 -->
...
```

## 版本对比

| 版本 | 章节数字位置 | 标题遮挡 | 适用场景 |
|------|-------------|----------|----------|
| v1.0 | 与标题重叠（-48px） | 有 | 紧凑布局 |
| v3.0 | 标题上方（独立） | 无 | 清晰阅读 |

## 使用方式

```bash
# 使用 v1.0（紧凑）
npx aipioneer-publisher publish "链接" --theme ai-pioneer-v1

# 使用 v3.0（清晰）
npx aipioneer-publisher publish "链接" --theme ai-pioneer-v3
```
