from selenium import webdriver as wd

# 웹드라이버 설정(크롬, 익스플로러, 파이어폭스 등)
browser = wd.Chrome('./webdriver/chromedriver.exe')

# # 브라우저 내부 대기 설정(데이터를 불러왔을 때 화면에 펼쳐지는 것을 랜더링이라고 함
# # 랜더링이 완료되지 않았을 때 클릭명령을 내리면 오류가 나기 때문에 최소 3초간)
browser.implicitly_wait(3)

# # 속성 확인
print(dir(browser))

# # 브라우저 사이즈 지정 : maximize_window(), minimize_window()
browser.set_window_size(800,600)

# # 페이지 이동
browser.get('https://www.daum.net')

# # 페이지 내용
print(f'page contents : {browser.page_source}')

# # 세션의 id값 가져오기
print(f'Session ID: {browser.session_id}')

# 쿠키 정보 확인
print(f'Cookies: {browser.get_cookies()}')

# 타이틀 출력
print(f'Title: {browser.title}')

# url 출력
print(f'Url: {browser.current_url}')

# 검색어 입력창 선택
element = browser.find_element_by_css_selector('div.inner_search > input.tf_keyword')

# 검색어 입력
element.send_keys('손흥민')

# 검색어 서버에 전송(submit)
element.submit()

# 스크린샷 저장1
browser.save_screenshot('./website_capture1.jpg')
browser.get_screenshot_as_file('./website_capture2.jpg')

# 브라우저 종료
browser.quit()
