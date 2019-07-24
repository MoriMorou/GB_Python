import collections
import requests
import re


def return_wiki_html(topic):
    wiki_request = requests.get(f'https://ru.wikipedia.org/wiki/{topic.capitalize()}')
    return wiki_request.text

def return_words(topic):
    wiki_html = return_wiki_html(topic)
    words = re.findall('[а-яА-Я]{3,}', wiki_html)
    words_counter = collections.Counter()
    for word in words:
        words_counter[word] += 1
    for word in words_counter.most_common(10):
        print(f'Слово {word[0]} встречается {word[1]} раз')
    return words_counter.most_common(10)


print(return_words('Трям!_Здравствуйте!'))
