#학번: _____________
#주제: 1개의 정수를 입력 받은 후 1부터 n까지의 홀수 합 구하기 

#입력문 수행: 정수 1개 입력 받기
n = int(input("정수 입력 ==>"))
sum=0

#반복문 수행하는 코드 추가
#반드시 for문과 continue 사용해서 수행할 것(while문 사용 시 감점) 
for i in range(1,n+1):
    if i%2==0: continue
    sum=sum+i
print("1부터 %d까지의 홀수 합은 %d입니다\n"% (n, sum))
#반드시 while문과 continue 사용해서 수행할 것(for문 사용 시 감점) 
i=0 #주어진 코드를 변경하지 말 것
sum=0
while i<n:
    i=i+1
    if i%2==0:  continue
    sum=sum+i
print("1부터 %d까지의 홀수 합은 %d입니다\n"% (n, sum))
#반드시 while문과 continue 사용해서 수행할 것(for문 사용 시 감점) 
i=1 #주어진 코드를 변경하지 말 것
sum=0
while i<=n:
    if i%2==0: i=i+1; continue
    sum=sum+i
    i=i+1
print("1부터 %d까지의 홀수 합은 %d입니다\n"% (n, sum))
    
# 결과화면
# 정수 입력 ==>10 (엔터)
# 1부터 10까지의 홀수 합은 25입니다
#
# 1부터 10까지의 홀수 합은 25입니다

# <Ctrl+F5>를 눌러서 코드 실행