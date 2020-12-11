list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in list: #리스트의 객체마다 반복
    if i.endswith(('.h','.c')):  #리스트의 객체(i)중 끝에 .h, .c 가 있다면..
        print(i) #i를 출력하여라