import json
import hashlib
import re


def hash_string(s):
    return hashlib.sha256(s.encode()).hexdigest()


def match_and_replace_keywords_in_text(text, json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    matched_keywords = []
    replaced_text = text

    i = 0
    while i < len(replaced_text):
        for j in range(i + 1, len(replaced_text) + 1):
            keyword = replaced_text[i:j]
            first_char_hash = hash_string(keyword[0])
            if first_char_hash not in data:
                break
            last_char_hash = hash_string(keyword[-1])
            keyword_hash = hash_string(keyword)
            for item in data[first_char_hash]:
                if last_char_hash in item and item[last_char_hash] == keyword_hash:
                    matched_keywords.append(keyword)
                    replaced_text = replaced_text.replace(keyword, '***', 1)
                    i = j - 1
                    break
            else:
                continue
            break
        i += 1

    # Replace consecutive "***" with a single "***"
    replaced_text = re.sub(r'\*{3,}', '***', replaced_text)

    return matched_keywords, replaced_text



