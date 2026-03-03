# 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# https://chadireoroonu.tistory.com/349

# sort
def solution(phone_book):
    nums = sorted(phone_book)
    
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1][:len(nums[i])]:
            return False
    
    return True
