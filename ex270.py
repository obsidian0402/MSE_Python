class Stock:                      #클래스 설정
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend
        
#class를 이용하여 원하는값 출력
종목 = []

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83) #표의 데이터값 대입
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)  #종목 리스트에 각 항목들 추가.
종목.append(현대차)
종목.append(LG전자)

for i in 종목: #i=삼성, 현대차, lg전자
    print(i.code, i.per)        # i-> Stock 클래스의 객체를 바인딩하기 때문임.
    #i에 포함된 code, per 에 접근해서 출력