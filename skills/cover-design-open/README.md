# 封面设计 Skill

根据文章或视频主题，通过逐步确认构图、人物、素材、背景和字体，生成可直接用于图片生成模型的封面提示词。

## 能力

- 支持公众号、小红书、B站与短视频封面设计
- 内置深色渐变、产品主视觉、海报拼贴、人物侧置留白等 10 种构图风格
- 支持人物身份参考图与产品图、UI 截图等多素材输入
- 明确人物姿势、主体比例、前中后景关系、标题字体与安全区

## 使用

向 Agent 提供文章内容或视频主题，并按提示逐项选择风格。也可以明确要求“全部由你决定”，让 Agent 自动完成设计取舍。

## 安装

```bash
git clone https://github.com/Leon-Drq/self-media-skills.git
cp -R self-media-skills/skills/cover-design-open ~/.codex/skills/
```

## 来源与许可

本技能收录自 [hongfamonvAI/oh-my-cover-design](https://github.com/hongfamonvAI/oh-my-cover-design)，上游项目标注为 MIT License。本仓库仅保留运行技能所需的指令与展示配置，未复制示例图片素材。
