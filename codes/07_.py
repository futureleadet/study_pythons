# 중급 난이도 문제 1 — 문자열과 f-string 활용
# second 문자열에 "Python"이 포함되어 있는지 확인하고,
#  "Welcome!"과 합쳐서 출력하는 코드를 작성하시오.

fourth = "Welcome! Python is fun"
second = "Python"

if second in fourth :
    print(f"Welcome! + {second}")