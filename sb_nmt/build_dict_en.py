from collections import Counter
import spacy

nlp = spacy.load('en_core_web_lg')

all_words=[]
output = open('../output/en_dict.txt', 'w', encoding='utf-8')
with open('../src_corpus/TED2013/TED2013.en-zh.en', 'r', encoding='utf-8') as corpus_file :
    content = corpus_file.read()
    lines = content.split('\n')
    for texts_num, line in enumerate(lines):
        doc = nlp(line)
        for token in doc:
            all_words.append(token.text)

    output.write('<blank>\n')
    output.write('<s>\n')
    output.write('</s>\n')
    word_freq = Counter(all_words)
    common_words = word_freq.most_common(50000)
    for token, _ in common_words:
        output.write(token+'\n')
    output.close()
