# 2. txt 읽고, 쓰기 
with open("hello.txt", "w") as f :
    for i in range(10):
        f.write("%d 번째 줄 입니다\n" %i)

with open("hello.txt", "r") as f :
    read = f.readlines()
    for i in read :
        print(i)