# 100에서 1까지 숫자를 출력. 단, 369 게임처럼 3을 포함하고 있는 경우, 갯수만큼 “짝” 을 출력. (33일경우 “짝짝”)

i = 100
while i >= 1:
    num_str = str(i)
    count = 0

    for ch in num_str:
        if ch in "369":
            count += 1

    if count > 0:
        print("짝" * count)
    else:
        print(i)

    i -= 1