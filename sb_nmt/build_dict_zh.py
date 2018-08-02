from collections import Counter
import jieba

jieba.set_dictionary('../jieba_dict/dict.txt.big')

all_words=[]
output = open('../output/zh_dict.txt', 'w', encoding='utf-8')
with open('../src_corpus/TED2013/TED2013.en-zh.zh', 'r', encoding='utf-8') as content :
    for texts_num, line in enumerate(content):
        line = line.strip('\n')
        words = jieba.cut(line, cut_all=False)
        all_words.extend(words)

    output.write('<blank>\n')
    output.write('<s>\n')
    output.write('</s>\n')
    word_freq = Counter(all_words)
    common_words = word_freq.most_common(50000)
    for token, _ in common_words:
        output.write(token+'\n')
    output.close()

