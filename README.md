# Markdown 的常用语法简介（只记这些就够用）
| 功能    | 语法示例                          |
| ----- |-------------------------------|
| 一级标题  | `# 一级标题`                      |
| 二级标题  | `## 二级标题`                     |
| 粗体    | `**加粗文字**`                    |
| 斜体    | `*斜体文字*`                      |
| 列表    | `- 项目A` / `* 项目B` / `1. 项目C`  |
| 行内代码  | `` `print("Hello")` ``        |
| 多行代码块 | ` `python ... ` `             |
| 添加链接  | `[点击这里](https://example.com)` |
| 添加图片  | `![图片描述](图片链接)`               |
| 换行     | [space][space] / "<b_r>"      |



# 🐍 pythonCodes

这是我系统学习 Python 时记录的代码笔记项目，涵盖了单元测试、自动化框架、工具函数、模块练习等多个方向，持续维护中。

---

# 📁  Project Structure（项目结构）
pythonCodes/<br>
├── venv/ # 虚拟环境文件夹（已添加到 .gitignore)<br>
├── requirements.txt # pip依赖记录文件<br>
├── README.md # 项目说明<br>
├── test_learning/ # 单元测试相关笔记（unittest / pytest）<br>
├── notes/ # 基础语法、练习题、脚本实验区<br>
├── utils/ # 常用工具函数<br>
└── .gitignore # 忽略虚拟环境/缓存文件<br>

---
# ⚙️ Environment Requirements（环境说明）
- ✅ Python 版本：**3.11.8**<br>
- ✅ 推荐 IDE：PyCharm（或 VSCode)<br>
- ✅ 使用 Git Bash 作为默认终端<br>
- ✅ 已启用虚拟环境 `venv`<br>

---
# 🔧 Usage Instructions（使用说明）
- ### Clone the project（克隆项目）<br>
        git clone https://research-git.uiowa.edu/nnie/pythonCodes.git
        cd pythonCodes

- ### Create and activate virtual environment（创建并激活虚拟环境）
        python -m venv .venv
        $ source .venv/Scripts/activate # Git Bash 下的激活方式     
        deactivate


- ### Install dependencies（安装依赖）
        pip install -r requirements.txt   

- ### update requirements.txt (任何更新应该覆盖重写整个requirements.txt)
        pip freeze > requirements.txt
---

# 📦 Installed Dependencies（当前依赖）
### check requirements.txt

---





