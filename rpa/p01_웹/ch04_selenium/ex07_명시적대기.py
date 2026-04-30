# 명시적 대기(Explicit Waits)
'''
WebDriverWait()
http://localhost:63342/rpa/ch02_%EC%9B%B9%EC%8A%A4%ED%81%AC%EB%9E%98%ED%95%91/05_selenium%EC%8B%AC%ED%99%94/ex01_app.html?_ijt=5rs2ngl6hpm4jspm1mh0dcjn3k&_ij_reload=RELOAD_ON_SAVE
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("http://127.0.0.1:5500/rpa/ch02_%EC%9B%B9%EC%8A%A4%ED%81%AC%EB%9E%98%ED%95%91/05_selenium%EC%8B%AC%ED%99%94/ex01_app.html")
time.sleep(2)

try:
    try_it_button = browser.find_element(By.TAG_NAME, 'button')
    try_it_button.click()
    print("버튼 클릭 완료")

    hello_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[text()="Hello"]')))

    print("찾은 요소: ", hello_element.text)

except Exception as e:
    print("에러:",e)


time.sleep(10)
browser.quit()