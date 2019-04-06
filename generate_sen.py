grammar = """
sentence => noun_phrase verb_phrase 
noun_phrase => Article Adj* noun
Adj* => null | Adj Adj*
verb_phrase => verb noun_phrase
Article =>  一个 | 这个
noun =>   女人 |  篮球 | 桌子 | 小猫
verb => 看着   |  坐在 |  听着 | 看见
Adj =>   蓝色的 |  好看的 | 小小的
"""


def name_get(grammar):
    lines = grammar.split('\n')
    dict_op = {}
    for line in lines:
        line = line.strip()
        if line == '':
            continue
        name = line.split('=>')[0].strip()
        string_sentence = line.split('=>')[1].strip()
        dict_op[name] = string_sentence
    return dict_op

import random
def recurr(sentence,dict_op,list_all):
    sentence = sentence.strip()
    if ' ' in sentence:
        parts_sen = sentence.split(' ')
        for part_sen in parts_sen:
            recurr(part_sen, dict_op, list_all)
    elif sentence not in dict_op:
        if sentence!= 'null':
            list_all.append(sentence)
        return list_all
    else:
        name_op = sentence
        string_op = dict_op[name_op]
        if '|' in string_op:
            part = random.choice(string_op.split('|'))
            part = part.strip()
            recurr(part,dict_op,list_all)
        elif ' ' in string_op:
            parts = string_op.split(' ')
            for part in parts:
                recurr(part, dict_op, list_all)

        return list_all

dict_op = name_get(grammar)
list_all = recurr('sentence',dict_op,[])
print(''.join(list_all))
