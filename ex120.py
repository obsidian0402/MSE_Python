fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"} #딕셔너리 정의
user = input("좋아하는 과일은?") #input : 사용자로부터 문자를 입력받을수 있음
if user in fruit.values(): #입력받은 문자가 fruit 딕셔너리내에 키로 존재한다면 정답
    print("정답입니다.") 
else:               #아니라면, 오답
    print("오답입니다.")