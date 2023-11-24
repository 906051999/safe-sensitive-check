import os
import glob
import data_check
import data_process

data_process.generate_json_file()

# Check if input directory exists, if not, create it
if not os.path.exists('input'):
    os.makedirs('input')
# 遍历input文件夹下的所有txt文件
txt_files = glob.glob('input/*.txt')

# 打开info.txt文件，准备记录matched_keywords
with open('info.txt', 'w', encoding='utf-8') as info_file:
    for txt_file in txt_files:
        # 读取txt文件的内容
        with open(txt_file, 'r', encoding='utf-8') as f:
            text = f.read()

        # 使用data_check.match_and_replace_keywords_in_text方法处理文本
        matched_keywords, replaced_text = data_check.match_and_replace_keywords_in_text(text, 'keywords.json')

        # 将replaced_text输出到output文件夹下，命名规则是输入文件名+replace

        # Check if output directory exists, if not, create it
        if not os.path.exists('output'):
            os.makedirs('output')
        base_name = os.path.splitext(os.path.basename(txt_file))[0]
        output_file = 'output/' + base_name + '_replace.txt'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(replaced_text)

        # 将每个输入文件的matched_keywords记录到info.txt中，标注对应的文件名
        info_file.write(f'Matched keywords for file {base_name}:\n')
        # 将matched_keywords分行输出，每行最多20个
        for i in range(0, len(matched_keywords), 20):
            info_file.write(f' {matched_keywords[i:i+20]}\n')
        info_file.write('\n')

