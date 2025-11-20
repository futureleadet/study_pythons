def calculate_all(num1, num2):
    # 덧셈 (num1 + num2)
    add_result = num1 + num2
    # 뺄셈 (num1 - num2)
    sub_result = num1 - num2
    # 곱셈 (num1 * num2)
    mul_result = num1 * num2
    
    # 나눗셈 (0으로 나누는 경우 처리)
    if num2 == 0:
        div_result = "division_error"
    else:
        # 일반적인 나눗셈 (num1 / num2)
        div_result = num1 / num2
    
    # 모든 결과를 튜플로 묶어 반환
    return (add_result, sub_result, mul_result, div_result)

# 테스트 리스트 (10개)
test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]

for i in range(10):
    a = test_a[i]
    b = test_b[i]
    result = calculate_all(a, b)
    print(f"{a}, {b} => {result}")

