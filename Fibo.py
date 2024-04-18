# 메모이제이션과 테뷸레이션 방식 두개 적용을 하지 않은다면 중복 계산에 비효율적임

# 메모이제이션: 함수 호출 스택을 사용하므로 일반적으로 Bottom-up 방식보다 느림
# 테뷸레이션: 함수 호출 오버헤드가 없음

#피보나치 기본 함수
def solution(n):
    answer = 0
    if(n==0):
        return 0
    elif(n==1):
        return 1
    elif(n>=2):
        answer = solution(n-1) + solution(n-2)
    return answer

#메모이제이션
def fibonacci_memoization(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
        return memo[n]
#테뷸레이션
def solution_Tabulation(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    #모듈러 연산(나머지 연산)을 수행
    dp[n]=dp[n] % 1234567
    return dp[n]

#NO 재귀
def simple_solution(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    a=a % 1234567
    return a


print(solution(11))