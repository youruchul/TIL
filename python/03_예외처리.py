'''
    예외(exception)란?
        - 프로그램 실행중에 발생되는 오류를 의미.(일반적으로 에러라고 부름)
        - 가장 큰 문제는 비정상종료 됨.

    예외 처리란?
        - 예외가 발생해도 끝까지 실행하도록 처리(정상종료 되도록)
        - 예외 발생 코드를 수정하는 것은 불가능, 정상종료 + 예외정보를 알려주는 역할 (매우 중요)
'''
'''
    예외처리 방법
        1. 예외클래스 이용
            - help(__builtins__)를 통해 예외클래스 종류 확인 가능

        2. try - except문
'''

# try 문
try:
    pass # 실행하고자 하는 문장
except Exception as e:
    pass # 예외발생시 처리하는 문장

# 다중 except문
try:
    pass
except ZeroDivisionError as e:
    pass # ZeroDivisionError 일때 처리
except ValueError as e:
    pass # ValueError 일때 처리
except Exception as e:
    pass # 관례적으로 마지막에 Exception을 넣어주어 모든 예외를 잡아준다.

# finally문
'''
    finally문
        - 예외의 발생여부와 관계없이 무조건 실행되는 문장
        - 반드시 실행되어야 하는 문장을 알려주는 역할
'''
try:
    pass
# 이 안에 except문이 들어와도 상관없다.
finally:
    pass # 반드시 실행되어야 할 문장 ex) 파일.close()
