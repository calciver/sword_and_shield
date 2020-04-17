from urllib.request import urlopen
from bs4 import BeautifulSoup
import copy
import io
import csv
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
    full_rarity_list = []
    full_ability_list = []
    i = 4
    while i<total_len:
        rarity_entry = name_box.find_all('tr',recursive=False)[i]
        # full_rarity list = [{1: '35%'}, {1: '35%'},...] for all 24 pokemon
        full_rarity_list = full_rarity_list + parse_rarity_ability(rarity_entry,mode='rarity')

        ability_entry = name_box.find_all('tr',recursive=False)[i+1]
        # full_ability list = ['Standard', 'Hidden Possible',...] for all 24 pokemon
        full_ability_list = full_ability_list + parse_rarity_ability(ability_entry,mode='ability')
        i += 6

    return(full_rarity_list,full_ability_list)


def parse_rarity_ability(rarity_entry,mode = 'rarity'):
    all_info = rarity_entry.find_all('td')
    full_list = []
    for each_info in all_info:
        # For each pokemon
        rarity_dictionary = {}
        for br in each_info.find_all('br'):
            if br.next_sibling:
                statement = str(br.next_sibling)
                if mode == 'rarity':
                    num_stars = statement.count('&star')
                    percent = statement.split(':')[-1]
                    rarity_dictionary[num_stars] = percent[1:]
                elif mode == 'ability':
                    full_list.append(statement)
        if mode == 'rarity':
            full_list.append(rarity_dictionary)
    return(full_list)

def clean_representation(pkmn_id_list,pkmn_rarity_list,pkmn_ability_list):
    for i in range(len(pkmn_id_list)):
        print(f'Pokemon ID: {pkmn_id_list[i]}| Rarity: {pkmn_rarity_list[i]} | Ability: {pkmn_ability_list[i]}')

def write_to_csv(den_number,pkmn_id_list,pkmn_rarity_list,pkmn_ability_list,csv_file_path = 'read_serebii/den_information.csv'):
    # csv_file = io.open(csv_file_path,'w')

    csv_file = io.open(csv_file_path,'w')
    writer = csv.DictWriter(csv_file,fieldnames=['Den_Number','Pokemon_ID','Rarity','Ability'])
    writer.writeheader()

    # csv_file = io.open(self.csv_file_name,'a')
    # writer = csv.DictWriter(csv_file,fieldnames=self.fieldnames)
    for i in range(len(pkmn_id_list)):
        result_dictionary = {}
        result_dictionary['Den_Number'] = den_number
        result_dictionary['Pokemon_ID'] = pkmn_id_list[i]
        result_dictionary['Rarity'] = pkmn_rarity_list[i]
        result_dictionary['Ability'] = pkmn_ability_list[i]
        writer.writerow(result_dictionary)
    csv_file.flush()

def write_to_csv(csv_file_path='read_serebii/den_information.csv'):
    csv_file = io.open(csv_file_path,'w')
    writer = csv.DictWriter(csv_file,fieldnames=['Den_Number','Pokemon_ID','Rarity','Ability'])
    writer.writeheader()
    for den_number in range(1,94):
        response = urlopen('https://www.serebii.net/swordshield/maxraidbattles/den{den_number}.shtml'.format(den_number=den_number))
        html_doc = response.read()
        # Parse the html file
        soup = BeautifulSoup(html_doc, 'lxml')
        name_box = soup.find('table', attrs={'class': 'trainer'})

        pkmn_id_list = find_pokemon_id(name_box)
        rarity_list,ability_list = find_pokemon_rarity_ability(name_box)
        for i in range(len(pkmn_id_list)):
            result_dictionary = {}
            result_dictionary['Den_Number'] = den_number
            result_dictionary['Pokemon_ID'] = pkmn_id_list[i]
            result_dictionary['Rarity'] = rarity_list[i]
            result_dictionary['Ability'] = ability_list[i]
            writer.writerow(result_dictionary)
        print(result_dictionary)
    csv_file.flush()


# pkmn_id_list = find_pokemon_id(name_box)
# rarity_list,ability_list = find_pokemon_rarity_ability(name_box)
# clean_representation(pkmn_id_list,rarity_list,ability_list)
write_to_csv(csv_file_path='read_serebii/den_information.csv')
# write_to_csv(85,pkmn_id_list,rarity_and_ability_list[0],rarity_and_ability_list[1],csv_file_path = 'read_serebii/den_information.csv')

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