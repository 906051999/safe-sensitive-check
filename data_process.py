import os
import json
import hashlib
import shutil
import glob
import data_process


def hash_string(s):
    return hashlib.sha256(s.encode()).hexdigest()


def generate_json_structure(txt_file):
    # Get the base name of the txt_file
    base_name = os.path.splitext(os.path.basename(txt_file))[0]
    # Create the json_file name based on the txt_file name
    json_file = base_name + '.json'

    with open(txt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    data = {}
    for line in lines:
        line = line.strip()
        if line:  # ignore empty lines
            first_char_hash = hash_string(line[0])
            last_char_hash = hash_string(line[-1])
            keyword_hash = hash_string(line)
            if first_char_hash not in data:
                data[first_char_hash] = []
            data[first_char_hash].append({last_char_hash: keyword_hash})

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# 格式化json文件，便于检查
def format_json_file(input_file):
    # Get the base name of the txt_file
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    # Create the json_file name based on the txt_file name
    output_file = 'formatted_' + base_name + '.json'

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def generate_json_file():
    # Step 1: 遍历text文件夹下的所有txt文件
    txt_files = glob.glob('sensitive_data/text/*.txt')

    for txt_file in txt_files:
        # Step 2: 对每个txt文件调用data_process.generate_json_structure()方法
        data_process.generate_json_structure(txt_file)

        # Get the base name of the txt_file
        base_name = os.path.splitext(os.path.basename(txt_file))[0]
        # Create the json_file name based on the txt_file name
        json_file = base_name + '.json'

        # Step 3: 将生成的json文件移动到json文件夹中
        shutil.move(json_file, 'sensitive_data/json/' + json_file)

    # Step 4: 遍历data文件夹下的所有json文件，将它们的内容合并到一个新的json文件中
    merged_data = {}
    json_files = glob.glob('sensitive_data/json/*.json')

    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        merged_data.update(data)

    merged_file_name = 'keywords.json'
    with open(merged_file_name, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=4)
