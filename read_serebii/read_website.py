from urllib.request import urlopen
from bs4 import BeautifulSoup

# Fetch the html file
response = urlopen('https://www.serebii.net/swordshield/maxraidbattles/den1.shtml')
html_doc = response.read()

# Parse the html file
soup = BeautifulSoup(html_doc, 'lxml')

name_box = soup.find('table', attrs={'class': 'trainer'})

def find_pokemon_id(name_box):
    pokemon_entry = name_box.find_all('td', attrs={'class': 'pkmn'})
    pkmn_ids = []
    for item in pokemon_entry:
        try:
            # print(item.a)
            basename = item.a.img['src'].split('/')[-1]
            pkmn_id = basename.split('.png')[0]
            pkmn_ids.append(pkmn_id)
            # print(item.a.img['src'])
            # print(pkmn_id)
            # i += 1
            
        except:
            pass
    return(pkmn_ids)

# print(find_pokemon_id(name_box))



    # print(item.find('a').text)
# print(pokemon_entry)
# print(more_specific)
# for pokemon in pokemon_entry:
    # print(pokemon.find('img', attrs={'src'}))
#     print(pokemon.get('a'))

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