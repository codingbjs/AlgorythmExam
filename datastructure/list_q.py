# 자연수 배열에서 가장 큰 수 찾기

def check_max(arr):
    _max = arr[0]
    for num in arr:
        if num > _max:
            _max = num
    return _max


# 자연수 배열에서 가장 큰 2 수 찾아 배열 반환
def check_max2(arr):
    _max_1 = arr[0]
    _max_2 = arr[1]

    for num in arr:
        if num > _max_1:
            _max_2 = _max_1
            _max_1 = num
        elif num > _max_2:
            _max_2 = num

    return [_max_1, _max_2]


# 앞으로 읽어도, 뒤로 읽어도 같은 단어(회문) 인지 검사하는 함수 작성
# 기러기, 토마토, 역삼역
# aabaa - True
# aaabaa - False
def check_palindrome(text):
    left_point = 0
    right_point = len(text) - 1

    while left_point < right_point:
        if text[left_point] != text[right_point]:
            return False
        left_point += 1
        right_point -= 1

    return True


def check_palindrome1(text):
    rev_text = ""
    for char in text:
        rev_text = char + rev_text

    return rev_text == text
