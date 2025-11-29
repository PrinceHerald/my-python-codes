a = input("Enter a sentence: ")
count = {}
now = ""
for i in a:
    if i != " ":
        now += i
    else:
        if now:
            count[now] = count.get(now,0) + 1
            now = ""
if now:
    count[now] = count.get(now,0) + 1
print(count)