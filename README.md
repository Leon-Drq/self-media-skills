# 自媒体技能专区

这是一个面向自媒体选题、文案、开头、分镜、发布与复盘的 Agent Skills 仓库。所有技能统一放在 `skills/` 下，方便持续新增、独立安装和版本管理。

## 技能目录

| 技能 | 用途 |
| --- | --- |
| [百万播放爆款开头](skills/million-view-opening-hooks/SKILL.md) | 使用连环否定、一招搞定、只问不答、树立敌人、放大损失五种结构，设计黄金 3 秒和前 12 秒承接 |
| [抖音爆款策划师](skills/douyin-viral-planner/SKILL.md) | 策划抖音选题、口播脚本、黄金 3 秒、分镜、标题封面、互动收尾和发布测试 |

## 目录约定

```text
self-media-skills/
├── README.md
└── skills/
    └── skill-name/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references/
```

每个技能保持独立，只保留完成任务所需的指令和参考资料。后续新增技能时，同时在上方“技能目录”中增加一行索引。

## 安装单个技能

```bash
git clone https://github.com/Leon-Drq/self-media-skills.git
cp -R self-media-skills/skills/million-view-opening-hooks ~/.codex/skills/
cp -R self-media-skills/skills/douyin-viral-planner ~/.codex/skills/
```
