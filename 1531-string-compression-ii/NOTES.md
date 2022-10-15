class Solution:
def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
cur = 0
com, count = [], []
while cur <= len(s)-1:
start = cur
end = cur + 1
if end >= len(s):
count.append(end-start)
com.append(s[cur])
break
while s[end] == s[start]:
end += 1
if end >= len(s):
break
count.append(end-start)
com.append(s[cur])
cur = end
print(com, count)
length = 0
target = sorted(range(len(count)), key=count.__getitem__)
for i in range(len(target)):
if count[target[i]] <= k:
k = k - count[target[i]]
count[target[i]] = 0
com[target[i]] = 0
else:
count[target[i]] = count[target[i]] - k
break
# print(count, k)
# print(com, count)
​
com = [i for i in com if i != 0]
count = [i for i in count if i != 0]
cur += 1