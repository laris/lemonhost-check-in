# LemonHost Auto Login & Keep Alive

这是一个基于 **GitHub Actions** 和 **Python Selenium** 的自动化脚本，专用于 [Dash LemonHost](https://dash.lemonhost.me/) 的自动登录与活跃保持。

## ✨ 功能特点

* **自动登录**：自动填写邮箱与密码并完成登录。
* **会话保活**：登录成功后保持浏览器运行 **1 小时**。
* **防超时**：运行期间每 10 分钟自动刷新一次页面，防止 Session 过期。
* **定时运行**：默认配置为 **每 3 天** 自动执行一次。
* **无头模式**：使用 Chrome Headless 模式，无需图形界面即可在服务器端运行。

## 🚀 使用方法

### 1. 准备代码
将本项目中的文件上传到你的 GitHub 仓库：
* `main.py` (主程序)
* `.github/workflows/keep_alive.yml` (自动运行配置)
* `requirements.txt` (可选，虽然 workflow 里直接安装了 selenium，但保留个依赖文件是好习惯)

### 2. 配置账号密码 (Secrets)
为了安全起见，**不要**将密码直接写在代码里。请按以下步骤配置：

1.  进入你的 GitHub 仓库页面。
2.  点击顶部菜单栏的 **Settings** (设置)。
3.  在左侧导航栏找到 **Secrets and variables** -> **Actions**。
4.  点击 **New repository secret** 按钮，添加以下两个变量：

| Name (名称) | Value (值) | 说明 |
| :--- | :--- | :--- |
| `LEMON_EMAIL` | `你的邮箱@example.com` | 你的登录邮箱 |
| `LEMON_PASSWORD` | `你的密码` | 你的登录密码 |

### 3. 启用 Actions
如果是 Fork 的仓库，默认 Actions 可能是禁用的。
1.  点击顶部菜单栏的 **Actions**。
2.  点击绿色按钮 **I understand my workflows, go ahead and enable them**。

### 4. 手动测试
配置完成后，你可以手动触发一次以确保脚本正常工作：
1.  点击 **Actions** 选项卡。
2.  在左侧选择 **LemonHost Auto Login**。
3.  点击右侧的 **Run workflow** 按钮。

---

## ⚙️ 高级配置

### 修改运行时长
默认运行 **1 小时**。如需修改，请编辑 `main.py` 文件：

```python
# 运行持续时间（秒），1小时 = 3600秒
DURATION = 3600  # 修改这里的数字
