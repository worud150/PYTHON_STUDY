import os
import pandas as pd

dir_path = os.getcwd() # 현재 폴더의 경로
file_list = os.listdir(dir_path) # 현재 폴더의 파일 리스트

print("dir_path : ", dir_path)
print("file_list : ", file_list)


print(file_list[0])

print("----------------------------------")

data = pd.Series(file_list)

data.to_excel("ggg.xlsx", index=False, header=False)

