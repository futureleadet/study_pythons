## 문제:
```
두 개의 숫자 리스트를 이용해 사칙연산(+, -, , /)을 수행하는 함수를 구현하시오.*
조건
테스트 데이터는 리스트(list) 로만 제공


테스트 데이터 개수는 10개


변수명은 소문자 + _ 조합


함수는 두 숫자를 입력받아 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 모두 반환


0으로 나누는 경우는 "division_error" 반환



## 문제 코드 골격
학생이 채워 넣도록 비워둔 버전입니다.
def calculate_all(num1, num2):
    # 여기에 사칙연산 구현
    # return (덧셈, 뺄셈, 곱셈, 나눗셈)
    pass


# 테스트 리스트 (10개)
test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]

# 테스트 실행
for i in range(10):
    a = test_a[i]
    b = test_b[i]
    result = calculate_all(a, b)
    print(f"{a}, {b} => {result}")
```

## JSON 프롬프트
```
{
  "prompt_title": "두 숫자 리스트를 이용한 사칙연산 함수 구현",
  "problem_description": "두 개의 숫자 리스트를 이용해 사칙연산(+, -, *, /)을 수행하는 함수 `calculate_all(num1, num2)`를 구현합니다. 함수는 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 모두 반환해야 합니다. 나눗셈 시 0으로 나누는 경우 'division_error'를 반환해야 합니다.",
  "function_name": "calculate_all",
  "parameters": [
    "num1",
    "num2"
  ],
  "implementation_language": "Python",
  "required_logic": [
    "덧셈 (num1 + num2)",
    "뺄셈 (num1 - num2)",
    "곱셈 (num1 * num2)",
    "나눗셈 (num1 / num2) 또는 0으로 나눌 경우 'division_error' 반환"
  ],

  "code_solution": "def calculate_all(num1, num2):\n    
  
  # 덧셈\n    add_result = num1 + num2\n    
  # 뺄셈\n    sub_result = num1 - num2\n    
  # 곱셈\n    mul_result = num1 * num2\n    
  \n    
  # 나눗셈 (0으로 나누는 경우 처리)\n    
  if num2 == 0:\n
          div_result = \"division_error\"\n    else:\n
        div_result = num1 / num2\n
                          \n
        # 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 튜플로 반환\n    return (add_result, sub_result, mul_result, div_result)\n\n
                              
        # 테스트 리스트 (10개)\n
        test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]\n
        test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]\n\n
                              
        # 테스트 실행\n
        print(\"num1, num2 => (덧셈, 뺄셈, 곱셈, 나눗셈)\")\n
        print(\"-------------------------------------------\")\n
        for i in range(10):\n    
        a = test_a[i]\n    
        b = test_b[i]\n    
        result = calculate_all(a, b)\n    
        print(f\"{a}, {b} => {result}\")\n\n
                              
        # 예상 출력 예시: \n
        # 7, 0 => (7, 7, 0, 'division_error')\n
        # 10, 5 => (15, 5, 50, 2.0)"
}