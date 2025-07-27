#학번: ___________
#주제: 객체 지향 프로그래밍 예제
#코드(test3.png)를 그대로 입력하고 결과를 확인 후 분석한다

#문제: 다음 코드를 실행시켰을 때 나오는 결과화면은?
class Animal(object):
    species="포유류"  # 속성(클래스 변수) 초기화
    def __init__(self, name):  # 생성자, 객체가 생성될 때 호출됨
        self.name = name       # 속성(인스턴스 변수) 초기화
        print("%s 객체 생성 시작" % name)  # 생성자 매개변수 출력

    def eat(self, friend_name):  # 메서드
        self.breed = "드워프"    # 속성(인스턴스 변수) 설정
        print("%s %s과 함께 식사중" % (self.name, friend_name))  # 속성과 매개변수 출력

    def show_breed(self):  # 메서드
        print("%s 품종 = %s" % (self.name, self.breed))  # 속성 출력


# 객체 생성→ 객체명 = 클래스명()
tobin = Animal("토빈")  # '토빈' 객체(인스턴스) 생성
tobin.eat("고빈")        # '토빈' 객체의 eat 메소드 호출
tobin.show_breed()       # '토빈' 객체의 show_breed 메소드 호출
print("종=", tobin.species)

wonbin = Animal("원빈")  # '원빈' 객체(인스턴스) 생성
wonbin.eat("나영")       # '원빈' 객체의 eat 메소드 호출
# print("종=", Animal("쪼앙").species)


### 결과화면(예시)
# 토빈 객체 생성 시작
# 토빈 고빈과 함께 식사중
# 토빈 품종 = 드워프
# 종= 포유류
# 원빈 객체 생성 시작
# 원빈 나영과 함께 식사중