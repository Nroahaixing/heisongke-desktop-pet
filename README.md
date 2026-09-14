# 黑松克桌面宠物 · 动作框架

桌面宠物角色的动作素材库 + 一个可交互的演示页面。

## 目录结构

```
assets/
├── normal/       # 待机 · 9帧（无操作满3分钟自动触发一次，其余时间静止）
├── levelup/      # 升级 Lv.2~Lv.5 撒花动画 · 16帧
├── wave/         # 挥手打招呼 · 12帧
├── idea/         # 灵感/想法（头顶灯泡）· 12帧
├── followup/     # 深入追问（戴眼镜+问号）· 16帧
├── lv2/ ~ lv5/   # 升级状态占位（共用 levelup 撒花动画）
├── crosslink/    # 跨学科同源 · 16帧
├── savecard/     # 存为知识卡片 · 18帧
├── mastered/     # 复习考核掌握 · 16帧
├── forgotten/    # 复习遗忘/模糊 · 16帧
├── savecard/     # 存为知识卡片（占位）
├── mastered/     # 复习掌握（占位）
├── forgotten/    # 复习遗忘/模糊（占位）
├── newnote/      # 新建笔记 · 10帧
├── newbook/      # 整理书架/新建书籍（占位）
└── actions.json  # 动作清单：每个状态的中文名、触发时机、帧数、状态

demo/
├── demo_template.html  # 演示页模板（占位符 __FRAMES_JSON__ 会被替换成真实图片数据）
├── gen_demo.py          # 读取 assets/ 下的图片、生成可直接打开的 demo/pet_demo.html
└── pet_demo.html        # 生成好的静态演示页，通过相对路径加载 assets 中的图片

wave.zip / idea.zip / followup.zip / crosslink.zip   # 对应状态的图片打包，文件名和内部图片名统一按 <状态>_<序号>.png 命名
```

## 命名规则

每个动作状态一个文件夹，帧图片按 `状态_序号.png` 命名（如 `wave_1.png ~ wave_12.png`），方便代码按顺序批量加载。`assets/actions.json` 登记了每个状态的标签、触发时机、帧数和路径，新增动作只要：

1. 在 `assets/` 下建一个新文件夹，放入 `状态_序号.png`
2. 在 `actions.json` 里补一条记录
3. （可选）跑一遍 `demo/gen_demo.py` 重新生成演示页

## 查看演示

直接用浏览器打开 `demo/pet_demo.html`，或者改完素材后重新生成：

```bash
cd demo
python3 gen_demo.py
```

`gen_demo.py` 只把图片相对路径写入 HTML，不再将 PNG 转成 Base64 嵌入；因此在线部署时需同时提供 `assets/` 目录。

### 发布到公网（GitHub Pages）

仓库已附带 `.github/workflows/deploy-pages.yml`。推送到 `main` 后，GitHub Actions 会自动把 `demo/pet_demo.html` 发布为站点首页。

首次使用时，在仓库的 **Settings → Pages** 将 **Source** 设为 **GitHub Actions**。部署完成后访问：

`https://nroahaixing.github.io/heisongke-desktop-pet/`

## 目前进度

- ✅ normal（待机，无操作满3分钟自动触发一次，其余时间显示静止帧）、升级撒花（Lv.2~Lv.5 共用）、wave（挥手打招呼）、idea（灵感/想法）、followup（深入追问）、crosslink（跨学科同源）、savecard（存为知识卡片）七类状态已配好素材
- ⬜ 学习类动作（对接心潮记忆笔记应用的事件）：
  - newbook 整理书架/新建书籍 — 整理书架或新建书籍时

以上占位状态都已经在 `assets/actions.json` 里登记好（`frameCount: 0`，`status: 待补充`），素材到位后按「命名规则」放图、把 `frameCount`/`status` 改掉即可。
