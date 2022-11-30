'''
    파이썬의 모든것이 객체(object)로 관리

    객체(object) -> 클래스(class)
        ==> class 클래스명:
                변수 ...
                메서드 ...
'''

'''
    1. __builtins__ 객체 : 도트(.) 없이도 메서드 사용 가능 # 중요
                        ex) print(), int(), str() ...
    
    2. 나머지 객체 : 도트가 있어야 사용 가능
                    ex) 문자열.메서드(), 리스트.메서드()
'''
# 함수확인 : print(dir(__builtins__)), print(dir(str)) ... 