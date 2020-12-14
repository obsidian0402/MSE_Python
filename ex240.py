def 함수0(num) :
    return num * 2  #3. 함수0을 호출해 num은 14*2

def 함수1(num) :
    return 함수0(num + 2) #2. 함수1을 호출함으로써, 함수 0호출(12+2)    #4. 함수1로 리턴.

def 함수2(num) :      
    num = num + 10   # 1. 2+10 하고 함수 1호출     #5. 함수2로 리턴.
    return 함수1(num)

c = 함수2(2)   #6. c로 리턴.
print(c)   #7. c출력