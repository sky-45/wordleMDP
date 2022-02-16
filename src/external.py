import requests
# fecth data from repo
def getWords(n):
    urlWords = "https://raw.githubusercontent.com/javierarce/palabras/master/listado-general.txt"
    r = requests.get(urlWords)
    words = r.text.split("\n")
    words = [word for word in words if len(word)==5]
    print("total words avaliable: ",len(words))
    return words[:n]

print(getWords(5))

