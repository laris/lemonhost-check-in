import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 从环境变量获取账号密码
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
URL = "https://dash.lemonhost.me/"

# 运行持续时间（秒），1小时 = 3600秒
DURATION = 3600 

def run_bot():
    # 设置 Chrome 浏览器参数
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 无头模式，无界面运行
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # 针对部分反爬虫机制的伪装
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        print(f"正在打开页面: {URL}")
        driver.get(URL)
        
        wait = WebDriverWait(driver, 30)

        # 1. 输入邮箱
        print("正在定位邮箱输入框...")
        email_input = wait.until(EC.presence_of_element_located((By.ID, "login-email")))
        email_input.clear()
        email_input.send_keys(EMAIL)

        # 2. 输入密码
        print("正在定位密码输入框...")
        password_input = driver.find_element(By.ID, "login-password")
        password_input.clear()
        password_input.send_keys(PASSWORD)

        # 3. 点击登录按钮 (匹配 class btn-primary 或 type=submit)
        print("正在点击登录按钮...")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # 等待登录后的页面加载
        time.sleep(15)
        print(f"当前页面标题: {driver.title}")
        print("登录操作完成，开始保活循环...")

        # 4. 保持活跃 (循环运行指定时间)
        start_time = time.time()
        while time.time() - start_time < DURATION:
            current_duration = int(time.time() - start_time)
            remaining = DURATION - current_duration
            
            print(f"已运行: {current_duration}秒, 剩余: {remaining}秒")
            
            # 每 10 分钟 (600秒) 刷新一次页面以保持活跃
            if current_duration > 0 and current_duration % 600 == 0:
                print("执行页面刷新...")
                driver.refresh()
                time.sleep(10) # 等待刷新完成
            
            # 每分钟检查一次
            time.sleep(60)

    except Exception as e:
        print(f"发生错误: {str(e)}")
        # 输出页面源码片段以便调试（可选）
        # print(driver.page_source[:500])
        raise e
    finally:
        driver.quit()
        print("脚本运行结束")

if __name__ == "__main__":
    if not EMAIL or not PASSWORD:
        print("错误: 未设置 EMAIL 或 PASSWORD 环境变量")
        exit(1)
    run_bot()
