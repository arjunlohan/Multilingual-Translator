import requests
import re
import sys
from bs4 import BeautifulSoup

list_languages = ["Arabic", "German", "English", "Spanish", "French", "Hebrew", "Japanese",
                  "Dutch", "Polish", "Portuguese", "Romanian", "Russian", "Turkish"]


def menu():
    print("Hello, welcome to the translator. Translator supports:")
    for i in range(len(list_languages)):
        print(str(i+1)+str(". ")+str(list_languages[i]))


args = sys.argv

if len(args) < 4:
    print("Error, please enter three arguments. First argument is language of the word, "
              "second argument is language you want to translate to and third argument is word you want to translate.")
else:
    #print('Type the number of your language:')
    if args[1].title() not in list_languages:
        print("Sorry, the program doesn't support " + args[1])
    else:
        your_language = int(list_languages.index(args[1].title()))
    #print("Type the number of language you want to translate to:")
    if args[2].title() not in list_languages:
        if args[2].title() == 'All':
            request_language = 0
        else:
            print("Sorry, the program doesn't support "+args[2])
    else:
        request_language = int(list_languages.index(args[2].title()))
    #print("Type the word you want to translate:")
    word_language = args[3].lower()

try:
    file_name = str(word_language)+".txt"
    file = open(file_name, 'w', encoding='utf-8')
    if request_language != 0:
        url = str("https://context.reverso.net/translation/") + list_languages[your_language].lower() + "-" + list_languages[request_language].lower() + "/" + word_language
        request_connection = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

        if request_connection.status_code:
            soup = BeautifulSoup(request_connection.content, 'html.parser')
            word_legit = soup.find_all('span', {"class": "wide-container message"})
            word_legit = [x.text for x in word_legit]
            if "not found in Context" in "".join(word_legit):
                print("Sorry, unable to find "+ word_language)
            else:
                file.write((list_languages[request_language]+" Translations:"+"\n"))
                print(list_languages[request_language]+" Translations:")
                translation_list = soup.find_all('div', {'id': 'translations-content'})
                translations_list_text = [x.text for x in translation_list]
                translations_list_text = [x.replace('\n', '') for x in translations_list_text]
                translations_list_text = [x.replace('          ', ' 0 ') for x in translations_list_text]
                translations_list_text = re.sub(r"\s+", " ", " ".join(translations_list_text))
                translations_list_text = translations_list_text.split(' 0 ')
                translations_list_text = translations_list_text[1:6]
                file.write('\n'.join(str(line) for line in translations_list_text))
                print(*translations_list_text, sep='\n')
                file.write('\n')
                file.write('\n')
                print()
                file.write(list_languages[request_language]+" Examples:"+"\n")
                print(list_languages[request_language]+" Examples:")
                translation_examples = soup.find_all('div', {'class': 'example'})
                translation_examples = [x.text for x in translation_examples]
                translation_examples = [x.replace('\n', '') for x in translation_examples]
                translation_examples = [x.replace('          ', ' 0 ') for x in translation_examples]
                translation_examples = re.sub(r"\s+", " ", " ".join(translation_examples))
                translation_examples = translation_examples.split(' 0 ')
                if len(translation_examples) > 11:
                    max_list = 11
                else:
                    max_list = int(len(translation_examples))
                translation_examples = translation_examples[1:max_list]
                for i in range(0, int(len(translation_examples)), 2):
                    file.write(translation_examples[i]+"\n")
                    print(translation_examples[i])
                    file.write(translation_examples[i+1]+"\n")
                    print(translation_examples[i+1])
                if i <= int(len(translation_examples))-1:
                    file.write('\n')
                    file.write('\n')
        else:
            print("Something wrong with your internet connection")
    else:
        for i in range(1, len(list_languages)+1):
            if your_language + 1 == i:
                pass
            else:
                request_language = i
                url = str("https://context.reverso.net/translation/") + list_languages[your_language].lower() + "-" + \
                      list_languages[request_language-1].lower() + "/" + word_language
                request_connection = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
                if request_connection.status_code:
                    soup = BeautifulSoup(request_connection.content, 'html.parser')
                    word_legit = soup.find_all('span', {"class": "wide-container message"})
                    word_legit = [x.text for x in word_legit]
                    if "not found in Context" in "".join(word_legit):
                        print("Sorry, unable to find " + word_language)
                    else:
                        file.write(list_languages[request_language-1]+" Translations:"+"\n")
                        print(list_languages[request_language-1] + " Translations:")
                        translation_list = soup.find_all('div', {'id': 'translations-content'})
                        translations_list_text = [x.text for x in translation_list]
                        translations_list_text = [x.replace('\n', '') for x in translations_list_text]
                        translations_list_text = [x.replace('          ', ' 0 ') for x in translations_list_text]
                        translations_list_text = re.sub(r"\s+", " ", " ".join(translations_list_text))
                        translations_list_text = translations_list_text.split(' 0 ')
                        translations_list_text = translations_list_text[1:6]
                        file.write('\n'.join(str(line) for line in translations_list_text))
                        print(*translations_list_text, sep='\n')
                        file.write('\n')
                        file.write('\n')
                        print()
                        file.write(list_languages[request_language-1] + " Examples:"+"\n")
                        print(list_languages[request_language-1] + " Examples:")
                        translation_examples = soup.find_all('div', {'class': 'example'})
                        translation_examples = [x.text for x in translation_examples]
                        translation_examples = [x.replace('\n', '') for x in translation_examples]
                        translation_examples = [x.replace('          ', ' 0 ') for x in translation_examples]
                        translation_examples = re.sub(r"\s+", " ", " ".join(translation_examples))
                        translation_examples = translation_examples.split(' 0 ')
                        if len(translation_examples) > 11:
                            max_list = 11
                        else:
                            max_list = int(len(translation_examples))
                        translation_examples = translation_examples[1:max_list]
                        for i in range(0, int(len(translation_examples)), 2):
                            file.write(translation_examples[i]+"\n")
                            print(translation_examples[i])
                            file.write(translation_examples[i + 1]+"\n")
                            print(translation_examples[i + 1])
                        if request_language <= len(list_languages)-1:
                            file.write('\n')
                            file.write('\n')
                            print()
                            print()
                else:
                    print("Something wrong with your internet connection")
    file.close()
except NameError:
    pass
