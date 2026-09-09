import requests

from config.api import BASE_URL, APPKEY, APPSECRET

ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6IjU5ZjI4OTVjLTZhZDYtNGE5ZC04YjZlLWI0ZmQxZTc2YTI5YyIsInByZHRfY2QiOiIiLCJpc3MiOiJ1bm9ndyIsImV4cCI6MTc4OTAwMTUzNSwiaWF0IjoxNzg4OTE1MTM1LCJqdGkiOiJQU3phdjhwQWxkS2RDTEJ0T0dYV0JSSXpDRnpNR3JkYzlVTlEifQ.z0FaWKXbEUY6u0zkpriuxRLRwL3taKkQV4T9eLDKRX2-EIeV4UlqrQnMXgywwIkBn7JL7hnrG0wHsBYGdYExWg', 'access_token_token_expired"

url = f"{BASE_URL}/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice"
headers = {
    "content-Type": "application/json; charset=utf-8",
    "authorization": f"Bearer {ACCESS_TOKEN}",
    "appkey": APPKEY,
    "appsecret": APPSECRET,
    "tr_id": "FHKST03010200",
    "custtype": "P"
}

params = {
    "FID_ETC_CLS_CODE": "",
    "FID_COND_MRKT_DIV_CODE": "J",
    "FID_INPUT_ISCD": "005930",
    "FID_INPUT_HOUR_1": "093000",
    "FID_PW_DATA_INCU_YN": "Y"
}

try:
    res = requests.get(url, headers=headers, params=params)
    data = res.json()
    print(data["output1"]["hts_kor_isnm"])  # HTS 한글 종목명
    for item in data["output2"]:
        print(f"시간 : {item['stck_bsop_date']} {item['stck_cntg_hour']} 가격 : {item['stck_prpr']}")
except Exception as e:
    print(type(e).__name__, e)  