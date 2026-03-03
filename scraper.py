import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

if len(sys.argv) < 2:
    print("Enter a URL")
    sys.exit()

url = sys.argv[1]

if "http" not in url:
    url = "https://" + url

driver = webdriver.Chrome()
driver.get(url)

print("Title:")
print(driver.title)

print("\n[Body Text:]")
body = driver.find_element(By.TAG_NAME, "body")
print(body.text)

print("\nLinks:")
links = driver.find_elements(By.TAG_NAME, "a")

for l in links:
    href = l.get_attribute("href")
    if href:
        print(href)

driver.quit()

