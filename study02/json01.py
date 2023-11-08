# 3. json, xlsx, csv 파일 항목추가, 항목삭제, 항목 수정
# 3-01 json 쓰고 저장하기

import json

# set path and file name
path = "spmple.json"

# write json
data = {}
data['playlist'] = []
# data['playlist'].append({
#     "singer" : "TAEYEON",
#     "song" : "Weekend",
#     "date" : 20210706
# })

# data['playlist'].append({
#     "singer": "almost monday",
#     "song" : "til the ebd of time",
#     "date" : 20210709
# })

# data['playlist'].append({
#     "singer": "The Volunteers",
#     "song" : "Summer",
#     "date" : 20210527
# })

data['playlist'].append({
    "singer": "The Volunteers",
    "song" : "Summer",
    "date" : 20210527
})

print(data)

# save json
with open(path, 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, indent=4)
    
# read json
with open(path, "r") as json_file :
    json_date = json.load(json_file)
    
print(json_date)
