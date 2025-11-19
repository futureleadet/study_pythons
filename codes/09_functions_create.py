# 문제 1
# 섭씨 온도 3개를 받아 평균을 반환하는 함수 avg_celsius(t1, t2, t3) 를 작성하시오


# test = [
#    (20, 30, 40),
#     (70, 80, 90),
#     (30, 40, 50) 
# ]


# def avg_celsius(t1, t2, t3) :
#     avg = (t1 + t2 + t3) / 3
#     return avg

# for t1, t2, t3 in test : 
#     result = avg_celsius(t1, t2, t3)
#     print(f"({t1}, {t2}, {t3}) 평균온도 : {result}도")
#     pass

# 문제 2
# 이름과 좋아하는 언어 2개를 받아 아래 형식으로 출력하는 함수를 작성하시오.
# 홍길동님의 선호 언어는 Python, Java 입니다.

# def prefer_lang(t1, t2, t3) :
#     print(f"{t1}님의 선호 언어는 {t2}, {t3}입니다.")

# test = [
#    ("hans", "eng", "japan"),
#     ("you1", "japan", "china"),
#     ("you2", "eng", "france") 
# ]

# for t1, t2, t3 in test :
#     solve = prefer_lang(t1, t2, t3)
#     print(solve)

# 문제 3
# 점수 리스트를 받아 60점 이상 점수만 누적한 합계를 반환하는 함수를 작성하시오.

# def scored_60(scores) :
#     total = 0
#     for s in scores :
#         if s >= 60 :
#         total = total + s
#     return total

# test_list = [
#  (90, 80, 70, 60, 50),
#  (85, 75, 65, 55, 45),
#  (88, 78, 68, 58, 48)
# ]

# for scores in test_list :
#     result = scored_60(scores)
#     print(f"입력{scores} 중 60점 이상 총합은 : {result}입니다.")

# 문제 4
# 문자열 두 개를 받아 하나의 문장으로 이어 붙이는 함수 combine(str1, str2) 작성.

# def combine(str1, str2) :
#     print(f"{str1}+{str2}")

# test_list = [
#     ("hi", "my name"),
#     ("good", "morning1")
# ]

# for str1, str2 in test_list : 
#     print(combine(str1,str2))

###########################실패#######################################
# 문제 5
# 온도 리스트를 받아 모두 섭씨로 변환해 새로운 리스트로 반환하는 함수 작성.

# def to_celsius(temps) :
#     celsius_list = []
#     for temp in temps :
#     celsius = (temp -32) * 5 / 9
#     celsius_list.append(celsius)
#     return celsius_list

# test_list = [
#  (90, 80, 70, 60, 50),
#  (85, 75, 65, 55, 45),
#  (88, 78, 68, 58, 48)
# ]

# for temps in test_list
# result=to_celsius(temps)
# print(f"화씨 {temps} -> 섭씨 {result}")
###################실패#########################