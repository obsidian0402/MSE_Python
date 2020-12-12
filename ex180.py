low  = [100, 200, 400, 800, 1000] #저가, 고가 리스트 생성
high = [150, 300, 430, 880, 1000]
result = [] #빈 리스트 생성
for i in range(len(low)) :  #low 리스트의 길이만큼 반복
    result.append(high[i] - low[i]) # 고가와 저가의 차이를 result 리스트에 저장
print (result)