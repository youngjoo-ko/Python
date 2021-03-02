from selenium import webdriver as wd


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

import xlsxwriter as xw
import urllib.request as req

chrome_options = Options()

chrome_options.add_argument('--headless')

browser = wd.Chrome('./0810_webdriver/chromedriver.exe')

# 엑셀 처리하기 위한 workbook 생성
workbook = xw.Workbook('./crawl_result.xlsx')

# 워크시트 생성
worksheet = workbook.add_worksheet()

browser.implicitly_wait(5)

browser.set_window_size(1280, 760)

browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')


WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()



WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="selectMaker_simple_priceCompare_A"]/li[12]/label'))).click()


time.sleep(2)

# 현재 페이지
cur_page = 1

# 크롤링할 페이지 수
target_page = 3

# 엑셀의 행번호
row_num = 1

while cur_page <= target_page:
    

    bs = BeautifulSoup(browser.page_source, 'lxml')


    prod_list = bs.select('div.main_prodlist.main_prodlist_list > ul > li')

    # 페이지 번호 출력
    print(f'****page : {cur_page}******')
    print()
    
    # 원하는 정보 추출(계속 추출)
    for li in prod_list:
        if not li.find('div',class_='ad_caster'):
            
            # 상품명, 가격 엑셀에 저장
            prod_name = li.select('p.prod_name > a')[0].text.strip()
            prod_price = li.select('p.price_sect > a')[0].text.strip()

            # 이미지 가져오려면 url 필요
#             img_data = li.select('a.thumb_link > img')[0].get('data-original')
#             img_src = li.select('a.thumb_link > img')[0]['src']
#             print(img_data if img_data else img_src)

            # 엑셀 저장
            worksheet.write(f'A{row_num}',prod_name)
            worksheet.write(f'B{row_num}',prod_price)
            
            row_num += 1
            
        print()
    print()
    
    cur_page += 1

    if cur_page > target_page:
        print('크롤링 성공!!')
        break
        
    # 페이지 클릭(공부차원으로 By.CSS_SELECTOR로 변경)
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,f'div.number_wrap > a:nth-child({cur_page})'))).click()
    
    # 클릭하자마자 for문이 다시 돌아버리니까 
    # 2초간 대기
    time.sleep(2)
    
    # number_wrap 클래스명을 가진 div 태그 안에 a 태그 7개
    # 총 페이지가 7페이지까지 있어서 a태그도 7개까지 있는데
    # 그 중에 2랑 3페이지 가져올 때, nth-child(2), nth-child(3) 
    # 이런식으로 가져오면 될 듯. nth-child(cur_page)
    
    
browser.quit()

# close()를 해줘야지만 생성된다.
workbook.close()
