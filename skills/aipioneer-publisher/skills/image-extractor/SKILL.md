---
name: image-extractor
description: |
  自动提取网页中的所有图片。支持提取图片 URL、下载图片、筛选特定尺寸/格式的图片。
  触发词：提取图片、下载网页图片、获取图片、网页图片提取。
---

# 网页图片提取器

自动提取网页中的所有图片，支持下载和筛选。

## 功能

- 提取网页中所有图片 URL
- 按尺寸筛选（宽度、高度）
- 按格式筛选（jpg、png、webp 等）
- 下载图片到本地
- 生成图片列表报告

## 使用方法

### 命令行

```bash
# 提取图片 URL
npx image-extractor extract "https://example.com"

# 下载所有图片
npx image-extractor download "https://example.com" --output ./images

# 筛选大尺寸图片
npx image-extractor extract "https://example.com" --min-width 800
```

### OpenClaw

```
@666Claw 提取 https://example.com 的所有图片
```

## 输出示例

```json
{
  "url": "https://example.com",
  "images": [
    {
      "src": "https://example.com/image1.jpg",
      "width": 1200,
      "height": 800,
      "format": "jpg",
      "alt": "描述文字"
    }
  ],
  "total": 15,
  "downloaded": 15
}
```