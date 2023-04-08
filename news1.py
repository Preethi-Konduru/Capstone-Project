import requests
from bs4 import BeautifulSoup

from colorama import Fore
import pyfiglet as pf


def tech():

    print(Fore.LIGHTBLUE_EX + (pf.figlet_format("TECH  NEWS")))

    # Send a request to the BBC news website and get the response
    response = requests.get('https://www.bbc.com/news/technology')

    # Parse the response using BeautifulSoup
    doc = BeautifulSoup(response.text, 'html.parser')

    # Start with an empty list to store the stories
    stories_list = []

    # Find all the stories on the page
    stories = doc.find_all('div', {'class': 'gs-c-promo'})

    # Counter to keep track of the number of stories processed
    counter = 0

    # Loop through each story
    for story in stories:
        headline = story.find('h3')
        link = story.find('a')['href']
        full_link = "https://www.bbc.com" + link
        print(headline.text, '-', full_link)
        # summary = story.find('p')
        # if summary:
        #   print(summary.text)
        print("\n")

        # Increment the counter
        counter += 1

        # Break the loop if the counter reaches 5
        if counter == 8:
            break