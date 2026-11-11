# fun-skills

> 把爱好交给 Agent：一张照片变成可打印的拼豆图纸，一段代码变成更会撒娇的桌宠。

一套「吃喝玩乐」向的 **Agent Skills** 集合：从生成拼豆图纸，到优化桌宠、安排周末玩法，把小爱好做成可一键安装、可复现的技能包。附成品示例与贡献模板。

每个技能都是一个自包含目录，遵循 [Agent Skills 开放规范](https://agentskills.io/specification)：`SKILL.md` 给 Agent 读，同名目录下的 `README.md` 给人看。分类（吃 / 喝 / 玩 / 乐）只作为标签，不做目录层级。

## 作品画廊

| 拼豆图纸 | 桌宠调优 |
| :---: | :---: |
| 待补效果图 `skills/bead-pattern/examples/preview.png` | 待补效果图 `skills/desktop-pet-tuneup/examples/before-after.png` |
| 一张照片 → 逐格色号、可打印 PDF、用量清单 | 优化前 / 优化后的运行对比 |

<!-- 图片就绪后，把上面的占位文字替换为：
![拼豆图纸](skills/bead-pattern/examples/preview.png)
![桌宠调优](skills/desktop-pet-tuneup/examples/before-after.png)
-->

## 技能目录

| 技能 | 分类 | 做什么 | 状态 |
| --- | --- | --- | --- |
| [bead-pattern](skills/bead-pattern/) | 玩 · 手作 | 照片或像素画 → 少色拼豆图纸、逐格色号、可打印 PDF、用量清单 | 占位，待迁入完整实现 |
| [desktop-pet-tuneup](skills/desktop-pet-tuneup/) | 玩 · 桌宠 | 现有桌宠项目的性能、动画、交互与素材优化 | 占位，待实现 |

新增技能时请同步更新这张表和 `.claude-plugin/marketplace.json`，CI 会检查两处是否一致。

## 安装

```bash
# 方式一：skills.sh，一键安装整套
npx skills add wanghanone/fun-skills

# 只装其中一个
npx skills add wanghanone/fun-skills --skill bead-pattern

# 方式二：作为 Claude Code 插件市场
/plugin marketplace add wanghanone/fun-skills
/plugin install play-skills@fun-skills

# 方式三：直接复制目录（WorkBuddy 等支持该规范的客户端）
cp -r skills/bead-pattern ~/.workbuddy-ai/skills/
```

## 仓库结构

```text
fun-skills/
├── README.md                          人看：画廊、目录表、安装命令
├── LICENSE                            MIT
├── THIRD_PARTY_NOTICES.md             第三方资源许可登记
├── CONTRIBUTING.md                    准入清单与 PR 约定
├── .claude-plugin/marketplace.json    一键安装整套技能
├── template/                          新 skill 起手模板
├── scripts/validate.py                格式校验（含 README 一致性）
├── .github/                           CI 工作流 + 新玩法提案模板
└── skills/
    ├── bead-pattern/                  一个 skill = 一个目录
    └── desktop-pet-tuneup/
        ├── SKILL.md                   给 Agent 读：frontmatter + 指令
        ├── README.md                  给人看：效果图、依赖、快速开始
        ├── scripts/                   可执行脚本
        ├── references/                按需加载的长文档
        ├── assets/                    色卡、模板等静态资源
        └── examples/                  示例输入与成品图
```

## 新增一个 skill

复制 `template/` → 改成小写连字符目录名 → 让 `name` 与目录名一致 → 写清 `description`（做什么 + 什么时候用）→ 补人看的 README 和 `examples/` 效果图 → 跑 `bash scripts/validate.sh` → 更新本页目录表与 marketplace.json → 提 PR。

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。想先聊想法，可以用「新玩法提案」issue 模板。

## 许可

本仓库自有内容采用 [MIT](LICENSE)。第三方资源（色卡、字体、示例图、桌宠素材等）以各自许可为准，登记在 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)——根目录 LICENSE 不覆盖这些资源。
