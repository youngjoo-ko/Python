from selenium import webdriver as wd


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

chrome_options = Options()

chrome_options.add_argument('--headless')

browser = wd.Chrome('./0810_webdriver/chromedriver.exe')


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

while cur_page <= target_page:
    

    bs = BeautifulSoup(browser.page_source, 'lxml')


    prod_list = bs.select('div.main_prodlist.main_prodlist_list > ul > li')

    # 페이지 번호 출력
    print(f'****page : {cur_page}******')
    print()
    
    # 원하는 정보 추출(계속 추출)
    for li in prod_list:
        if not li.find('div', class_='ad_caster'):
            print(li.select('p.prod_name > a')[0].text.strip())
            print(li.select('p.price_sect > a')[0].text.strip())
            img_data = li.select('a.thumb_link > img')[0].get('data-original')
            img_src = li.select('a.thumb_link > img')[0]['src']
            print(img_data if img_data else img_src)
        print()
    print()

    cur_page += 1

    if cur_page > target_page:
        print('크롤링 성공')
        break

    # 페이지 클릭
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CSS_CELECTOR,f'div.numver_wrap > a:nth-child({cur_page})'))).click()

    # 2초간 대기
    time.sleep(2)

browser.quit()
