import shutil
import os

# 1. 파일, 이동, 복사, 삭제 프로그램 

dir_path = os.getcwd() # 현재 폴더의 경로
file_list = os.listdir(dir_path) # 현재 폴더의 파일 리스트

shutil.move("result.txt", "kim") # 파일 이동
shutil.copy("sample.txt", "kim") # 파일 복사
os.remove("새 파일.txt") # 파일 삭제
