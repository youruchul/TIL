# print에서 r활용
print(r'C:\work') # print에 r을 붙이면 escape문자 무시 가능 

# 문자열은 bytes의 형태와 str의 형태가 있다.
'''
    1. bytes
        - 네트워크에서 이용되는 문자열
        - bytes 타입
        - 표현 : b'hello'
        * 웹크롤링 - 기본적으로 bytes 타입으로 문자열 받음

    2. str
        - 일반적인 문자열
        - 유니코드 타입(전 셰계의 모든 언어표현,unicode)
        - 표현 : 'hello'

    3. str -> bytes : 암호화(encode)
       bytes -> str : 복호화(decode)
'''

# 3. 예제
s = "hello한글"

# str ==> bytes 로
s_bytes = s.encode('utf-8')
print(s, s_bytes) # hello한글 b'hello\xed\x95\x9c\xea\xb8\x80'

# bytes ==> str 로
s_str = s_bytes.decode('utf-8')
print(s_str) # hello한글