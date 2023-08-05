[n, k]       = input().split()
participants = input().split()
result       = 0
for member in participants:
    if int(member) >= int(participants[int(k)-1]) and int(member) > 0:
        result += 1
print(result)
