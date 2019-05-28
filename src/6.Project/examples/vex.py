"""
In this example I will get the top ten robotics team for a given city by using the REST API vexdb.io. I will rank
the teams by the number of awards they have gotten.
ex)
    Team 1145 - 24 Awards
    Team 2344 - 15 Awards
    Team 3333 - 17 Awards
"""
# Import requests so that we can access the internet
import requests


# Create a class to store the data we care about
class Team:
    def __init__(self, number):
        self.number = number
        self.num_awards = 0

    def __str__(self):
        return 'Team Number: ' + str(self.number) + '\tTotal Awards: ' + str(self.num_awards)


# Creating a variable for the base URL is helpful
API_URL = 'http://api.vexdb.io/v1/'


def get_teams(city_name):
    """
    Get all of the teams for a given city. Will get the data located at https://api.vexdb.io/v1/get_teams and create
    Team objects that will hold the team number and name. Note that the data at that url does not contain the number
    of awards, that will have to be added later
    :param city_name: The name of the city to search in
    :return: A list of Team objects representing each team in the city
    """
    url_extension = 'get_teams'
    get_params = {'city': city_name}
    data = requests.get(API_URL + url_extension, params=get_params).json()['result']
    teams = []
    for team_info in data:
        team_number = team_info['number']
        team = Team(team_number)
        teams.append(team)
    return teams


def get_num_awards(team_number):
    """
    Get the number of awards for a given team. https://api.vexdb.io/v1/get_awards returns award data and the key 'size'
    represents the number of awards
    :param team_number: The team number to search through
    :return: A number representing the number of awards a team has won
    """
    url_extension = 'get_awards'
    get_params = {'team': team_number}
    data = requests.get(API_URL + url_extension, params=get_params).json()
    return data['size']


def main():
    # City name will be changed based on the city we want a ranking for
    city_name = 'Syracuse'
    teams = get_teams(city_name)
    # Add the number of awards to each team
    for team in teams:
        num_awards = get_num_awards(team.number)
        team.num_awards = num_awards

    # Sorting
    teams.sort(key=lambda data: data.num_awards, reverse=True)

    # Printing the teams ranked
    for team in teams:
        print(team)


if __name__ == '__main__':
    main()


