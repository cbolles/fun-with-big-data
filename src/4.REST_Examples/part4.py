import requests

API_URL = 'https://api.fantasy.nfl.com/v1'


def get_by_positions():
    """
    Makes a request to get all player stats, then sorts the players into a
    dictionary based on their position
    ex)
    {
        'def': ['Bob Smith', 'Kathy', 'Sam'],
        'K': ['Another guy'],
        ...
    }
    :return: A dictionary that matches the positions to all of the players that play it
    """
    # The bit of url after the main url that gets us stats on players
    url_extension = '/players/stats'
    # Information about what we want from the REST API
    get_parameters = {'statType': 'seasonStats', 'season': 2018, 'week': 1, 'format': 'json'}
    # Make request to get data
    data = requests.get(API_URL + url_extension, get_parameters).json()

    # Get the list of players from the JSON data
    player_list = data['players']
    # Create a dictionary to store the player data
    player_dict = dict()
    for player in player_list:
        # Team's do not have an esbid and we dont care about teams rn
        if player['esbid'] is not None:
            # Get the position of the player from JSON data
            player_position = player['position']
            # Get the name of the player from the JSON data
            player_name = player['name']
            # If the position has not been added to the player dictionary, create an empty list
            if player_position not in player_dict:
                player_dict[player_position] = []
            # Add the player under the specific position
            player_dict[player_position].append(player_name)
    return player_dict


def main():
    players = get_by_positions()
    for position in players:
        print(position)
        for player in players[position]:
            print('\t' + player)


if __name__ == '__main__':
    main()
