from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import xlsxwriter as xw
import urllib.request as req
from io import BytesIO
import urllib.request as req
from fake_useragent import UserAgent

chrome_options = Options()

browser = wd.Chrome('./0810_webdriver/chromedriver.exe', options=chrome_options)
workbook = xw.Workbook('./2조_고영주.xlsx')
worksheet = workbook.add_worksheet()
browser.implicitly_wait(3)
browser.set_window_size(800, 600)
browser.get('https://taling.me/')
element = browser.find_element_by_css_selector('fieldset > input.inp')
element.send_keys('기타')
element.submit()
time.sleep(2)


cur_page = 1
target_page = 6
row_num = 2

worksheet.write(f'A1', '강의명')
worksheet.write(f'B1', '튜터')
worksheet.write(f'C1', '비용')
worksheet.write(f'D1', '위치')
worksheet.write(f'E1', '강의 링크')
worksheet.write(f'F1', '이미지')


while cur_page <= target_page:
    bs = BeautifulSoup(browser.page_source, 'lxml')
    ua = UserAgent()
    headers = {
        'User-agent':ua.chrome
    } 
    class_list = bs.select('div.cont2 > div.cont2_class')

    print(f'****page : {cur_page}******')
    print()
    
    for li in class_list:
        img_url = li.select('a > div.img')[0]['style']        
        img_url = img_url.replace("background-image: url(", "http:")
        img_url = img_url.replace(");", "")    
        img = BytesIO(req.urlopen(req.Request(img_url, headers=headers)).read())
        x_scale = 0.2
        y_scale = 0.2
        title = li.select('a > div.title')[0].text.strip() 
        tutor = li.select('a > div.profile_box > div.name')[0].text.strip()
        price = li.select('div.price2 > span')[0].text.strip()
        location = li.select('a > div.info div.location')[0].text.strip()
        link = li.select('a')[0]['href']


        worksheet.write(f'A{row_num}', title)
        worksheet.write(f'B{row_num}', tutor)
        worksheet.write(f'C{row_num}', price)
        worksheet.write(f'D{row_num}', location)
        worksheet.write(f'E{row_num}', 'https://taling.me' + link )
        worksheet.insert_image(f'F{row_num}', img_url, {'image_data' : img, 'y_scale' : y_scale, 'x_scale' : x_scale, 'object_position' : 2})

        row_num += 1
    cur_page += 1

    if cur_page > target_page:
        print('크롤링 성공')
        break

    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,f'div.page > a:nth-child({cur_page})'))).click()
    
browser.quit()
workbook.close()