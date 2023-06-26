import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 配置ChromeOptions以使用无界面模式
options = Options()
options.add_argument('--headless')  # 启用无界面模式

# 创建Chrome WebDriver对象
driver = webdriver.Chrome(options=options)

url = input("请输入要访问的网页：")

# 循环抓取值
while True:
    # 打开网页
    driver.get('http://' + url)

    # 等待页面加载完全
    time.sleep(2)

    # 找到具有特定id的元素
    try:
        element = driver.find_element(By.ID, 'total_requests')

        # 提取元素的文本内容
        value = element.text

        print(value)  # 输出动态生成的值

    except Exception as e:
        print("Error occurred:", str(e))

# 关闭浏览器
driver.quit()
