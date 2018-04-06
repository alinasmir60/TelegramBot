import random

def choose_word():
    choice_word = random.choice(word)
    trans_word = [translater_word(choice_word, "ru-en")]
    while len(trans_word) <= 2:
        w = random.choice(translat)
        if w not in trans_word:
            trans_word.append(w)
    return choice_word, trans_word


def translater_word(text, lang):
    translator_uri = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    response = requests.get(
        translator_uri,
        params={
            "key": "trnsl.1.1.20180401T224213Z.c1143abeda1b8ddf.366d17dd4a20cb2ccc211c86c4bb1ec637a175de",
            "lang": lang,
            "text": text
        })
    return response.json()["text"][0]