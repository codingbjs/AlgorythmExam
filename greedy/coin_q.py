"""
매개변수로 금액을 전달하면 해당 금액을 최소한의 동전 개수로 동전 조합을 구할 수 있는 함수를 작성하시오
동전 종류 : 500, 100, 50, 10, 1
금액 : 3456
# {500:6, 100:4, 50:1, 10:1, 1:5}
"""


def coin_combi(change):
    coins = [500, 100, 50, 10, 1]
    coin_counts = {}  # 동전 개수를 저장할 딕셔너리

    for coin in coins:
        coin_count = change // coin  # 해당 동전으로 얼마나 사용할 수 있는지 계산
        change = change % coin  # 나머지 금액 계산

        if coin_count > 0:
            coin_counts[coin] = coin_count  # 딕셔너리에 동전 개수 저장

    return coin_counts


print(coin_combi(3465))

