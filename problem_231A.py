n = int(input())
result = 0
for i in range(n):
    str = input()
    opinions = str.split(' ')
    count_op = 0
    for op in opinions:
        count_op += int(op)
    if count_op >= 2:
        result += 1

print(result)
