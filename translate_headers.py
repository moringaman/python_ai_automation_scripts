

import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# get the webpage
url = "https://packaging.python.org/en/latest/tutorials/installing-packages/"
page = requests.get(url)

# create a BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')

# create a Translator object
translator = Translator()

# open a new file to write
f = open('headers_fr.html', 'w')

# write the html head tag
f.write('<head>\n')

# get all the html headers
headers = soup.find_all('h1', 'h2', 'h3', 'h4', 'h5')

# loop through each header
for header in headers:
    # translate the text
    translated_text = translator.translate(header.text, dest='fr').text
    # write the translated text in the new file
    f.write('<' + header.name + '>' +
            translated_text + '</' + header.name + '>\n')

# close the html head tag
f.write('</head>')

# close the file
f.close()
