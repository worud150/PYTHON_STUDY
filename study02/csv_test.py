import csv

with open('write.csv', 'w', newline='') as f :
    wr = csv.writer(f)
    wr.writerow([1,'test', '천안'])
    wr.writerow([2,'test2', '부산'])

with open('write.csv', "r") as f :
    rdr = csv.reader(f)
    for i in rdr:
        print(i[1])
        
        
print("--------------------")
 
with open("write.csv", 'a', newline='') as f:
    wr = csv.writer(f)
    wr.writerow([3, 'test3', '강원'])
    
f = open('write.csv','r')
rdr = csv.reader(f)
lines = []
for line in rdr:
    if line[1] == "test":
        line[2] = "hello"
    lines.append(line)
    
f = open('write.csv','w',newline='') #원본을 훼손할 위험이 있으니 다른 파일에 저장하는 것을 추천합니다.
wr = csv.writer(f)
wr.writerows(lines)
 
f.close()