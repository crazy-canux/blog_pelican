Title: TPL_Selenium
Date: 2017-03-27 21:18:33
Tags: Selenium



# Selenium

参考DevOps/selenium进行安装配置．

selenium只有两个包webdriver和common.

# selenium.webdriver

    from selenium import webdriver

    # 返回WebDriver类型的对象．
    driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    driver = webdriver.Edge()
    driver = webdriver.Ie()
    driver = webdriver.Opera()
    driver = webdriver.Safari()

selenium.webdriver.[browser].webdriver.WebDriver
是
selenium.webdriver.remote.webdriver.WebDriver
的子类.

    # selenium.webdriver.firefox.webdriver.WebDriver
    driver.implicitly_wait(self, time_to_wait) # 隐式等待一个元素被找到．
    driver.get("http://www.google.com")
    ...
    driver.maximize_window() # 最大化窗口
    driver.get_screenshot_as_file("filename")
    driver.current_window_handle # 当前窗口的句柄
    driver.title
    driver.execute_script(self, script, *args)
    ...
    driver.close() # 关闭一个标签
    driver.quit() # 退出整个浏览器

定位元素的八个方法

    elem = driver.find_element_by_id()
    elem = driver.find_element_by_name()
    elem = driver.find_element_by_class_name()
    elem = driver.find_element_by_tag_name
    elem = driver.find_element_by_link_text
    elem = driver.find_element_by_partial_link_text
    elem = driver.find_element_by_xpath()
    elem = driver.find_element_by_css_selector()

selenium.webdriver.[browser].webelement.[Browser]Element
是
selenium.webdriver.remote.webelement.WebElement
的子类．

    # selenium.webdriver.firefox.webelement.FirefoxWebElement

    elem.find_anonymous_element_by_attribute(self, name, value)
    elem.anonymous_children
    elem.click() # 点击按钮．
    elem.clear()
    elem.screenshot(self, filename)
    elem.send_keys(self, *value) # 给文本框输入内容，比如用户名密码，搜索框等．
    elem.submit(self)
    elem.value_of_css_property(self, property_name)

## selenium.webdriver.remote

    from selenium.webdriver.remote.webelement import WebElement

    from selenium.webdriver.remote.webdriver import WebDriver

## selenium.webdriver.support

    from selenium.webdriver.support.select import Select

    from selenium.webdriver.support.ui import WebDriverWait
    # 用于显示等待, 注意method的参数是driver.
    WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
    WebDriverWait.until(self, method, message='') # 调用method(driver)直到返回True.失败返回message.
    WebDriverWait.until_not(self, method, message='')

## selenium.webdriver.common

    from selenium.webdriver.common.keys import Keys

    from selenium.webdriver.common.action_chains import ActionChains

    from selenium.webdriver.common.by import By

***

# selenium.common

common.exception包括了所有的异常．

    from selenium.common.exceptions import TimeoutException # 等待超时
    from selenium.common.exceptions import NoSuchElementException

***

# example

    try:
        wait = WebDriverWait(driver, 10, 1.0)
        wait.until(lambda s: s.execute_script(
            'return document.readyState=="complete";'),
            'Fail to wait page full loaded.')
    except TimeoutException as e:
        raise e
    finally:
        driver.quit()
