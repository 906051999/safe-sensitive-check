# safe-sensitive-check
一个安全的、离线的敏感词检测，使用处理过的数据集，不会泄露敏感词，避免争议

## 功能
- 提供敏感词检测功能，自带转码后安全的敏感词文件，也可以在 `sensitive_data/text` 中加入自定义的敏感词
- 将需要检测的文本放在 `input` 文件夹下，执行 `main.py` 即可在 `output` 文件夹下输出替换后的文本
- 被检测的词汇在 `info.txt` 文件中体现
- 可使用 `test.py` 随机生成测试文本，会加入 `words.txt` 中的词汇

## 使用方法
1. 可在 `sensitive_data/text/words.txt` 中加入自定义的敏感词
2. 将需要检测的文本放在 `input` 文件夹下，执行main.py会自动创建input文件夹
3. 执行 `main.py`，在 `output` 文件夹下会生成替换后的文本
4. 查看 `info` 文件，可以看到被检测的词汇
5. 可以使用 `test.py` 随机生成测试文本

## 鸣谢
本项目使用了以下开源库中的数据集：
- [tencent-sensitive-words](https://github.com/cjh0613/tencent-sensitive-words) by cjh0613
- [commonly-used-chinese-characters-and-words](https://github.com/nk2028/commonly-used-chinese-characters-and-words) by nk2028

---
**项目使用copilot生成，仅供学习使用，不可用于商业用途，法律责任自负。**

以下是基础功能实现的对话输入：
- txt文件中每一行包含一个关键词，关键词包含中英文和标点符号，读取txt文件并转换为json文件。 json文件中包含：关键词的首字符的hash值 -》 关键词的尾字符的hash -》 关键词的hsah。
- 以关键词的首字符hash为入口，然后再以关键词的尾字符hash为入口，存储关键词的hash. 如果有多个关键词的首字符一致的，请在同一个首字符hash入口下继续添加。
- 根据json文件，可以优化算法，首先检测窗口首字符hash是否与json文件匹配，不匹配直接可以将窗口移位；其次如果首字符匹配，将窗口拓展检测尾字符hash是否与json中当前字符中的尾字符hash匹配，不匹配可将窗口移动下一位； 如果匹配了，则计算窗口内字符总hash，检测是否与json中尾字符对应的关键词hash匹配，不匹配窗口移位；
匹配则将窗口内字符置为未通过状态。 将关键词替换为的文本，如果有多个【星号】相连，去除多余的，只保留一个【星号】