a = input("Enter a sentence: ")
cur = ""
freq = {}
high = 0
word = ""
for i in a:
    if i!=" ":
        cur += i
    else:
        if cur:
            freq[cur] = freq.get(cur,0)+1
            cur = ""
if cur:
    freq[cur] = freq.get(cur,0)+1
for key,value in freq.items():
    if value>high:
        high = value
        word = key
print(f"The Highest Frequency word  in the sentence is: {word}.")