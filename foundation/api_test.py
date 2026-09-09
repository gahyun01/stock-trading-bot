"""
 리퀘스트 보내기
"""
import requests

url = "https://learn.codeit.kr/api/avatars"
res = requests.get(url)

try:
    data = res.json()
    print(data)
except Exception as e:
    print(e)


"""
 쿼리 파라미터 보내기
"""

url = "https://learn.codeit.kr/api/avatars"
params = {"limit": 5, "offset": 10}

try:
    res = requests.get(url, params=params)
    data = res.json()
    print(data)

except Exception as e:
    print(e)


"""
 POST 리퀘스트로 바디 보내기
"""
url = "https://learn.codeit.kr/api/avatars"
header = {"Content-Type": "application/json"}
body = {"hairType": "short2", "hairColor": "brown", "skin": "tone200", "clothes": "hoodie", "accesories": "earbuds"}

try:
    res = requests.post(url, headers=header, json=body)
    data = res.json()
    print(data)
except Exception as e:
    print(e)


"""
 f-string으로 리퀘스트 보내기
"""

avatar_id = 10
url = f"https://learn.codeit.kr/api/avatars/{avatar_id}"

try:
    res = requests.get(url)
    data = res.json()
    print(data)
except Exception as e:
    print(e)

# API : Application Programming Interface ( 애플리케이션 프로그래밍 인터페이스 )