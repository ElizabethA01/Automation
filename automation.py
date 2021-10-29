from selenium import webdriver

chrome_browser = webdriver.Chrome(executable_path='.\chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy' in chrome_browser.title #returns true if it's in the title. If not, it returns assertion error
show_message_button = chrome_browser.find_element_by_class_name ('btn btn-default')
user_button2 = chrome_browser.find_element_by_css_selector ('#get-input > .btn')
print(user_button2)
# print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOOL')

show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')

assert 'I AM EXTRA COOOL' in output_message.text

chrome_browser.quit()