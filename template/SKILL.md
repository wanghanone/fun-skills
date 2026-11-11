---
name: your-skill-name
description: 一句话说明这个 skill 做什么、产出什么，再写清「用户要求……时使用」。不超过 1024 字符，name 必须与目录名完全一致。
license: MIT
metadata:
  version: "0.1.0"
---

# 技能标题

> 复制本目录后请删除这段说明。`SKILL.md` 是给 Agent 读的指令，控制在 500 行内；长文档放 `references/`，脚本放 `scripts/`，静态资源放 `assets/`，成品图放 `examples/`（给人看的 `README.md` 里引用）。

## 输入与默认值

写清最少需要什么、不知道时用什么默认值、哪些信息不要反问用户。

## 制作流程

1. 检查输入。
2. 执行主要步骤（需要脚本时写清相对路径与调用命令）。
3. 视觉或结果复核。
4. 验证交付物。

## 交付物

列出输出文件、格式与用户能拿到的东西。

## 关键约束

列出不能违反的边界：尺寸、数量上限、素材许可、不得静默修改的部分等。

## 参考

- 可选参数与细节见 [references/REFERENCE.md](references/REFERENCE.md)。
