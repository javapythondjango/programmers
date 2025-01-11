def solution(number):
    answer = 0
    for x in number:
        answer+=int(x)
    return answer%9