# 少色拼豆图纸 · bead-pattern

> 一张照片 → 逐格色号、可打印 PDF、每色用量清单。

![效果示意](examples/preview.png)

**当前状态：占位文档**。指令骨架已就位，生成脚本、色卡数据与成品图待迁入；迁入前不会产生图纸。

## 能做什么

- 把照片、插画或像素画量化成有限色数的拼豆网格。
- 按 1/2/4/6/8/12/16/24 色预算比较方案，兼顾主体轮廓与关键细节。
- 输出逐格色号图（PNG/PDF）、`grid.csv`、`beads.csv`、`pattern.json`，以及可选的分板图。

## 依赖

- Python 3.9+
- Pillow、NumPy（迁入实现后按实际脚本要求补充）
- 无需联网；生成物写入用户工作目录

## 快速开始

```bash
# 实现迁入后的预期用法（脚本尚未提供）
python3 skills/bead-pattern/scripts/make_pattern.py \
  --image examples/input.png --width 52 --height 52 --output ./output/beads
```

在客户端里可以直接说：「把这张图做成 52×52 的拼豆图纸，尽量少用颜色」。

## 示例输入与产出

| 输入 | 产出 |
| --- | --- |
| `examples/input.png`（待补） | `examples/preview.png`、`pattern.pdf`、`beads.csv`（待补） |

## 素材与许可

计划使用社区整理的 MARD 221 参考色卡（MIT，Copyright (c) 2020 maxcleme）。迁入数据文件时须同时复制 `assets/MARD_PALETTE_LICENSE.txt`，并在根目录 `THIRD_PARTY_NOTICES.md` 补齐来源链接。色号仅供参考，不是官方实测色值。
