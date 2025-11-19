# 함수 사용
# def funtion_name(param_first,...) :
    #실행할 코드
    #return reture_value

# kor = 60
# eng = 70
# math = 80

# sum = kor + eng

# def get_sum(korean, english, mathmatics=0) :
#     summation = korean + english + mathmatics
#     return summation

# sum = get_sum(kor, eng, math)
# print(f"총점 : {sum}")

# sum = get_sum(kor, eng)
# print(f"총점 : {sum}")

kor_score = [90, 80, 70, 60, 50]
eng_score = [85, 75, 65, 55, 45]
math_score = [88, 78, 68, 58, 48]

lenth = len(kor_score)
len_list = range(lenth)

# range(len(kor_score))
# pass

# for i in range(len(kor_score))
#     kor = kor_scores[i]
#     eng = eng_scores[i]
#     math = math_scores[i]
#     sum = get_sum(kor, eng, math)
#     print(f"{i+1}번 학생 총점 : {sum}")

def get_for_sum(korean_scores, english_scores, mathmatics_scores)
    
for i in range(len(kor_scores)) :
    kor = korean_scores[i]
    eng = english_scores[i]
    math = mathmatics_scores[i]
    sum = get_sum(kor, eng, math)
    print(f"{i+1}번 학생 총점 : {sum}")

    return 0

get_for_sum(kor_score, eng_score, math_score)