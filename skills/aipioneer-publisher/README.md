# AIPioneer 公众号发布器

> 一键完成：素材获取 → 卡兹克风格改写 → AI Pioneer 纯黑样式排版 → 微信草稿箱发布

## ✨ 核心功能

- **智能获取**：支持 X/Twitter、网页文章、PDF 等多种素材
- **双风格改写**：write-skill 爆款风格 + 卡兹克 (Khazix) 活人感风格
- **智能图片**：自动提取、分类、匹配文章图片
- **专业排版**：AI Pioneer 纯黑样式，80px 大号章节标题
- **一键发布**：自动推送到微信公众号草稿箱

## 🚀 快速开始

### 1. 安装依赖

```bash
# 克隆项目
git clone https://github.com/你的用户名/aipioneer-publisher.git
cd aipioneer-publisher

# 安装依赖
npm install

# 配置环境变量
cp config/config.example.json config/config.json
# 编辑 config.json 填入你的微信配置
```

### 2. 配置微信

编辑 `config/config.json`：

```json
{
  "wechat": {
    "appId": "你的微信AppID",
    "appSecret": "你的微信AppSecret"
  },
  "server": {
    "port": 3000
  }
}
```

### 3. 启动服务

```bash
npm run dev
```

### 4. 开始发布

```bash
npm run publish "https://x.com/用户名/status/推文ID"
```

## 📋 使用示例

### 命令行使用

```bash
# 发布 X/Twitter 文章（默认 write-skill 风格）
npx aipioneer-publisher publish "https://x.com/garrytan/status/123456"

# 发布网页文章
npx aipioneer-publisher publish "https://example.com/article"

# 使用 write-skill 风格（爆款写法，高启示率）
npx aipioneer-publisher publish "链接" --style write-skill

# 使用 khazix 风格（卡兹克活人感写法）
npx aipioneer-publisher publish "链接" --style khazix

# 使用特定排版
npx aipioneer-publisher publish "链接" --theme ai-pioneer-black

# 完整示例：write-skill + 自动图片 + 纯黑样式
npx aipioneer-publisher publish "链接" \
  --style write-skill \
  --with-images \
  --auto-cover \
  --theme ai-pioneer-black
```

### 作为 OpenClaw Skill 使用

在 OpenClaw 中：

```
@666Claw 帮我发布这篇文章：https://x.com/用户名/status/推文ID
```

## 🎨 支持的写作风格

| 风格 | 特点 | 适用场景 |
|------|------|----------|
| **write-skill** | 高启示率、强钩子、信息密集、情绪驱动 | 热点解读、产品发布、观点输出 |
| **khazix** | 口语化、朋友聊天感、渐进节奏、文化升维 | 深度长文、人物故事、行业分析 |

## 🎨 支持的排版样式

| 样式 | 版本 | 主色 | 特点 |
|------|------|------|------|
| **ai-pioneer-v1** | v1.0 | `#000000` | 纯黑标签 + 章节数字重叠 + 浅灰引用 |
| **ai-pioneer-v2** | v2.0 | `#0E61AC` | 品牌头图 + 奶润米杏引用 + 深海宝蓝强调 |
| **ai-pioneer-v3** | v3.0 | `#000000` | 章节数字在标题上方（无遮挡）+ 浅灰引用 |

### 版本选择建议

- **v1.0**: 极简现代，适合短平快的热点内容
- **v2.0**: 温暖专业，适合品牌感强的深度内容
- **v3.0**: 清晰阅读，适合长文和复杂结构内容（推荐）

### 使用示例

```bash
# v1.0 - 纯黑极简
npx aipioneer-publisher publish "链接" --theme ai-pioneer-v1

# v2.0 - 深海宝蓝
npx aipioneer-publisher publish "链接" --theme ai-pioneer-v2

# v3.0 - 章节数字优化（推荐）
npx aipioneer-publisher publish "链接" --theme ai-pioneer-v3
```

## 🛠️ 系统架构

```
用户输入链接
    ↓
[Fetcher] 获取内容 (X/Twitter/网页/PDF) + 提取图片
    ↓
[Writer] 选择风格改写
    ├─ write-skill: 爆款写法（高启示率）
    └─ khazix: 活人感写法（渐进节奏）
    ↓
[Image Processor] 智能图片处理
    ├─ 分类: 封面/Hero/数据/场景/概念
    ├─ 匹配: 按内容插入对应位置
    └─ 上传: 自动上传到微信图床
    ↓
[Formatter] AI Pioneer 纯黑样式排版
    ↓
[Publisher] 推送到微信草稿箱
    ↓
返回 Media ID
```

## 📦 项目结构

```
aipioneer-publisher/
├── src/
│   ├── fetcher/          # 内容获取模块
│   ├── writer/           # 写作风格模块
│   ├── formatter/        # 排版样式模块
│   └── publisher/        # 发布功能模块
├── config/               # 配置文件
├── scripts/              # 脚本工具
├── docs/                 # 文档
└── README.md             # 本文件
```

## 🔧 配置说明

### 必需配置

1. **微信公众号配置**
   - AppID
   - AppSecret
   - IP 白名单（添加你的服务器 IP）

2. **OpenClaw 配置**（可选）
   - Gateway 地址
   - 浏览器自动化配置

### 可选配置

- 自定义样式
- 自定义写作风格
- 自动发布设置

## 📝 写作方法论

### write-skill 方法论

基于「写作只解决一个问题」理念：

1. **明确类别** - 细分领域，找到攀登阶梯
2. **独特风格** - 在教育↔娱乐光谱上定位
3. **启示率** - 信息密度和递进速度
4. **具体性** - 越具体越能击中人心

详见 `skills/write-skill/SKILL.md`

### khazix 方法论

卡兹克开源写作风格：

1. **口语化** - 像跟朋友聊天
2. **渐进节奏** - 由浅入深，层层递进
3. **文化升维** - 从具体案例上升到文化层面
4. **活人感** - 有情绪、有观点、有态度

详见 `skills/khazix-skills/khazix-writer/SKILL.md`

## 🤝 贡献指南

欢迎提交 Issue 和 PR！

## 📄 许可证

MIT License

## 🙏 致谢

- 卡兹克 (Khazix) 写作风格
- wechat-typesetting 项目
- OpenClaw 社区