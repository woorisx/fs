# pip install requests -->설치
# pip uninstall requests --> 지우기

import requests

# 정상페이지 -> 페이지 있음
url_success = "https://www.python.org"
# 정상이 아닌 페이지 -> 페이지 없음
url_fail = "https://www.python.org/this-page-does-not-exist"

urls_to_check = [url_success, url_fail]

for url in urls_to_check:
    try: 
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("페이지 로딩 에러:", e)
    else:
        print("페이지 로딩 성공:", response.status_code)