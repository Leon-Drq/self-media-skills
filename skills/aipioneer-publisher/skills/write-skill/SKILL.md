---
name: write-skill
description: |
  自媒体爆款写作方法论 Skill。基于「写作只解决一个问题」的核心理念，支持自动图片提取、智能图片匹配、封面自动生成。
  触发词：写文章、写爆款、自媒体写作、起号写作、写文案。
---

# 自媒体爆款写作方法论

> 写作只解决一个问题：如何在7天内做出一个有变现价值的千粉账号。

## 核心心法

### 1. 自媒体是一场比赛
- 你与所有内容竞争（包括猫咪视频、热点新闻）
- 必须有意识地参与游戏，了解规则、竞争对手
- 不是让你抄袭对标，而是找到自己的写作风格

### 2. 别把粉丝当人
- 粉丝是「未被满足的需求」，不是需要讨好的活人
- 用内容满足需求，而非追求认同
- 把粉丝当作需求检验工具

### 3. 别把写作当回事
- 写作就是把对朋友说的话搬到网上
- 感性（理解）+ 理性（真心考虑）= 自然表达
- 会说话就能写出爆款

### 4. 自媒体是数学题，不是作文题
- 目标是涨粉（影响力）和变现（利润）
- 优质内容只是策略之一
- 让等式左边的数字变大

## 四大核心支柱

### 支柱一：明确类别
**问题**：你知道自己在写什么领域吗？

**行动**：
1. 确定你的创作类别（如：个人成长 → 财务独立 → 穷人如何通过一人公司实现财务独立）
2. 找到类别中的「攀登阶梯」（谁是顶尖创作者？）
3. 或开创全新类别（如「人格成长」）

**原则**：类别越细分，越容易脱颖而出

### 支柱二：独特风格
**光谱定位**：教育 ↔ 娱乐

| 位置 | 特点 | 示例 |
|------|------|------|
| 教育端 | 信息、解释、洞见 | 教科书、新闻 |
| 娱乐端 | 吸引力、愉悦 | 故事、小说 |
| 中间跨界 | 独特定位 | 何同学（科技+人文）|

**秘诀**：在类别中做「出乎意料」的事

### 支柱三：启示率
**定义**：向读者传递新信息的速度

**高启示率示例**：
```
低：我坐在电脑前敲字，猫咪走过来，我摸了摸它...
高：猫咪飞奔而来，跳上桌子，一爪子把杯子扫落，
    玻璃渣刺进脚背，水溅到主机冒出白烟...
```

**检查清单**：
- [ ] 前2-3秒抓住注意力
- [ ] 每句话带来新信息
- [ ] 逻辑/情绪层层递进
- [ ] 300字内构建最强钩子

### 支柱四：具体性
**模糊 vs 具体**：

| 模糊 | 具体 |
|------|------|
| 我想学做饭 | 我想学做糖醋排骨 |
| 我想买车 | 我想买小米SU7 |
| 一人企业是提升收入的好方式 | 一人企业是普通人通过在数字平台提供手工艺品、软件服务或在线课程，实现月收入翻倍的绝佳方式 |

**测试**：不断问自己「还能再具体吗？」

## 图片处理系统（增强版）

### 1. 图片提取策略

**提取所有图片**：
```bash
# 提取网页中所有图片 URL
curl -s "https://example.com/article" | grep -oE 'https?://[^"<>]+\.(jpg|jpeg|png|webp|gif)' | sort -u
```

**筛选标准**：
- 宽度 ≥ 800px（高清图）
- 排除图标、logo、头像
- 优先选择：数据图表、产品截图、场景图

### 2. 智能图片分类

| 类型 | 特征 | 用途 | 位置 |
|------|------|------|------|
| **封面图** | 最大尺寸、最上方 | 文章封面、分享卡片 | 微信封面 |
| **Hero图** | 产品展示、界面截图 | 吸引眼球 | 文章开头 |
| **数据图** | 图表、benchmark、对比 | 证明观点 | 核心论述后 |
| **场景图** | 使用场景、案例展示 | 具体化 | 功能介绍后 |
| **概念图** | 架构图、流程图 | 解释原理 | 技术讲解后 |
| **嵌入推文** | 引用的 tweet 截图 | 案例证明 | 引用段落旁 |

### 2.1 X/Twitter 特殊处理

X 文章（长推文/文章）中常包含：
- **媒体图片**：直接附加的图片（media_entities）
- **嵌入推文**：引用的其他推文（atomic blocks / entityMap）

**提取方法**：
```bash
# 使用 fxtwitter API 获取完整内容
curl -s "https://api.fxtwitter.com/status/推文ID" | python3 -c "
import json, sys
data = json.load(sys.stdin)

# 提取媒体图片
tweet = data.get('tweet', {})
article = tweet.get('article', {})

# 1. 直接媒体图片
if 'media_entities' in article:
    for media in article['media_entities']:
        url = media.get('media_info', {}).get('original_img_url')
        if url:
            print(f'MEDIA: {url}')

# 2. 嵌入推文（需要进一步获取）
if 'entityMap' in article:
    for ent in article.get('entityMap', []):
        if ent.get('value', {}).get('type') == 'TWEET':
            tweet_id = ent.get('value', {}).get('data', {}).get('tweetId')
            print(f'EMBED_TWEET: {tweet_id}')
"

# 下载嵌入推文截图
for tweet_id in 嵌入推文ID列表; do
    curl -sL "https://api.fxtwitter.com/status/${tweet_id}" -o "tweet_${tweet_id}.json"
    # 提取推文中的图片
    python3 -c "
import json
with open('tweet_${tweet_id}.json') as f:
    data = json.load(f)
media = data.get('tweet', {}).get('media', {})
if 'photos' in media:
    for photo in media['photos']:
        print(photo.get('url'))
" | xargs curl -O
done
```

### 3. 图片匹配规则

**自动匹配逻辑**：
```
文章内容分析 → 识别关键段落 → 匹配对应图片类型

示例：
- "性能提升 13%" → 匹配 benchmark 图表
- "安全机制" → 匹配安全架构图
- "产品界面" → 匹配 UI 截图
```

### 4. 封面图自动生成

**策略**：
1. 提取文章首图（最大尺寸图片）
2. 如无合适图片，生成纯色封面（品牌色 + 标题）
3. 上传到微信素材库获取 thumb_media_id

**封面要求**：
- 尺寸：900 x 383（微信推荐）
- 格式：jpg 或 png
- 大小：≤ 2MB

### 5. 图片插入节奏

**标准布局**：
```
钩子段落（纯文字，快速进入）
    ↓
Hero 图（产品/场景，吸引眼球）
    ↓
核心论述 1（2-3 段）
    ↓
数据图（证明观点）
    ↓
核心论述 2（2-3 段）
    ↓
场景图/案例图（具体化）
    ↓
核心论述 3（2-3 段）
    ↓
概念图/架构图（解释原理）
    ↓
总结升华（纯文字，留白）
```

**原则**：
- 每 300-500 字一张图
- 图片必须有 caption 说明
- 避免连续两张图（文字缓冲）

### 6. 图片上传流程

```bash
# 1. 上传封面图（thumb）
curl -F "media=@cover.jpg" "https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=TOKEN&type=thumb"

# 2. 上传正文图片（获取 URL）
curl -F "media=@image.jpg" "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=TOKEN"

# 3. 替换 HTML 中的图片路径
# 4. 创建草稿
```

## 完整 Workflow（含图片）

### 步骤 1：获取素材
```bash
# 获取文章内容和所有图片
npx write-skill fetch "https://example.com/article" --with-images

# 输出：
# - article.json（内容）
# - images/（图片文件夹）
# - images.json（图片元数据：尺寸、格式、位置）
```

### 步骤 2：分析图片
- 分类：封面、Hero、数据、场景、概念
- 筛选：宽度 ≥ 800px
- 排序：按文章结构匹配

### 步骤 3：改写内容
- 应用 write-skill 方法论
- 预留图片插入位置
- 为每张图片写 caption

### 步骤 4：排版发布
```bash
npx write-skill publish "https://example.com/article" \
  --style write-skill \
  --with-images \
  --auto-cover \
  --min-image-width 800
```

## 常见图片问题及解决

| 问题 | 原因 | 解决 |
|------|------|------|
| 图片遗漏 | 只提取了部分图片 | 检查所有 img 标签，包括 data-src |
| 封面不匹配 | 没有自动选择首图 | 按尺寸排序，选择最大图片 |
| 图片位置错 | 没有按内容匹配 | 分析段落关键词，匹配对应图片类型 |
| 上传失败 | 图片太大或格式不对 | 压缩到 2MB 以下，转 jpg/png |
| 微信不显示 | 使用了相对路径 | 必须替换为微信图床 URL |

## 写作 Checklist（含图片）

### 创作前
- [ ] 明确类别：我在哪个细分领域竞争？
- [ ] 目标用户：他们的什么需求未被满足？
- [ ] 图片规划：需要几张图？什么类型？

### 创作中
- [ ] 启示率检查：前3段/30秒是否有强钩子？
- [ ] 具体性测试：还能再具体吗？
- [ ] 情绪触发：是否引发共鸣或争议？
- [ ] 图片匹配：每张图是否对应关键论述？

### 创作后
- [ ] 图片完整：是否遗漏关键图片？
- [ ] 封面合适：首图是否吸引人？
- [ ] 节奏检查：图片分布是否均匀？
- [ ] 开放结尾：是否促使用户留言/提问？

## 使用示例

**用户**：帮我写一篇关于「Claude Opus 4.7」的爆款文章

**我**：
1. **获取素材**：提取 Anthropic 博客内容和所有图片
2. **分析图片**：
   - 封面：产品主图（最大尺寸）
   - Hero：界面截图
   - 数据：benchmark 对比图
   - 场景：使用案例图
3. **改写内容**：write-skill 风格，高启示率
4. **插入图片**：
   - 开头：Hero 图
   - 性能部分：benchmark 图
   - 功能部分：界面截图
   - 安全部分：架构图
5. **上传发布**：自动生成封面，推送到草稿箱

**完整命令**：
```bash
npx write-skill publish "https://www.anthropic.com/news/claude-opus-4-7" \
  --style write-skill \
  --with-images \
  --auto-cover \
  --min-image-width 800 \
  --image-types hero,data,scene,concept
```