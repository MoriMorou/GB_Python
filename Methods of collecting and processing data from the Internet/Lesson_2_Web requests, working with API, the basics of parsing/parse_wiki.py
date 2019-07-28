
# Задание 2. В приложении парсинга википедии получить первую ссылку на другую страницу и вывести все значимые слова
# из неё. Результат записать в файл в форматированном виде

# Задание 3.*Научить приложение определять количество ссылок в статье. Спарсить каждую ссылку и результаты записать в
# отдельные файлы.


from requests import get
import re

def get_link(topic):
    link = "https://ru.wikipedia.org/wiki/" + topic.capitalize()
    return link

def get_topic_page(link):
    html = get(link).text
    return html

def get_topic_text(topic):
    html_content = get_topic_page(topic)
    words = re.findall("[а-яА-Я]{3,}",html_content)
    return words

def get_common_words(topic):
    words_list = get_topic_text(topic)
    rate={}
    for word in words_list:
        if word in rate:
            rate[word]+=1
        else:
            rate[word]=1
    rate_list = list(rate.items())
    rate_list.sort(key = lambda x :-x[1])

    return rate_list

def visualize_common_words(topic):
    words = get_common_words(topic)
    for w in words[0:10]:
        print(f'{w[0]} встречается {w[1]} раз')


def get_links(topic):
    text = get_topic_page(topic)
    links = re.findall('<li><a rel="nofollow" class="external text" href="(.*)">(.*)<\/a></li>', text)
    return links

def save_link_into_file(link):
    words_in_link = get_common_words(link[0])

    file = open(link[1]+".txt", "w+")
    for word in words_in_link:
        str_ = str(word[0])+' : '+str(word[1])
        file.write(str_+"\n")


def parse_links_from_topic(wiki_topic):
    topic_link = get_link(wiki_topic)
    links = get_links(topic_link)

    for link in links:
        save_link_into_file(link)

    return len(links)

<<<<<<< HEAD
topic = 'Льгов'
links_len = parse_links_from_topic(topic)
print('Количество доступных ссылок', links_len)
=======
print(return_words('Здравствуйте!'))
>>>>>>> master
