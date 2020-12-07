date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
#zip 으로 data와 close_price를 서로 매칭하여 각각의 새로운 리스트로 만든다.
#zip함수는 '동일한' 개수로 이루어진 자료형을 묶어주는 역할을 한다.
#dict 은 zip 함수로 만들어진 각각의 리스트를 이용해 딕셔너리를 생성한다. 
print(close_table)