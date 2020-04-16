from urllib.request import urlopen
from bs4 import BeautifulSoup

# Fetch the html file
# response = urlopen('https://www.serebii.net/swordshield/maxraidbattles/den1.shtml')
response = urlopen('https://www.serebii.net/swordshield/maxraidbattles/den85.shtml')
html_doc = response.read()

# Parse the html file
soup = BeautifulSoup(html_doc, 'lxml')

name_box = soup.find('table', attrs={'class': 'trainer'})

def find_pokemon_id(name_box):
    pokemon_entry = name_box.find_all('td', attrs={'class': 'pkmn'})
    pkmn_ids = []
    for item in pokemon_entry:
        try:
            basename = item.a.img['src'].split('/')[-1]
            pkmn_id = basename.split('.png')[0]
            pkmn_ids.append(pkmn_id)            
        except:
            pass
    return(pkmn_ids)

def find_pokemon_rarity_ability(name_box):
    total_len = len(name_box.find_all('tr',recursive=False))
    rarity_list = []
    ability_list = []
    i = 4
    while i<total_len:
        rarity_entry = name_box.find_all('tr',recursive=False)[i]
        parse_rarity(rarity_entry)
        rarity_list.append(rarity_entry)

        ability_entry = name_box.find_all('tr',recursive=False)[i+1]
        ability_list.append(ability_entry)
        i += 6

    # print(rarity_list)
    # print(ability_list)
    # print(len(rarity_list),len(ability_list))

def parse_rarity(rarity_entry):
    all_rarities = rarity_entry.find_all('td')
    for each_rarity_info in all_rarities:
        # print(each_rarity_info)
        # for b in each_rarity_info.find_all('b'):
        #     if b.next_sibling:
        #         print(b.next_sibling)
        print('Rarity')
        for br in each_rarity_info.find_all('br'):
            if br.next_sibling:
                print(br.next_sibling)
        # print(each_rarity_info)

find_pokemon_rarity_ability(name_box)


# print(len(name_box.find_all('tr',recursive=False)))
# print(name_box.find_all('tr',recursive=False)[4])
# print(name_box.find_all('tr',recursive=False)[5])
# print(name_box.find_all('tr',recursive=False)[4+6])
# print(name_box.find_all('tr',recursive=False)[5+6])

# print(name_box.find_all('tr',recursive=False)[4+6+6])
# print(name_box.find_all('tr',recursive=False)[5+6+6])

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