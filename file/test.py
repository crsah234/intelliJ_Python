# 정수 리스트 num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를
# return하도록 solution 함수를 완성해주세요. 음수가 없다면 -1을 return합니다.

def solution(num_list):
    answer = len(num_list) - 1
    for a in num_list:
        answer=answer-1
        if (a < 0):
            answer = len(num_list) - answer-2
            break

    return answer


print(solution([1,2,3,4,5,6,-1]))
