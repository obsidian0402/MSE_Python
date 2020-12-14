def print_max(a, b, c) : #함수정의
    max = 0 #초기값 지정
    if a > max: #조건1
        max = a
    if b > max : #조건2
        max = b
    if c > max : #조건3
        max = c
#max에 대해 변수하나하나 검증하여 이전의것과 크면 max 변수변경, 아니라면 보존.
    print(max)
print_max(27,5,28)