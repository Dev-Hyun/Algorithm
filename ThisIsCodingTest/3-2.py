#큰 수의 법칙

n, m, k = map(int, input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data [n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print (result)


## More Greedy way
'''
n, m, k = map(int, input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data [n-2]

first 를  k번 더하고 second를 1번 더하게되겠지.
그러면 K * first + 1 * second

count = imt(m/K+1) * k K +1 을 계속 반복 하겠지 몇번? m으로 나눈 나머지의 몫만큼
count = count + m % (K+1) // k+1번으로 나눈 나머지 만큼 다시 더해준다.

따라서

result = 0
result += (count) * (first) // first가 나온 개수 만큼 곱해준다.
result += (m-count) * (second) // second는 전체 m 에서 first가 나온 count만큼 뺴준 개수이다.

print(result)
'''


