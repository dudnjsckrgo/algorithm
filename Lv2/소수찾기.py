# 소수찾기
# lv 2

# 코드 설명:

# is_prime 함수는 주어진 숫자가 소수인지 판별하는 함수입니다. 2보다 작은 숫자는 소수가 아니므로 False를 반환하고, 2부터 숫자의 제곱근까지 숫자를 나누어 떨어지는지 확인합니다. 나누어 떨어지는 숫자가 없다면 소수입니다.
# solution 함수에서는 permutations 함수를 사용하여 주어진 문자열에서 가능한 모든 숫자 조합을 생성합니다. 문자열의 길이만큼 반복하면서 1개부터 문자열 길이까지의 순열을 생성합니다.
# 생성된 각 순열을 숫자로 변환하고, is_prime 함수를 사용하여 소수인지 판별합니다. 소수인 경우 prime_set에 추가합니다. 집합(set)을 사용하여 중복을 제거합니다.
# 최종적으로 prime_set의 길이를 반환하여 만들 수 있는 소수의 개수를 출력합니다.
# 이 솔루션은 문자열의 모든 가능한 숫자 조합을 생성하고 소수 판별을 수행하여 소수의 개수를 반환합니다. 문제의 제한사항을 모두 만족하는 솔루션입니다.

from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    prime_set = set()
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        for perm in perms:
            num = int(''.join(perm))
            if is_prime(num):
                prime_set.add(num)
    return len(prime_set)

