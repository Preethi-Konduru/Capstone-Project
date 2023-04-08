import requests
from bs4 import BeautifulSoup
from colorama import Fore
import pyfiglet as pf


def news():

    print(Fore.YELLOW + (pf.figlet_format("TOP  NEWS")))

    # Send a request to the BBC news website and get the response
    response = requests.get('https://www.bbc.com/news')

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

    # Now that we're done, convert the list to a DataFrame and save it to a CSV file
    import pandas as pd
    df = pd.DataFrame(stories_list)
    df.to_csv("bbc.csv", index=False)


def sport():

    print(Fore.CYAN + (pf.figlet_format("SPORTS  NEWS")))

    url = "https://www.bbc.com/sport"

    # Send a request to the BBC news website and get the response
    response = requests.get(url)

    # Parse the response using BeautifulSoup
    doc = BeautifulSoup(response.text, 'html.parser')

    # Start with an empty list to store the stories
    stories_list = []

    # Find all the stories on the page
    stories = doc.find_all('div', {'class': 'ssrcss-1f3bvyz-Stack e1y4nx260'})

    # Counter to keep track of the number of stories processed
    M = 0

    # Loop through each story
    for story in stories:
        headline = story.find('span')
        link = story.find('a')['href']
        full_link = "https://www.bbc.com" + link
        print(headline.text, '-', full_link)
        # summary = story.find('p')
        # if summary:
        #   print(summary.text)
        print("\n")

        # Increment the counter
        M += 1

        # Break the loop if the counter reaches 5
        if M == 8:
            break

def business():

    print(Fore.LIGHTGREEN_EX + (pf.figlet_format("BUSINESS  NEWS")))

    response = requests.get('https://www.bbc.com/news/business')

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

