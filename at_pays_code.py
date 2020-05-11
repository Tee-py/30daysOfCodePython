from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("http://atpays.com/")


elem = driver.find_elements_by_partial_link_text('')
print(elem[:4])
for elements in elem[:4]:
    try:
        elements.click()
    except:
        print('faikled')
        break