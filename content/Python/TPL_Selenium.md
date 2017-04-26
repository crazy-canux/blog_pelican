Title: TPL_Selenium
Date: 2017-03-27 21:18:33
Tags: Selenium



# Selenium

参考DevOps/selenium进行安装配置．

selenium只有两个包webdriver和common.

# selenium.webdriver

    from selenium import webdriver

    # 返回WebDriver类型的对象．
    # class WebDriver(selenium.webdriver.remote.webdriver.WebDriver)
    driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    driver = webdriver.Edge()
    driver = webdriver.Ie()
    driver = webdriver.Opera()
    driver = webdriver.Safari()

    # WebDriver:
    driver.get("http://www.google.com")
    driver.get_screenshot_as_file("filename")
    driver.close() # 关闭一个标签
    driver.quit() # 退出整个浏览器
    driver.title

    # 定位元素的八个方法
    # 返回FirefoxWebElement类型的对象．
    # class FirefoxWebElement(selenium.webdriver.remote.webelement.WebElement)
    elem = driver.find_element_by_id()
    elem = driver.find_element_by_name()
    elem = driver.find_element_by_class_name()
    elem = driver.find_element_by_tag_name
    elem = driver.find_element_by_link_text
    elem = driver.find_element_by_partial_link_text
    elem = driver.find_element_by_xpath()
    elem = driver.find_element_by_css_selector()

    # FirefoxWebElement:
    elem.find_anonymous_element_by_attribute(self, name, value)
    elem.anonymous_children
    elem.click()
    elem.clear()
    elem.screenshot(self, filename)
    elem.send_keys(self, *value)
    elem.submit(self)
    elem.value_of_css_property(self, property_name)

    # selenium.webdriver.remote
    from selenium.webdriver.remote.webelement import WebElement

    # selenium.webdriver.common
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains

    # selenium.webdriver.support
    from selenium.webdriver.support.select import Select
    from selenium.webdriver.support.ui import WebDriverWait

# selenium.common

common.exception包括了所有的异常．

    from selenium.common.exceptions import TimeoutException
    from selenium.common.exceptions import NoSuchElementException
    ...

