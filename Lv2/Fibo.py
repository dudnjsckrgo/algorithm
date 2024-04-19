#프로그래머스> 코딩테스트 연습> 피보나치 수

#동적 프로그래밍 사용 해야됨

# 메모이제이션: 함수 호출 스택을 사용하므로 일반적으로 Bottom-up 방식보다 느림
# 테뷸레이션: 함수 호출 오버헤드가 없음

# 피보나치 기본 함수
# 메모이제이션과 테뷸레이션 방식 두개 적용을 하지 않은다면 중복 계산에 비효율적임
def solution(n):
    answer = 0
    if(n==0):
        return 0
    elif(n==1):
        return 1
    elif(n>=2):
        answer = solution(n-1) + solution(n-2)
    return answer

#메모이제이션은 테스트케이스에서 런타임 에러가 남
#런타임 에러가 나는 이유: 일부 언어는 재귀 호출을 할 수 있는 횟수가 정해져 있고, 횟수를 넘어 재귀 호출을 하면 런타임 에러를 내도록 설계되어 있습니다.
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
    
    #모듈러 연산(나머지 연산)을 수행: 이 나머지 연산은 결과를 1234567 미만의 값으로 유지하므로, 정수 오버플로를 방지할 수 있습니다.
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