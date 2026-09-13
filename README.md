# 黑松克桌面宠物 · 动作框架

桌面宠物角色的动作素材库 + 一个可交互的演示页面。

## 目录结构

```
assets/
├── normal/       # 待机（占位，还没素材）
├── happy/        # 开心（占位）
├── shy/          # 害羞（占位）
├── surprised/    # 惊讶（占位）
├── wave/         # 挥手打招呼 · 12帧
├── idea/         # 灵感/想法（头顶灯泡）· 12帧
├── followup/     # 深入追问（戴眼镜+问号）· 16帧
└── actions.json  # 动作清单：每个状态的中文名、触发时机、帧数、状态

demo/
├── demo_template.html  # 演示页模板（占位符 __FRAMES_JSON__ 会被替换成真实图片数据）
├── gen_demo.py          # 读取 assets/ 下的图片、生成可直接打开的 demo/pet_demo.html
└── pet_demo.html        # 生成好的静态演示页，用浏览器直接打开即可播放动作

wave.zip / idea.zip / followup.zip   # 对应状态的图片打包，文件名和内部图片名统一按 <状态>_<序号>.png 命名
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

## 目前进度

- ✅ wave（挥手打招呼）、idea（灵感/想法）、followup（深入追问）三个状态已配好素材
- ⬜ normal / happy / shy / surprised 四个状态还是占位，等素材到位后照上面步骤接入
