import json

# 读取txt文件
txt_file_path = "list.txt"
with open(txt_file_path, "r") as file:
    # 以每行为一个元素构建列表
    lines = file.read().splitlines()

# 构建json对象
data = {"websites": lines}

# 将数据写入json文件
json_file_path = "output.json"
with open(json_file_path, "w") as json_file:
    json.dump(data, json_file, indent=2)
