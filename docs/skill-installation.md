# Skill 系统安装说明

这份说明用于解释，如何把 `huozhongche-skill` 作为一个完整的 Skill 系统安装使用。

核心建议只有一句话：

> 最好整体安装整个仓库，而不是只摘取其中某一段提示词。

因为这套系统真正发挥效果，依赖的是以下几部分协同工作：

- `SKILL.md` 中的主流程
- `scripts/` 中的辅助脚本
- `templates/` 中的通用提示词模板
- `examples/` 中的案例与前置素材收集表
- `docs/` 中的结构理解与培训说明

## 推荐安装方式

推荐优先级如下：

1. 安装到 Codex
2. 安装到其他支持 Skill 或知识包的平台
3. 无法安装时，再退回到通用提示词模式

## 方式一：安装到 Codex

这是当前仓库原生支持最好的一种方式。

### 步骤 1：获取仓库

你可以通过两种方式获取：

- 直接下载 GitHub 仓库压缩包并解压
- 用 Git 克隆仓库到本地

例如：

```bash
git clone https://github.com/xiangzi-cyber/huozhongche-skill.git
```

### 步骤 2：放入本地 Skill 目录

把整个仓库目录放到本地 Skill 目录中，并确保最终目录名为：

```text
huozhongche-skill
```

典型结构如下：

```text
$CODEX_HOME/skills/huozhongche-skill/
├── SKILL.md
├── scripts/
│   └── dedup_check.py
├── templates/
│   └── universal-writing-prompt.md
├── docs/
├── examples/
└── references/
```

### 步骤 3：重启或重新加载

把目录放好之后，重启 Codex，或重新加载本地 Skill。

### 步骤 4：验证是否安装成功

你可以直接发起一个测试任务，例如：

- “请按 AI火种车数智课堂写作系统，先梳理这份素材表并识别缺口。”
- “请先给我 2-3 个主线方向，不要直接写成稿。”

如果系统表现出以下特征，就说明安装基本成功：

- 会先做信息梳理
- 会主动识别缺口
- 会要求课表、日期、人名等关键信息
- 会在正式写稿前先给主线和结构建议

## 方式二：安装到其他 Skill 系统或知识包平台

如果你使用的不是 Codex，但平台支持以下任一能力，也可以迁移：

- 自定义 Skill
- 自定义 Agent
- 知识包 / 知识库导入
- 本地目录型工作流

### 推荐导入方式

优先推荐把整个仓库作为一个整体知识包导入。

如果平台不支持完整目录导入，至少建议保留这些内容：

- `SKILL.md`
- `templates/universal-writing-prompt.md`
- `examples/material-intake/`
- `examples/phase-1-pdfs/`
- `docs/skill-understanding.html`
- `docs/editor-training-deck.html`

如果平台支持脚本执行或本地工具，也尽量保留：

- `scripts/dedup_check.py`

### 迁移时的原则

如果目标平台没有“Skill 自动触发”机制，建议这样配置：

1. 把 `SKILL.md` 作为系统级主说明
2. 把 `templates/universal-writing-prompt.md` 作为可直接调用的标准提示词
3. 把 `examples/` 作为案例参考材料
4. 把 `docs/` 作为培训和理解材料

这样做的目标不是一比一复制 Codex 行为，而是尽量保留这套系统的完整结构。

## 不推荐的安装方式

以下方式虽然能用，但效果通常会明显打折：

- 只复制一句提示词
- 只拿 `SKILL.md`，不保留案例和模板
- 只给模型一个素材表，就要求它一步出终稿
- 完全跳过前置素材收集和缺口识别阶段

## 推荐的安装后使用顺序

安装完成后，建议按下面的顺序用：

1. 先用前置素材收集表把输入补齐
2. 让系统完成信息梳理与缺口识别
3. 再确定主线和结构
4. 再进入正式写稿
5. 最后做配图建议、去重检查和终稿交付

## 一句话总结

这套系统不是一段孤立提示词，而是一套“流程 + 模板 + 案例 + 脚本 + 协作文档”的组合包。

所以，真正推荐的安装方式是：

> 把整个仓库作为一个完整的 Skill 系统整体安装。
