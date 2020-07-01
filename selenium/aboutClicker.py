from selenium import webdriver


browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
browser.get('http://facebook.com')

elm = browser.find_element_by_link_text('About')
browser.implicitly_wait(5)

elm.click()


#  download chrome driver and place in the usr bin dir https://sites.google.com/a/chromium.org/chromedriver/downloads
# may not need executable path on windows or mac.