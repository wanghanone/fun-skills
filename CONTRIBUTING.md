# 贡献指南

欢迎提交新的「吃喝玩乐」玩法。这个仓库是**收集型**项目，最容易出问题的不是代码，而是来路不明的素材和无法复现的效果，所以准入标准侧重这两点。

## 准入清单

提交 PR 前请逐项确认：

- [ ] skill 放在 `skills/<name>/`，目录名为小写字母、数字与连字符，且与 `SKILL.md` 的 `name` 完全一致。
- [ ] `description` 同时写清「做什么」和「什么时候用」，不超过 1024 字符。
- [ ] `SKILL.md` 正文少于 500 行；长文档拆到 `references/`，脚本放 `scripts/`，色卡与模板放 `assets/`，文件引用只用一层相对路径。
- [ ] 指令里不写本机绝对路径，不依赖未声明的环境变量；依赖（Python 版本、第三方库、系统工具）在该 skill 的 `README.md` 里列全。
- [ ] 有给人看的 `README.md`：一段说明、效果截图、快速开始命令、示例输入输出。
- [ ] `examples/` 里至少有一张小尺寸成品图（生成物如大 PDF、高清原图不要提交）。
- [ ] 不含平台私有文件（`_user_meta.json`、`agents/openai.yaml` 等已由 `.gitignore` 排除）。
- [ ] 用到的第三方资源（色卡、字体、图标、素材图）在 `THIRD_PARTY_NOTICES.md` 登记来源与许可，并在资源目录里保留原许可文件；禁止提交来源不明或禁止再分发的素材。
- [ ] 本地跑 `bash scripts/validate.sh` 通过。
- [ ] 更新根目录 `README.md` 的技能目录表与 `.claude-plugin/marketplace.json` 的 `skills` 数组。

## 操作步骤

```bash
cp -r template skills/weekend-planner
# 1. 改目录名与 SKILL.md 的 name、description
# 2. 补齐 README.md 和 examples/
bash scripts/validate.sh
```

校验脚本会检查 frontmatter、目录名、正文行数、相对引用、平台私有文件，以及 README 目录表与 marketplace.json 是否与 `skills/` 一致。CI 对每个 PR 跑同一套检查。

## 关于授权（重要）

**提交 PR 即表示你同意：你提交的内容以本仓库的 [MIT 许可](LICENSE) 授权，且你确认自己有权这样授权。** 请不要提交从别处复制而来、未获授权或许可不明的 prompt、色卡、图片与代码；引用他人作品时，在 `THIRD_PARTY_NOTICES.md` 中如实登记。

## 提交规范

- 提交信息用简短英文，例如 `feat(skill): add weekend-planner`、`docs: update gallery`。
- 一个新 skill 一个 PR，方便评审与回滚。
- 想法还没成型时，先开「新玩法提案」issue 讨论，不必先写代码。
