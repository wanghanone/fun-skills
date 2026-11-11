# Changelog

本文件记录仓库级别的重要变更。单个 skill 的版本写在各自 `SKILL.md` frontmatter 的 `metadata.version`。

格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，版本号遵循语义化版本。

## [0.1.0] - 2026-11-11

### 新增

- 仓库骨架：README 画廊与技能目录表、MIT 许可、第三方资源登记、贡献指南。
- `.claude-plugin/marketplace.json`：支持 Claude Code 一键安装。
- `scripts/validate.py` 与 `scripts/validate.sh`：校验 frontmatter、目录名、正文行数、相对引用、平台私有文件，以及 README / marketplace 与 `skills/` 的一致性。
- GitHub Actions 校验工作流与「新玩法提案」issue 模板。
- `template/`：新 skill 起手模板。
- `skills/bead-pattern/`、`skills/desktop-pet-tuneup/`：两个占位技能（功能实现待迁入）。
