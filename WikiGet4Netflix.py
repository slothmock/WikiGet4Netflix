'''
WikiGet4Netflix - Created by Jordan Mock - 2022
Download from GitHub @ slothmock/WikiGet4Netflix
'''

# Perform HTTP requests
import requests  

# HTML Scraping
from bs4 import BeautifulSoup 

# Random
from random import choice

# Time
from time import sleep

urls = ["https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(2015-2017)",
        "https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(2018)",
        "https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(2019)",
        "https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(2020)",
        "https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(2021)",
        "https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(since_2022)"]


def GetData(url):
    # By default, Request will keep waiting for a response indefinitely. Therefore, set the timeout parameter.
    # If request was successful, reponse output == '200'.
    s = requests.Session()
    response = s.get(url, timeout=15)
    # Check we're getting a response
    print(response)

    # Parse response to HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Print title of Wikipedia page
    print(f"{soup.title.string}\n")

    # Get the table to scrape
    table=soup.find('table', {"class":'wikitable sortable'})

    # Number of columns in the table
    for row in table.findAll("tr"):
        cells = row.findAll('td')

    # Number of rows in the table
    rows = table.findAll("tr")

    lst_data = []
    for row in rows[2:]:
                data = [d.text.rstrip() for d in row.findAll('td')]
                lst_data.append(data)

    # HTML of each table row

    list_row = []
    for row in table.findAll("tr"):
        list_row.append(row)

    #Scrape the data and append to respective lists

    titles=[]

    for row in table.findAll("tr"):
        cells = row.findAll('td')
        if len(cells) == 5: #Only extract table body not heading
            titles.append(cells[0].find(text=True))

    return titles

# Test Print
#print(nFilms["2015-2017 List"][5])

def SetData():
    global nFilms
    nFilms = {
    "2015-2017 List" : GetData(urls[0]),
    "2018 List" : GetData(urls[1]),
    "2019 List" : GetData(urls[2]),
    "2020 List" : GetData(urls[3]),
    "2021 List" : GetData(urls[4]),
    "2022 List" : GetData(urls[5]),
    }

def Main():
    userHappy = 2
    while userHappy == 2:
        filmYear = choice(list(nFilms.keys()))
        print(filmYear)
        if filmYear == "2015-2017 List":
            print(choice(list(nFilms["2015-2017 List"])), "\n")
        elif filmYear == "2018 List":
            print(choice(list(nFilms["2018 List"])), "\n")
        elif filmYear == "2019 List":
            print(choice(list(nFilms["2019 List"])), "\n")
        elif filmYear == "2020 List":
            print(choice(list(nFilms["2020 List"])), "\n")
        elif filmYear == "2021 List":
            print(choice(list(nFilms["2021 List"])), "\n")
        elif filmYear == "2022 List":
            print(choice(list(nFilms["2022 List"])), "\n")
        try:
            userHappy = int(input("Are you happy with the selection? [1. Yes][2. No] > "))
        except ValueError as err:
            print(f"\n{err}\n")
            print("Mistakes were made. Try entering 1 or 2.")
            Main()
            
        Goodbye()

def Goodbye():
    print("Thanks for using this program!")
    sleep(1)
    quit()

if __name__ == "__main__":
    print('\nWelcome to the Random Netflix Original Selector!\n')
    SetData()
    Main()




















