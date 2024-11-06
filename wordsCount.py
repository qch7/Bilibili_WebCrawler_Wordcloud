"""数据处理部分，分词，统计词频和词性"""
import jieba
import json
import jieba.posseg as pseg


def words_count(txt_name, txt_path="./res/result/"):
    """统计词频"""
    s = open(txt_path+txt_name, 'r', encoding='utf-8').read()
    rp_str = '： ， ；、？——‘’（）#！\n '
    for i in rp_str:
        s = s.replace(i, '')
        s = ''.join(s.split())
    jieba.load_userdict(txt_path+txt_name)
    words = jieba.lcut(s)
    stopwords = open('./res/stopwords/stopwords.txt', 'r', encoding='utf-8').read()
    stopwords_list = list(stopwords.split("\n"))  # 去除停用词
    words_dict = {}
    for i in words:
        if len(i) == 1:
            continue
        if i not in stopwords_list:
            words_dict[i] = words_dict.get(i, 0) + 1  # 统计词频
    words_list = list(words_dict.items())
    words_list.sort(key=lambda x: x[1], reverse=True)  # 排序
    return words_list


def save_words_count_to_json(words_list, json_name="words_count.json", json_path="./res/result/"):
    """保存词频统计结果到./res/result/words_count.json，作为生成词云图的参数"""
    with open(json_path+json_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(dict(words_list), indent=4))
    f.close()


def save_words_to_json(words_json_name="words.json", words_count_json_name="words_count.json", json_path="./res/result/"):
    """统计词性，保存进一步的处理结果到./res/result/words.json，以便筛选"""
    with open(json_path+words_count_json_name, 'r', encoding='utf-8') as f:
        words = dict(json.load(f))
    f.close()
    for k, v in words.items():
        word_cut = pseg.cut(k)
        for word, flag in word_cut:
            if word == k:
                words[k] = [str(v), flag]
                break
        else:
            words[k] = [str(v), "un"]
    with open(json_path+words_json_name, 'w', encoding='utf-8') as f:
        json.dump(words, f, indent=4)
    f.close()
