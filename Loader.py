import json
import operator
import chardet
from pprint import pprint

newsafr = 'newsafr.json'
newsafr_encode = 'utf-8'
newscy = 'newscy.json'
newscy_encode = 'KOI8-R'
newsfr = 'newsfr.json'
newsfr_encode = 'ISO-8859-5'
newsit = 'newsit.json'
newsit_encode = 'windows-1251'


def news_sorted(text_on_sorted):
    with open(text_on_sorted,'rb') as f:
        news = json.load(f)
        code = news['rss']['channel']['description'].encode()
        result = chardet.detect(code)
        print(result['encoding'])

    new_dict_news = {}
    dict_text_before_word_count = {}
    list_before_cut = []
    list_finish = []
    list_text_before_len = []
    new_list_news = []

    new_dict_news_source = news['rss']['channel']['items']
    new_dict_news.update(news.pop('rss'))
    new_dict_news.update(new_dict_news.pop('channel'))

    for new in new_dict_news:
        new_list_news.append(new_dict_news[new])
        if type(new_dict_news[new]) == str:
            list_before_cut.append(new_dict_news[new])

    for news in new_dict_news_source:
        for new in news.values():
            list_before_cut.append(new)


    for line in list_before_cut:
        for word in line.split():
            list_finish.append(word)

    for word in list_finish:
        if len(word) > 5:
            list_text_before_len.append(word)

    for i,word, in enumerate(list_text_before_len):
        dict_text_before_word_count.update({word : list_text_before_len.count(list_text_before_len[i])})

    sorted_finish = sorted(dict_text_before_word_count.items(), key = operator.itemgetter(1), reverse = True)
    return pprint(sorted_finish[0:10])


print("Сортировка Топ-10 Африка")
news_sorted(newsafr)
print("Сортировка Топ-10 Россия")
news_sorted(newscy)
print("Сортировка Топ-10 Россия-2")
news_sorted(newsfr)
print("Сортировка Топ-10 Италия")
news_sorted(newsit)