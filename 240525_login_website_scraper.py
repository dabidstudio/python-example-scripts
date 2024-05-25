from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

# 설정
username = 'standard_user'
password = 'secret_sauce'
login_url = 'https://www.saucedemo.com/'  # Swag Labs의 로그인 URL로 변경 필요

# 웹 드라이버 설정 및 페이지 열기
driver = webdriver.Chrome()
driver.get(login_url)

# 페이지 로드 대기
time.sleep(2)

# 사용자 이름 입력
username_input = driver.find_element(By.ID, 'user-name')
username_input.send_keys(username)

# 비밀번호 입력
password_input = driver.find_element(By.ID, 'password')
password_input.send_keys(password)

# 로그인 버튼 클릭
login_button = driver.find_element(By.ID, 'login-button')
login_button.click()

# 페이지 로드 대기
time.sleep(2)

# 데이터 다운로드 로직 추가 (예: 특정 페이지에서 데이터를 추출하거나 파일을 다운로드)
# 예: 제품 페이지로 이동
driver.get('https://www.saucedemo.com/inventory.html')
time.sleep(2)

# 제품 정보 추출
products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
product_data = []

for product in products:
    name = product.find_element(By.CLASS_NAME, 'inventory_item_name').text
    description = product.find_element(By.CLASS_NAME, 'inventory_item_desc').text
    price = product.find_element(By.CLASS_NAME, 'inventory_item_price').text
    product_data.append({'Name': name, 'Description': description, 'Price': price})

# 드라이버 종료
driver.quit()

# 데이터프레임 생성 및 엑셀 파일로 저장
df = pd.DataFrame(product_data)
df.to_excel('product_data.xlsx', index=False)

print('제품 정보를 product_data.xlsx 파일로 저장했습니다.')