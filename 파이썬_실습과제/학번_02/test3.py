#학번: _____________  주제: 문자열
#결과화면과 같이 나오도록 해당 소스 코드를 완성하시오.
#참조할 코드: count()  find()  len()  print()  replace()

mind="I am sad" 
# 1. mind 문자열 중에서 'a'의 갯수를 반환 후 해당 결과를 출력하시오. 
#출력결과=> I am sad 중에서 a 개수 = 2
print("%s 중에서 %c 개수 = %d"%(mind,'a',mind.count('a')))

# 2. mind 문자열에서 "sad"를 "happy"로 변경 후 해당 결과를 출력하시오.
#출력결과=> I am happy
mind=mind.replace("sad","happy")
print(mind)

# 3. 변경된 mind 문자열에서 'h'의 위치를 출력하시오.
# 반드시 서식문자 %기호(%d %f %c %s등)와 제어문자(\")를 사용할 것
#출력결과=> I am happy에서 "h"의 위치 = 5
print("%s에서 \"h\"의 위치 = %d"%(mind,mind.find('h')))

title="토빈이와 함께 하는 신나는 파이썬 프로그래밍 입문" 
# 4. title 문자열에서 해당 길이를 카운트 후 해당 결과를 출력하시오.
# 반드시 서식문자 %기호(%d %f %c %s등)와 제어문자(\")를 사용할 것
#출력결과=> "토빈이와 함께 하는 신나는 파이썬 프로그래밍 입문"의 길이 = 27
print("\"%s\"의 길이 = %d"%(title,len(title)))

### 전체결과화면 ###
#I am sad 중에서 a 개수 = 2
#I am happy
#I am happy에서 "h"의 위치 = 5
#"토빈이와 함께 하는 신나는 파이썬 프로그래밍 입문"의 길이=27

