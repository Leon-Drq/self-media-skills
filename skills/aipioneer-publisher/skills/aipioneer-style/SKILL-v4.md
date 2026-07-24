---
name: aipioneer-style-v4
description: |
  AI Pioneer 公众号排版样式 v4.0 - 紧凑阅读版
  基于 v3.0 修改：
  - 正文从 16px 改为 15px
  - 整体文章两端缩进 8px
  - 更紧凑的阅读体验
---

# AI Pioneer 样式 v4.0（紧凑阅读版）

## 版本信息

- **版本**: v4.0.0
- **名称**: AI Pioneer 紧凑阅读版
- **基于**: v3.0 章节数字优化版
- **改进**: 字体缩小，两端缩进，更紧凑

## 与 v3 的区别

```
v3: 16px 正文，无缩进
v4: 15px 正文，两端缩进 8px
```

## 全局容器（新增）

```html
<!-- 文章全局容器：两端缩进 8px -->
<div style="padding:0 8px;">

  <!-- 首句 -->
  <p style="font-size:15px;color:#333;line-height:2.0;margin:0 0 16px;">
    <b style="color:#000;">首句内容</b>
  </p>

  <!-- 章节数字 -->
  <p style="margin:32px 0 0;font-size:64px;font-weight:700;color:rgba(0,0,0,0.08);line-height:1;letter-spacing:-2px;">01</p>

  <!-- 章节标题 -->
  <p style="margin:8px 0 24px;font-size:22px;font-weight:700;color:#000;line-height:1.3;">章节标题</p>

  <!-- 正文 -->
  <p style="font-size:15px;color:#333;line-height:2.0;margin:0 0 16px;">正文内容</p>

  <!-- 引用块 -->
  <p style="font-size:15px;color:#000;font-weight:700;line-height:2.0;margin:0 0 16px;padding:12px 16px;background:#F5F5F5;border-radius:8px;">
    金句内容
  </p>

  <!-- 列表 -->
  <p style="font-size:15px;color:#333;line-height:2.0;margin:0 0 16px;padding-left:20px;">
    - 列表项 1<br>
    - 列表项 2
  </p>

</div>
```

## 关键样式参数

| 元素 | v3.0 | v4.0 |
|------|------|------|
| 全局容器 | 无 | `padding:0 8px` |
| 正文大小 | 16px | **15px** |
| 章节数字 | 64px, rgba(0,0,0,0.08) | 64px, rgba(0,0,0,0.08) |
| 章节标题 | 22px, #000 | 22px, #000 |
| 引用块 | 16px | **15px** |
| 列表项 | 16px | **15px** |
| 行高 | 2.0 | 2.0 |
| 段间距 | 16px | 16px |

## 使用场景

- 长文阅读：更紧凑，减少滚动
- 移动端优化：小字体更适合手机屏幕
- 信息密度高：单位面积展示更多内容

## 完整模板

```html
<!-- AI Pioneer v4.0 - 紧凑阅读版 -->
<div style="padding:0 8px;">

  <!-- 首句 -->
  <p style="font-size:15px;color:#333;line-height:2.0;margin:0 0 16px;">
    <b style="color:#000;">首句内容</b>
  </p>

  <!-- 章节数字 -->
  <p style="margin:32px 0 0;font-size:64px;font-weight:700;color:rgba(0,0,0,0.08);line-height:1;letter-spacing:-2px;">01</p>
  <!-- 章节标题 -->
  <p style="margin:8px 0 24px;font-size:22px;font-weight:700;color:#000;line-height:1.3;">章节标题</p>

  <!-- 正文 -->
  <p style="font-size:15px;color:#333;line-height:2.0;margin:0 0 16px;">正文内容</p>

  <!-- 引用块 -->
  <p style="font-size:15px;color:#000;font-weight:700;line-height:2.0;margin:0 0 16px;padding:12px 16px;background:#F5F5F5;border-radius:8px;">
    金句内容
  </p>

  <!-- 结尾 -->
  <p style="border-top:1px solid rgba(0,0,0,0.1);margin:32px 0 0;"><br></p>
  <p style="margin:0;padding:24px 0;text-align:center;">
    <span style="font-size:14px;color:#666;line-height:2;display:block;">关注「AI Pioneer」</span>
  </p>

</div>
```

## 版本历史

- **v4.0** (2026-05-07): 基于 v3.0，正文 15px，两端缩进 8px
- **v3.0** (2026-04-17): 章节数字独立一行，无遮挡
- **v2.0** (2026-04-15): 深海宝蓝 #0E61AC，奶油杏色引用
- **v1.0** (2026-04-14): 纯黑 #000000，极简风格
