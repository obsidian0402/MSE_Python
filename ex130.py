import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# 모듈 requests를 불러오고 btc라 지정한다.

high = float(btc['max_price']) #btc에서 high, low, open을 불러온다.
low = float(btc['max_price'])
open = float(btc['opening_price'])
diff = high - low #불러온 high와 low 로 변동폭 diff 를 구한다.



if (open+diff) > high: #시가+변동폭 > 최고가  이면
    print("상승장") #상승장
else:
    print("하락장")#아니라면 하락장