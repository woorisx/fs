# 웹 페이지의 특정 요소 찾기
'''
find_element(): 하나 찾기, 없으면 에러
find_elements(): 여러 개 찾기, 없으면 빈 리스트

검색 기준
    id -> By.ID
    class -> By.CLASS_NAME
    tag -> By.TAG_NAME
    name -> By.NAME
    css -> By.CSS_SELECTOR
    By.LINK_TEXT

    예) ele = browser.find_element(By.ID, 'id값')
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.naver.com")

time.sleep(2)

try:
    search_box = browser.find_element(By.ID, 'query') #find_element는 예외발생가능
    print(search_box.tag_name) #input tab


except Exception as e:
    print("에러: ", e)

menu_links = browser.find_elements(By.CLASS_NAME, 'link_service')

print(len(menu_links))

for link in menu_links:
    if link.text.strip():
        print("링크 :", link.text.strip())

time.sleep(10)
browser.quit()