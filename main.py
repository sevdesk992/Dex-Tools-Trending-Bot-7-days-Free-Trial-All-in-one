import csv
from os.path import exists
from upvote import Upvote
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver

NUMBER_OF_BOTS = 3 # The number of bots we create
VOTES_PER_BOT = 1  # The number of votes/accounts created per bot
PROJECT_URL = 'https://coinsniper.net/coin/62469' # The Coinsniper URL of the project you want to upvote
CAPTCHA_KEY = '35e531c4b62300ee3ea8a4102d56207e' # The API key for your Anti-Captcha account
PROXY_KEY = 'ynsh1e1ag12uelbzj8q14henifhlvnwq3ndizo4k' # The API key for your Proxy Webshare account

def initiate(bot : Upvote, proxy_idx : int):
    # Run the bot
    bot.activate(proxy_idx)

def main() -> None:
    # Check whether there is already a '.csv' file to append accounts to
    if not exists('coinsniper_accounts.csv'):
        # Otherwise create one and add a header to it
        with open('coinsniper_accounts.csv', 'w') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(['Email', 'Password'])
    with ThreadPoolExecutor(max_workers=NUMBER_OF_BOTS) as executor:
        executor.map(initiate, [Upvote(VOTES_PER_BOT, PROJECT_URL, CAPTCHA_KEY, PROXY_KEY) for _ in range(NUMBER_OF_BOTS)], [i * VOTES_PER_BOT for i in range(NUMBER_OF_BOTS) ])

if __name__ == "__main__":
    main()
