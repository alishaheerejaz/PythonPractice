from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com")

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("alishaheerejaz")

password_box = browser.find_element_by_id("password")
password_box.send_keys("***********")
password_box.submit()

assert "alishaheerejaz" in browser.page_source

profile = browser.find_element_by_class_name("user-profile-link")
link_lable = profile.get_attribute("innerHTML")

assert "alishaheerejaz" in link_lable

browser.quit()
