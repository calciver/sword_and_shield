from urllib.request import urlopen
from bs4 import BeautifulSoup

# Fetch the html file
response = urlopen('https://www.serebii.net/swordshield/maxraidbattles/den1.shtml')
html_doc = response.read()

# Parse the html file
soup = BeautifulSoup(html_doc, 'html.parser')

name_box = soup.find('table', attrs={'class': 'trainer'})

pokemon_entry = name_box.find_all('td', attrs={'class': 'pkmn'})
for pokemon in pokemon_entry:
    
    print(pokemon.get('a'))

# print(pokemon_entry)

# print(name_box)
# # Format the parsed html file
# strhtm = soup.prettify()
# begin = strhtm.index('<td class="pkmn">')
# end = strhtm.index('Location of Den')

# # Print the first few characters
# print (strhtm[begin:end])
# # print (strhtm)
# print(begin,end)