f = open("두번째 새파일.txt" , 'r' )
line = f.readline()
print(line)
f.close

# while 1 :
#     data = input()
#     if not data: break
#     print(data)

f = open("두번째 새파일.txt" , 'r' )
lines = f.readlines()
for i in lines:
    print(i)
f.close

print("--------------------------------")
f = open("두번째 새파일.txt" , 'r' )
data = f.read()
print(data)
f.close

f = open("spample.txt", "r")
data = f.read()
print(data)