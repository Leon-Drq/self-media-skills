# 自媒体技能专区

这是一个面向自媒体选题、文案、开头、分镜、发布与复盘的 Agent Skills 仓库。所有技能统一放在 `skills/` 下，方便持续新增、独立安装和版本管理。

## 技能目录

| 技能 | 用途 |
| --- | --- |
| [百万播放爆款开头](skills/million-view-opening-hooks/SKILL.md) | 使用连环否定、一招搞定、只问不答、树立敌人、放大损失五种结构，设计黄金 3 秒和前 12 秒承接 |
| [抖音爆款策划师](skills/douyin-viral-planner/SKILL.md) | 策划抖音选题、口播脚本、黄金 3 秒、分镜、标题封面、互动收尾和发布测试 |
| [口播删稿编导](skills/cut-spoken-script/SKILL.md) | 删除正确废话，把形容词改成动作与证据，并把行业大词改成用户会说的话 |
| [封面设计](skills/cover-design-open/SKILL.md) | 使用 10 种构图风格、真人参考图和产品素材，生成公众号、小红书、B站与短视频封面提示词 |
| [AI Pioneer 深度写作](skills/ai-pioneer-deep-writing/SKILL.md) | 将 AI/科技新闻、论文、产品与产业事件写成有证据链、真实配图和可传播判断的深度公众号文章 |
| [AI Pioneer 新闻写作](skills/ai-pioneer-news/SKILL.md) | 把 AI 热点快速写成信息密度高、包含真实配图的短新闻深度稿 |
| [Deep Writer 公众号写作](skills/deep-writer-wechat/SKILL.md) | 用主理人视角组织深度、判断、细节和读者共鸣 |
| [科技公众号深度解读](skills/tech-wechat-deep-dive/SKILL.md) | 深度拆解科技新闻、产品发布、论文和产业事件 |
| [卡兹克公众号长文](skills/khazix-writer/SKILL.md) | 用卡兹克式现场感、好奇心和人话表达创作公众号长文 |
| [人味儿写作](skills/renwei-writing/SKILL.md) | 在润色和改写时保留作者的个性、经验与真实情绪 |
| [中文去 AI 味](skills/humanizer-zh/SKILL.md) | 清理模板化转折、机械表达、空洞排比和过度解释 |
| [X Article 个人观察](skills/x-article-personal-observation/SKILL.md) | 把中文 AI/科技素材改写成带个人判断的英文 X 长文 |
| [AI HOT](skills/aihot/SKILL.md) | 获取当天及最近一周的 AI 新闻、论文、产品和行业热点 |
| [微信文章转 Markdown](skills/wechat-article-to-markdown/SKILL.md) | 获取公众号文章、下载图片并转换成干净的 Markdown 素材 |
| [AI Pioneer 发布器](skills/aipioneer-publisher/SKILL.md) | 完成素材获取、写作、真实图片处理、品牌排版和公众号草稿箱发布 |
| [YouTube 转公众号草稿](skills/youtube-ai-pioneer-draft/SKILL.md) | 把 YouTube 视频转成带转录、配图和固定 Banner 的 AI Pioneer 文章 |
| [素材到卡兹克长文](skills/aipioneer-publisher/skills/khazix-from-materials/SKILL.md) | 从访谈、截图、数据和真实使用素材组织有现场感的文章 |
| [AI Pioneer 排版样式](skills/aipioneer-publisher/skills/aipioneer-style/SKILL.md) | 提供 AI Pioneer 黑白极简公众号排版模板 |
| [网页图片提取](skills/aipioneer-publisher/skills/image-extractor/SKILL.md) | 提取、筛选并下载网页中的真实图片 |
| [赛博技术写作](skills/aipioneer-publisher/skills/saibo-writer/SKILL.md) | 面向硬核技术主题进行原理拆解和专业解读 |
| [爆款写作方法](skills/aipioneer-publisher/skills/write-skill/SKILL.md) | 围绕一个核心问题组织高传播效率的自媒体文章 |
| [爆款写作方法 v2](skills/aipioneer-publisher/skills/write-skill-v2/SKILL.md) | 在传播效率之外增强技术深度、证据和逻辑推进 |

## 目录约定

```text
self-media-skills/
├── README.md
└── skills/
    └── skill-name/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── references/
        └── scripts/
```

每个技能保持独立，只保留完成任务所需的指令和参考资料。后续新增技能时，同时在上方“技能目录”中增加一行索引。

## 安装

安装全部顶层技能：

```bash
git clone https://github.com/Leon-Drq/self-media-skills.git
mkdir -p ~/.codex/skills
cp -R self-media-skills/skills/* ~/.codex/skills/
```

只安装单个技能：

```bash
cp -R self-media-skills/skills/ai-pioneer-deep-writing ~/.codex/skills/
```

`aipioneer-publisher` 目录内包含排版、图片提取、卡兹克素材写作、赛博技术写作和两版爆款写作子技能。

## 来源与许可

仓库保留了各技能原有的许可证和作者说明。部分第三方技能来自以下公开项目：

- [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)：`khazix-writer`、`aihot`
- [orange2ai/renwei-writing](https://github.com/orange2ai/renwei-writing)：`renwei-writing`
- [op7418/humanizer-zh](https://github.com/op7418/humanizer-zh)：`humanizer-zh`
- [jackwener/wechat-article-to-markdown](https://github.com/jackwener/wechat-article-to-markdown)：`wechat-article-to-markdown`
