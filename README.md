<div align="center">

# ☁️ tgstate-python
### 基于 Telegram 的无限私有云存储 & 永久图床系统

[![GitHub stars](https://img.shields.io/github/stars/buyi06/tgstate-python?style=flat-square)](https://github.com/buyi06/tgstate-python/stargazers)
[![License](https://img.shields.io/github/license/buyi06/tgstate-python?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/)

<p>
  <a href="#-核心特性">核心特性</a> •
  <a href="#-快速部署">快速部署</a> •
  <a href="#-配置指南">配置指南</a> •
  <a href="#-常见问题">常见问题</a>
</p>

</div>

---

## 📖 项目简介

**tgstate-python** 将您的 Telegram 频道或群组瞬间变身为功能强大的私有网盘与图床。无需服务器存储空间，借助 Telegram 的无限云端能力，实现文件管理、外链分享、图片托管与流媒体播放。

---

## ✨ 核心特性

| 功能 | 说明 |
| :--- | :--- |
| ♾️ **无限存储** | 依赖 Telegram 频道机制，容量无上限，零成本扩展。 |
| 🔗 **智能外链** | 生成简洁短链 (`/d/AbC123`)，自动适配当前访问域名/IP。 |
| ⚡ **极速上传** | 支持批量拖拽上传，大文件自动分块，体验丝滑。 |
| 🖼️ **图床模式** | 专为 Markdown/HTML 优化，支持 PicGo，一键复制引用。 |
| 🔒 **隐私安全** | 数据存储于私有频道，Web 端支持密码保护，安全可控。 |
| 📺 **流式播放** | 完美支持 HTTP Range，实现视频拖动进度条与断点续传。 |

---

## 🚀 快速部署

推荐使用一键脚本进行管理，支持安装、更新与维护。

### 1. 安装与更新 (推荐)
保留数据，适用于首次安装或版本更新。
```bash
bash -lc 'bash <(curl -fsSL [https://raw.githubusercontent.com/buyi06/tgstate-python/main/scripts/install.sh](https://raw.githubusercontent.com/buyi06/tgstate-python/main/scripts/install.sh))'

2. 重建容器
保留数据，仅重置运行环境，专治容器异常。
bash -lc 'bash <(curl -fsSL [https://raw.githubusercontent.com/buyi06/tgstate-python/main/scripts/reset.sh](https://raw.githubusercontent.com/buyi06/tgstate-python/main/scripts/reset.sh))'

3. 彻底卸载
⚠️ 高危操作：这将清空所有配置与数据，不可逆。
bash -lc 'bash <(curl -fsSL [https://raw.githubusercontent.com/buyi06/tgstate-python/main/scripts/purge.sh](https://raw.githubusercontent.com/buyi06/tgstate-python/main/scripts/purge.sh))'

> 💡 提示：脚本默认端口为 8000。如需非交互式安装，可预设环境变量：
> PORT=15767 BASE_URL=https://pan.example.com bash -lc ...
> 
⚙️ 配置指南
部署后首次访问网页将进入引导页设置管理员密码。之后请进入 “系统设置” 完成以下核心配置。
第一步：获取 BOT_TOKEN
 * 打开 Telegram 搜索 @BotFather 并点击 Start。
 * 发送 /newbot 创建新机器人。
 * 按提示输入机器人名称与用户名（必须以 bot 结尾）。
 * 获取 HTTP API Token，即为 BOT_TOKEN。
第二步：获取 Chat ID (CHANNEL_NAME)
 * 新建频道/群组：建议新建一个私密频道用于存储文件。
 * 添加管理员：将上一步创建的机器人拉入频道，并给予管理员权限（需有发消息权限）。
 * 获取 ID：
   * 在频道内发送任意文本消息。
   * 浏览器访问：https://api.telegram.org/bot<您的Token>/getUpdates
   * 在返回的 JSON 中找到 chat -> id（通常以 -100 开头）。
   * 注：如果是公开频道，也可以直接填写频道用户名（如 @my_channel）。
第三步：系统填报
回到网页端“系统设置”：
 * BOT_TOKEN: 填入第一步获取的 Token。
 * CHANNEL_NAME: 填入第二步获取的 Chat ID。
 * BASE_URL (可选): 您的对外访问域名（如 https://pan.example.com）。
🌐 反向代理设置
为获得最佳体验（如剪贴板复制、HTTPS），建议配合 Nginx 或 Caddy 使用。
<details>
<summary><strong>展开查看 Caddy 配置示例</strong></summary>
buyi.us.ci {
    encode gzip
    reverse_proxy 127.0.0.1:8000
}

</details>
<details>
<summary><strong>展开查看 Nginx 配置示例</strong></summary>
请务必透传 Host 与 X-Forwarded-* 头信息：
location / {
    proxy_pass [http://127.0.0.1:8000](http://127.0.0.1:8000);
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}

</details>
🛠️ 高级功能验证 (API & Headers)
系统对 Content-Disposition 和 Range 请求提供了企业级支持。
核心行为逻辑
 * 智能预览：图片、PDF、代码等默认 inline 预览。
 * 强制下载：链接附加 ?download=1 强制返回 attachment。
 * 流媒体支持：视频/音频响应 206 Partial Content，支持拖拽播放。
一键验收脚本
在 Linux/macOS 终端运行以下命令，验证服务器响应头是否合规：
<details>
<summary><strong>点击复制验收脚本</strong></summary>
bash -lc '
set -euo pipefail
# 请修改为您自己的域名和文件ID
BASE="${BASE_URL:-[https://pan.777256.xyz](https://pan.777256.xyz)}"
ID="${ID:-GNW2KH}"
URL="${BASE%/}/d/${ID}"

# 获取最终跳转地址
FINAL="$(curl -sS -L -o /dev/null -w "%{url_effective}" --max-time 15 "$URL" || true)"; [ -n "$FINAL" ] || FINAL="$URL"

echo "Target: $FINAL"
echo

echo "[1] HEAD 请求 (预期: 200/206)"
curl -sS -I --max-time 15 "$FINAL" | egrep -i "HTTP/|content-type|content-disposition|accept-ranges" || true
echo

echo "[2] Default GET (预期: inline for media)"
curl -sS -L -D - -o /dev/null --max-time 20 "$FINAL" | egrep -i "content-disposition:" || true
echo

echo "[3] Force Download (预期: attachment)"
curl -sS -L -D - -o /dev/null --max-time 20 "$FINAL?download=1" | egrep -i "content-disposition:" || true
echo

echo "[4] Range Request (预期: 206 + Content-Range)"
curl -sS -L -D - -o /dev/null --max-time 20 -H "Range: bytes=0-1023" "$FINAL" | egrep -i "HTTP/|content-range:" || true
'

</details>
❓ 常见问题 (FAQ)
<details>
<summary><strong>Q: 登录后循环跳转或报 500 错误？</strong></summary>
 * 密码字符：系统现已支持含特殊字符（中文、Emoji）的强密码。
 * Cookie：旧版本 Cookie 可能导致冲突，请尝试清除浏览器 Cookie 或使用无痕模式。
 * 重置数据：如遇顽固报错，可尝试重置数据卷（数据将丢失）：
   docker rm -f tgstate; docker volume rm tgstate-data; docker volume create tgstate-data
</details>
<details>
<summary><strong>Q: 删除文件后列表未刷新？</strong></summary>
删除为异步操作，受网络延迟影响。若刷新后文件仍在，请检查 Bot 是否具有频道管理员权限。
</details>
<details>
<summary><strong>Q: 分享链接显示为 127.0.0.1？</strong></summary>
前端会根据您的访问地址动态生成链接。请通过公网 IP 或域名访问网页，分享链接将自动更正。
</details>
<details>
<summary><strong>Q: 点击“复制链接”无反应？</strong></summary>
浏览器安全策略限制了非 HTTPS 环境下的剪贴板 API 调用。建议配置 HTTPS 反向代理以获得完整体验。
</details>
⚠️ 免责声明
> 请务必仔细阅读
> 
本项目基于 Telegram Bot API 实现，仅供 个人学习与技术研究 使用。
 * 合规性：Telegram 条款对将 Bot 用于“外部云存储服务”存在限制。
 * 禁止用途：
   * ❌ 严禁用于存储/分发盗版、色情、暴力等违法违规内容。
   * ❌ 严禁作为公共网盘或商业存储服务对外开放。
 * 风险自担：使用者需自行承担因使用本项目导致的数据丢失、账号封禁或法律风险。
<div align="center">
License MIT | Built with ❤️ by Buyi
</div>

