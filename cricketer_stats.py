from selenium import webdriver

cricketers = ["Sachin Tendulkar", "Virender Sehwag",
              "MS Dhoni", "Bhuvneshwar Kumar", "Jaspreet Bumrah"]

browser = webdriver.Chrome(
    "E:\Tutorials\Python\web-automation\chromedriver.exe")

browser.implicitly_wait(10)
browser.maximize_window()

for cricketer in cricketers:
    browser.get("https://google.com")

    search_bar = browser.find_element_by_name("q")
    search_bar.send_keys(cricketer+" career stats")

    search_btn = browser.find_element_by_name("btnK")
    search_btn.click()

    browser.execute_script("window.scrollTo(0, 150)")
    browser.save_screenshot(cricketer+".png")

browser.close()
