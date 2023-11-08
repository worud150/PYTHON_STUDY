def fib(n):
    if n == 0:
        return 0
    if n == 1 :
        return 1
    return fib(n-2) + fib(n-1)

for i in range(10):
    print(fib(i))

with open("sample.txt", "r") as f:
    read = f.readlines()
total = 0
for i in read:
    score = int(i)
    total += score

avg = total / len(read)

with open("result.txt", "w") as f:
    f.write(str(avg))