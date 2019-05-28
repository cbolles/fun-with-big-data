"""
In this example I will make a tool that will show the total number of pokemon of each type for each generation
of that type for example
    Normal: 30
    Flying: 24
    Fighting: 15
    ...
"""
# Import requests so we can access the internet
import requests


def main():
    # The value we will change depending on what generation we want to know about
    generation_number = 1
    # Get the general data about the generations using https://pokeapi.co/api/v2/generation/
    data = requests.get('https://pokeapi.co/api/v2/generation/' + str(generation_number)).json()

    # Pull out the different pokemon types and make a dictionary for the values
    """
    {
        "normal": 50,
        "flying": 30
    }
    """
    type_data = dict()
    for pokemon_type in data['types']:
        type_name = pokemon_type['name']
        if type_name not in type_data:
            type_data[type_name] = 0

    # Now lets get each pokemon for that generation
    pokemon = []
    for species in data['pokemon_species']:
        pokemon.append(species['name'])

    # We will make another call that will get us more information about the pokemon
    for species in pokemon:
        pokemon_data = requests.get('https://pokeapi.co/api/v2/pokemon/' + species).json()
        for pokemon_type in pokemon_data['types']:
            type_name = pokemon_type['type']['name']
            if type_name in type_data:
                type_data[type_name] += 1

    for pokemon_type in type_data:
        print('Type ' + pokemon_type + '\t\tNumber of Pokemon: ' + str(type_data[pokemon_type]))


if __name__ == '__main__':
    main()