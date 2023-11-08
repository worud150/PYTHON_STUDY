import pandas as pd
raw_data = {'col0' : [1, 2, 3, 4],
            'col1' : [10, 20, 30, 40],
            'col2' : [100, 200, 300, 400]} #리스트 자료형으로 생성
raw_data1 = pd.DataFrame(raw_data) #데이터 프레임으로 전환
raw_data2 = pd.DataFrame(raw_data) #데이터 프레임으로 전환

xlsx_dir = 'sample.xlsx'

# wirte xlsx
with pd.ExcelWriter(xlsx_dir) as writer:
    raw_data1.to_excel(writer, sheet_name= 'raw_data1') # raw_data1 시트에 저장
    raw_data2.to_excel(writer, sheet_name= 'raw_data2') # raw_data2 시트에 저장

# read xlsx
df = pd.read_excel(xlsx_dir, sheet_name=['raw_data1', 'raw_data2'])
print(df['raw_data1'])
print(df['raw_data2'])

# update xlsx


for i in file_list:
    data = pd.DataFrame(list(i))
    print(data)
    data.to_excel("www.xlsx", header=False, index=False)
    
for i in file_list:
    data = pd.Series(i)
    print(data)
data.to_excel("qqq.xlsx", index= False, header=False)