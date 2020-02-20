# 프로그래머스 > 프로그래밍 강의 > 파이썬을 파이썬답게 > 파트6. Itertools / Collections 모듈 > 가장 많이 등장하는 알파벳 찾기


import collections

my_str = input().strip()

dic = collections.Counter(my_str)
maxNum = max(dic.values())
result = filter(lambda x: x[1]==maxNum, dic.items()) # 람다 표현식(lambda x: x[1]==maxNum)을 filter 함수의 인자로 사용.
answer = [key for key, value in result] # List Comprehension [ 계산식 for문 ] 사용
answer.sort()

print(''.join(answer))



# collections.Counter 클래스를 사용하면, Counter({'key': value}) 형태로 결과 값을 주어 리스트에 있는 어떤 element의 수를 쉽게 찾을 수 있다.
# lambda 매개변수들: 식
# filter(function_to_apply, list_of_inputs) -> Iterator를 반환함(다른 자료구조들로 변환시킬 수 있음)
# List Comprehension : 원하는 구성요소를 가지는 리스트를 쉽게 만듬
