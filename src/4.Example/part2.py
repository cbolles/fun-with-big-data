"""
Program that uses Coin Lore's REST API to collect data on cryptocurrency. Specifically the program looks at the
total volume in USD that the currency has. Basic statistics are displayed via stdout and optionally the data
can be viewed on a bar or pie graph

Usage:
    $ python3 part2.py -b -p #_max_coins

author: Collin Bolles
"""
import argparse
import requests
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

API_BASE_URL = 'https://api.coinlore.com/api/'
API_ALL_COIN_EXTENSION = 'tickers/'
API_COIN_MARKET_EXTENSION = 'coin/markets/'


class Coin:
    """
    Represents the information needed to represent the volume of a virtual coin in USD.
    args
        :param coin_id: The id related to the coin from the REST API
        :param name: The vernacular name of the coin
        :param volume_usd: The total amount of the coin in USD
    """
    __slots__ = ['coin_id', 'name', 'volume_usd']

    def __init__(self, coin_id, name, volume_usd):
        self.coin_id = coin_id
        self.name = name
        self.volume_usd = volume_usd


def get_coins(max_coins=25) -> list:
    """
    Get the coins from the REST API up to an including the max number passes in.
    not yet have the volume in usd set
    :param max_coins: The max number of coins to get information on
    :return: A list of Coin objects with the id, name, and volume in usd included
    """
    get_parameter = {'limit': max_coins}
    response_data = requests.get(API_BASE_URL + API_ALL_COIN_EXTENSION, get_parameter).json()
    coins = []
    for value in response_data['data']:
        coin_id = value['id']
        coin_name = value['name']
        coin_volume = float(value['market_cap_usd'])
        coins.append(Coin(coin_id, coin_name, coin_volume))
    return coins


def display_stats(coins: list) -> None:
    """
    Display some basic statistics on the coins to stdout. Show the average, max, min
    :param coins: List of coin objects to display stats
    :return: None
    """
    average_value = sum(coin.volume_usd for coin in coins) / len(coins)
    sorted_data = sorted(coins, key=lambda coin: coin.volume_usd)
    max_coin = sorted_data[-1]
    min_coin = sorted_data[0]
    print('Stats')
    print('=====')
    print('Total Number of Coins:', len(coins))
    print('Average volume in USD:', '${:,}'.format(average_value))
    print('Max Coin:', max_coin.name, 'Volume:', '${:,}'.format(max_coin.volume_usd))
    print('Min Coin:', min_coin.name, 'Volume:', '${:,}'.format(min_coin.volume_usd))


def show_pie_chart(coins: list) -> None:
    """
    Show a pie chart based on the total volume of the coin in USD. Based on the percentage of the volume of the given
    coin compared to total volume in USD
    :param coins: A list of coin objects to turn into a pie chart
    :return: None
    """
    labels = [coin.name for coin in coins]
    total_volume = sum(coin.volume_usd for coin in coins)
    sizes = [coin.volume_usd / total_volume for coin in coins]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax1.axis('equal')


def show_bar_graph(coins: list) -> None:
    """
    Show a bar graph based on the volume in USD for each coin. Each coin is represented by a bar graph
    :param coins: A list of coins to graph
    :return: None
    """
    formatter = FuncFormatter(lambda val, pos: '$%1.1fM' % (val * 1e-6))

    x = [i for i in range(0, len(coins))]
    volume = [coin.volume_usd for coin in coins]

    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(formatter)
    plt.bar(x, volume)
    plt.xticks(x, [coin.name for coin in coins], rotation='vertical')


def main():
    """
    Handles running the program. Parses the command line arguments and displays statistics based on the max number
    of coins passed in. The program then checks to see if the user requested any graphs to be displayed. Bar graphs
    and pie graphs can be generated
    :return: None
    """
    parser = argparse.ArgumentParser(description='Get information on the volume of different cryptocurrency')
    parser.add_argument('max_num', action='store', type=int, help='Number of cryptocurrencies to analyse')
    parser.add_argument('-b', '--bar', action='store_true', help='Flag to display bar graph')
    parser.add_argument('-p', '--pie', action='store_true', help='Flag to display pie graph')
    args = parser.parse_args()

    coins = get_coins(args.max_num)
    display_stats(coins)

    if args.pie:
        show_pie_chart(coins)
    if args.bar:
        show_bar_graph(coins)
    if args.pie or args.bar:
        plt.show()


if __name__ == '__main__':
    main()
