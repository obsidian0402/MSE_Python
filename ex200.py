ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
profit = 0 #초기값(수익0)
for row in ohlc[1:]: #0번째는 설명을 위한 리스트로 건너뜀.
    profit += (row[0] - row[3]) 
    #수행할때마다 (시가-종가) 결과값을 profit에 더하는걸  반복(수익 누적->총수익금)
    #1번째 : 100-100=0  2번째 : 200-190 3번째: 300-310
print(profit)   