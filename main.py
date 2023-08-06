from selenium import webdriver
import time

url = "http://example.com/"
driver = webdriver.Chrome()
driver.get(url)
response = driver.page_source

with open("file.txt", "w", encoding="utf-8") as output:
    print(response, file=output)

time.sleep(10)
driver.quit()