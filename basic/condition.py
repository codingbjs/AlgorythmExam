# 세 수 중 최대값 구하기
def max(a, b, c):
    _max = a
    if b > _max:
        _max = b
    if c > _max:
        _max = c
    return _max


# 세 수 중 최소값 구하기
def min(a, b, c):
    _min = a
    if b < _min:
        _min = b
    if c < _min:
        _min = c
    return _min


# 세 수 중 중간값 구하기
def med(a, b, c):
    _med = a
    if (b <= _med <= c) or (c <= _med <= b):
        pass
    elif (a <= _med <= c) or (c <= _med <= a):
        _med = _med
    else:
        _med = c
    return _med


if __name__ == '__main__':
    print(max(50, 255, 30))
    print(min(50, 255, 30))
    print(med(50, 255, 30))
