#학번: 60241234  주제: 사칙연산

# 변수 선언 및 초기화
num1 = 20
num2 = 3

# 연산 식 수행 (사칙 연산)
result1 = num1 + num2
result2 = num1 - num2
result3 = num1 * num2
result4 = round(num1 / num2) # 버림의 정수 해결: round()

# 출력문 수행
print(num1, " + ", num2, " = ", result1)
print(f"{num1} - {num2} = {result2}")
print("{} * {} = {}".format(num1, num2, result3))
print("%d / %d = %d" % (num1, num2, result4))





### 결과화면
# 20 + 3 = 23
# 20 - 3 = 17
# 20 * 3 = 60
# 20 / 3 = 7


# <Ctrl+F5>를 눌러서 코드 실행


