per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i)) #실행
    except: #예외가 발생했을때 수행할 코드
        print(0)
    else: #예외가 발생하지 않았을 때 수행할 코드.
        print("clean data")
    finally: #예외발생여부 상관없이 항상 수행할 코드.
        print("변환 완료")