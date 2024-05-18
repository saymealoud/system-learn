import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

test_driver = webdriver.Chrome()
test_driver.maximize_window()
test_driver.get("https://www.baidu.com")

# 使用 By 类来指定通过链接文本定位
above = test_driver.find_element(By.ID, "s-usersetting-top")

# 使用 ActionChains 完成鼠标悬停操作
ActionChains(test_driver).move_to_element(above).perform()
time.sleep(5)
test_driver.quit()
