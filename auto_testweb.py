from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建Chrome WebDriver实例 #記得要放chromedriver.exe 在 python 資料夾的 scripts 裡面
driver = webdriver.Chrome()

# 定义要测试的网页列表和对应的元素ID
pages = [
    {"url": "https://tw.yahoo.com", "element_id": "header-logo"},
    {"url": "https://data.gov.tw/", "element_id": "app"},
    {"url": "https://alvinbest.wordpress.com/2012/09/09/html%E7%9B%B8%E5%B0%8D%E8%B7%AF%E5%BE%91%E4%B9%8B%E9%80%A3%E7%B5%90/", "element_id": "wrapper"},
]

for page in pages:
    # 打开网页
    driver.get(page["url"])

    # 查找元素
    element = driver.find_element(By.ID, page["element_id"])

    # 确认元素是否存在
    if element is not None:
        print("元素存在")
    else:
        print("元素不存在")

    # 进行截图
    screenshot_filename = f"screenshot_{page['element_id']}.png"
    driver.save_screenshot(screenshot_filename)

# 关闭浏览器窗口
driver.quit()
