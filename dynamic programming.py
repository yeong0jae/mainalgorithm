# 다이나믹 프로그래밍의 사용 조건 - 1. 큰 문제를 작은 문제로 나눌 수 있다. 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.(메모이제이션, dp 테이블)


# 탑 다운(하향식) 방식. 재귀

d = [0] * 100 # 메모이제이션을 위한 리스트

def pibo(x):
  print('f(' + str(x) + ')', end = ' ')
  if x == 1 or x == 2: # 종료조건
    return 1
  if d[x] != 0: # 메모이제이션
    return d[x]
  d[x] = pibo(x - 1) + pibo(x - 2)
    return d[x]


# 바텀 업(상향식) 방식. 반복

d = [0] * 100 # dp 테이블

d[1] = 1 # 초기값
d[2] = 1

for i in range(3, 100) # 반복조건
  d[i] = d[i - 1] + d[i - 2]
