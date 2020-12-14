class OMG :
    def print(self) :  #빈자리에 self 를 넣어둔다.
        print("Oh my god")


mystock = OMG()
mystock.print()      # OMG.print(mystock) -> self 를 넣어두지않으면 argument가 자동으로 변경됨.
#클래스로부터 객체를 만든다음에 자동으로 객체가 정의된 함수의 () 안에 들어간다.
#따라서 self 를 넣어줘야 오류가 나지 않는다.