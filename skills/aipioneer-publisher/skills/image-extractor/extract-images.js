#!/usr/bin/env node

/**
 * 网页图片提取器
 * 提取网页中的所有图片 URL
 */

const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs').promises;
const path = require('path');

class ImageExtractor {
  async extract(url, options = {}) {
    try {
      console.log(`🔍 正在提取: ${url}`);

      // 获取网页内容
      const response = await axios.get(url, {
        timeout: 30000,
        headers: {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
      });

      const $ = cheerio.load(response.data);
      const images = [];

      // 提取所有图片
      $('img').each((i, elem) => {
        const $img = $(elem);
        let src = $img.attr('src') || $img.attr('data-src') || $img.attr('data-original');

        if (!src) return;

        // 转换为绝对 URL
        if (src.startsWith('//')) {
          src = 'https:' + src;
        } else if (src.startsWith('/')) {
          const urlObj = new URL(url);
          src = `${urlObj.protocol}//${urlObj.host}${src}`;
        } else if (!src.startsWith('http')) {
          const urlObj = new URL(url);
          src = `${urlObj.protocol}//${urlObj.host}/${src}`;
        }

        const width = parseInt($img.attr('width')) || 0;
        const height = parseInt($img.attr('height')) || 0;

        images.push({
          src,
          alt: $img.attr('alt') || '',
          width,
          height,
          format: this.getFormat(src)
        });
      });

      // 筛选
      let filtered = images;

      if (options.minWidth) {
        filtered = filtered.filter(img => img.width >= options.minWidth || img.width === 0);
      }

      if (options.format) {
        filtered = filtered.filter(img => img.format === options.format);
      }

      // 去重
      const unique = [];
      const seen = new Set();
      for (const img of filtered) {
        if (!seen.has(img.src)) {
          seen.add(img.src);
          unique.push(img);
        }
      }

      console.log(`✅ 找到 ${unique.length} 张图片`);

      return {
        url,
        images: unique,
        total: unique.length
      };

    } catch (error) {
      throw new Error(`提取失败: ${error.message}`);
    }
  }

  getFormat(src) {
    const match = src.match(/\.(jpg|jpeg|png|webp|gif|svg)(\?|$)/i);
    return match ? match[1].toLowerCase() : 'unknown';
  }

  async download(images, outputDir = './images') {
    await fs.mkdir(outputDir, { recursive: true });

    const downloaded = [];

    for (let i = 0; i < images.length; i++) {
      const img = images[i];
      try {
        const response = await axios.get(img.src, {
          responseType: 'arraybuffer',
          timeout: 30000
        });

        const filename = `image_${String(i + 1).padStart(3, '0')}.${img.format === 'unknown' ? 'jpg' : img.format}`;
        const filepath = path.join(outputDir, filename);

        await fs.writeFile(filepath, response.data);

        downloaded.push({
          ...img,
          localPath: filepath,
          filename
        });

        console.log(`✅ 下载: ${filename}`);
      } catch (error) {
        console.log(`❌ 失败: ${img.src} - ${error.message}`);
      }
    }

    return downloaded;
  }
}

// CLI
async function main() {
  const url = process.argv[2];
  if (!url) {
    console.log('用法: node extract-images.js <url> [output-dir]');
    process.exit(1);
  }

  const outputDir = process.argv[3] || './images';

  const extractor = new ImageExtractor();

  try {
    const result = await extractor.extract(url, { minWidth: 400 });

    // 保存列表
    await fs.writeFile(
      path.join(outputDir, 'images.json'),
      JSON.stringify(result, null, 2)
    );

    console.log('\n📊 图片列表:');
    result.images.forEach((img, i) => {
      console.log(`${i + 1}. ${img.src}`);
      console.log(`   格式: ${img.format}, 尺寸: ${img.width}x${img.height}`);
    });

    // 下载
    console.log('\n⬇️  开始下载...');
    const downloaded = await extractor.download(result.images, outputDir);

    console.log(`\n✅ 完成！下载了 ${downloaded.length}/${result.total} 张图片`);
    console.log(`📁 保存位置: ${outputDir}`);

  } catch (error) {
    console.error('❌ 错误:', error.message);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = ImageExtractor;