# 이름,평점,리뷰수,주소,대표메뉴,대표메뉴가격,분류(카테고리),거리
# 위도,경도

import json
import time
from time import sleep
import pandas as pd

from selenium import webdriver  # 브라우저 자동 제어 모듈
from selenium.webdriver.common.by import By # 웹페이지의 요소들을 탐색하는 방법을 정의
from selenium.webdriver.common.keys import Keys # 키보드 키입력 관련
from selenium.webdriver.support import expected_conditions as EC  # 웹의 다양한 상태를 체크하는 모듈
from selenium.webdriver.support.ui import WebDriverWait # 웹의 요소나 상태가 될때까지 기다리는 기능
# 브라우저 세션을 생성할 때 원하는 기능을 정의할 수 있게 하는 기능
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities  
                                                                                

# --크롬창을 숨기고 실행-- driver에 options를 추가해주면 된다
# options = webdriver.ChromeOptions()
# options.add_argument('headless')

# 웹페이지가 완전히 로딩될때까지 기다리지 않고 준비되자마자 제어를 시작. 크롤링 속도가 향상됨
caps = DesiredCapabilities.CHROME # 크롬 브라우저의 기본 설정값을 가짐
caps["pageLoadStrategy"] = "none"

url = 'https://map.kakao.com/'
driver = webdriver.Chrome()  # 크롬 드라이버 경로
# driver = webdriver.Chrome('chromedriver.exe',chrome_options=options) # 크롬창 숨기기
driver.get(url)
key_word = '잠실새내 맛집'  # 검색어

# css 찾을때 까지 num초대기
def time_wait(num, code):
    try:
        wait = WebDriverWait(driver, num).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, code)))  # code요소가 웹페이지에 존재하는지 체크
    except:
        print(code, '태그를 찾지 못하였습니다.')
        driver.quit() # 오류가 발생하면 브라우저를 닫음
    return wait # 대기 조건이 만족될때까지 기다린 후, 해당 웹 요소를 가리킴

# 상세보기 페이지에서 메뉴 이름을 가져오는 함수
def get_menu_from_detail_page(detail_page_url):
    # 새 탭을 여는 자바스크립트 코드
    driver.execute_script("window.open('');")
    # 두번쨰 탭으로 전환(위에서 새로 연 탭)
    driver.switch_to.window(driver.window_handles[1])
    driver.get(detail_page_url) # 인자로 받은 URL을 새 탭에서 연다

    menu_text = ""
    price_text = ""
    
    # 새 탭에서 메뉴 이름, 가격 가져오기
    try:
        # menu_element = time_wait(1, "span.loss_word") # 이거는 연결 거부당함
        # <span class="loss_word">메밀정식(1인)</span>
        # span.loss_word라는 요소가 로드될 때까지 1초 기다림
        menu_element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.loss_word"))
        )
        menu_text = menu_element.text

        # price_element = time_wait(1, "em.price_menu") # 연결 거부
        # <em class="price_menu"><span class="screen_out">가격: </span>17,900</em>
        # em.price_menu라는 요소가 로드될 때까지 1초 기다림
        price_element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "em.price_menu"))
        )
        price_text = price_element.text.replace("가격: ", "")  # "가격: " 문자열을 제거

    except Exception as e:
        print("상세 페이지에서 메뉴 정보를 찾는 데 실패했습니다:", e)
        menu_text = ""

    # 현재 탭을 닫고 원래 탭으로 복귀
    driver.close()
    driver.switch_to.window(driver.window_handles[0]) # 원래 탭으로 전환
    return (menu_text, price_text)

# 음식점 정보 출력
def restaurant_list_print():

    sleep(0.2)

		# 장소 목록
    # "placelist"클래스 > "PlaceItem"클래스 > "clickArea"
    restaurant_list = driver.find_elements(By.CSS_SELECTOR, '.placelist > .PlaceItem')

    for index in range(len(restaurant_list)):
        # print(index)  # 현재 인덱스 출력

				# 음식점 이름
        # <a href="#none" data-id="name" class="link_name" title="살살녹소 본점">살살녹소 본점</a>
        names = driver.find_elements(By.CSS_SELECTOR, '.head_item > .tit_name > .link_name')

        # 평점
        # <em data-id="scoreNum" class="num" title="4.0점">4.0</em>
        scores = driver.find_elements(By.CSS_SELECTOR, '.rating > .score > .num')

        # 리뷰수
        # <a href="https://place.map.kakao.com/27291925#review" data-id="review" class="review" target="_blank">리뷰 <em data-id="numberofreview">76</em></a>
        review = driver.find_elements(By.CSS_SELECTOR, '.rating > .review')

        # <a href="https://place.map.kakao.com/629819421" 
        # data-id="moreview" class="moreview" target="_blank">상세보기</a>

        # 상세보기
        details = driver.find_elements(By.CSS_SELECTOR, 'a.moreview')
        details_value = details[index].get_attribute('href')

        # 상세 페이지로 이동하여 메뉴 이름, 가격 가져오는 함수 호출
        menu_name, menu_price = get_menu_from_detail_page(details_value)  

		    # 카테고리
        # <span data-id="subcategory" class="subcategory clickable">갈비</span>
        types = driver.find_elements(By.CSS_SELECTOR, '.head_item > .subcategory')

		    # 주소
        # <div data-id="wrapAddress" class="addr"> 어쩌구저쩌구 주소
        address = driver.find_elements(By.CSS_SELECTOR, '.addr')

        # css에서 문자만 뽑아와요
        restaurant_name = names[index].text
        # print(restaurant_name)

        restaurant_score = scores[index].text
        restaurant_score.strip()
        # print(restaurant_score)

        restaurant_review = (review[index].text).split()[1]
        restaurant_review = restaurant_review.replace(",", "")

        if int(restaurant_review) > 999:
            restaurant_review = '999+'
        # print(restaurant_review)

        restaurant_type = types[index].text
        # print(restaurant_type)

        restaurant_address = (address[index].text).split('\n')[0]
        # print(restaurant_address)

        restaurant_detail = details_value
        # print(restaurant_detail)

        # print("menu:", menu_name)

        menu_price = menu_price.replace(",", "")
        # print("price:", menu_price)

        # 평점이 4.0 이상이면 dict에 데이터 집어넣기
        # 거리, 위도, 경도는 일단 패스하고 대신 링크를 넣음
        if float(restaurant_score) >= 4.0:
          dict_temp = {
            '이름': restaurant_name,
            '평점': restaurant_score,
            '리뷰수': restaurant_review,
            '주소': restaurant_address,
            '대표메뉴': menu_name,
            '가격': menu_price,
            '분류': restaurant_type,
            '링크': restaurant_detail     
          }

          restaurant_dict['음식점정보'].append(dict_temp)
        print(f'{restaurant_name} ...완료')

# css를 찾을때 까지 10초 대기
time_wait(10, 'div.box_searchbar > input.query')

# 검색창 찾기
# <div class="box_searchbar">
search = driver.find_element(By.CSS_SELECTOR, 'div.box_searchbar > input.query')
search.send_keys(key_word)  # 검색어 입력
search.send_keys(Keys.ENTER)  # 엔터버튼 누르기

sleep(1)

# 장소 탭 클릭
# <ul id="info.main.options" class="sub">
# <li class="option1 option1-ACTIVE"><a href="#">장소</a></li>
# <a href="#">장소</a>
place_tab = driver.find_element(By.CSS_SELECTOR, '#info\.main\.options > li.option1 > a')
place_tab.send_keys(Keys.ENTER)

sleep(1)

# 음식점 리스트
restaurant_list = driver.find_elements(By.CSS_SELECTOR, '.placelist > .PlaceItem')

# dictionary 생성
restaurant_dict = {'음식점정보': []}
# 시작시간
start = time.time()
print('[크롤링 시작...]')

# 페이지 리스트만큼 크롤링하기
page = 1    # 현재 크롤링하는 페이지가 전체에서 몇번째 페이지인지
page2 = 0   # 1 ~ 5번째 중 몇번째인지
error_cnt = 0

while 1:  # while 1에서 변경

    # 페이지 넘어가며 출력
    try:
        page2 += 1
        print("**", page, "**")

				# 페이지 번호 클릭
        # //*[@id="info.search.page.no1"]
        driver.find_element(By.XPATH, f'//*[@id="info.search.page.no{page2}"]').send_keys(Keys.ENTER)

				# 음식점 리스트 크롤링
        restaurant_list_print()

				# 해당 페이지 음식점 리스트
        restaurant_list = driver.find_elements(By.CSS_SELECTOR, '.placelist > .PlaceItem')
				# 한 페이지에 장소 개수가 15개 미만이라면 해당 페이지는 마지막 페이지
        if len(restaurant_list) < 15:
            break
				# 다음 버튼을 누를 수 없다면 마지막 페이지
        # //*[@id="info.search.page.next"]
        if not driver.find_element(By.XPATH, '//*[@id="info.search.page.next"]').is_enabled():
            break

        # 다섯번째 페이지까지 왔다면 다음 버튼을 누르고 page2 = 0으로 초기화
        if page2 % 5 == 0:
            driver.find_element(By.XPATH, '//*[@id="info.search.page.next"]').send_keys(Keys.ENTER)
            page2 = 0

        page += 1

    except Exception as e:
        error_cnt += 1
        print(e)
        print('ERROR!' * 3)

        if error_cnt > 5:
            break

print('[데이터 수집 완료]\n소요 시간 :', time.time() - start)
driver.quit()  # 작업이 끝나면 창을 닫는다.

# json 파일로 저장
# with open('./restaurant_list.json', 'w', encoding='utf-8') as f:
#     json.dump(restaurant_dict, f, indent=4, ensure_ascii=False)

# # csv 파일로 저장
df = pd.DataFrame(restaurant_dict['음식점정보'])
df.to_csv('./잠실새내_맛집.csv', index=False, encoding='utf-8-sig')
