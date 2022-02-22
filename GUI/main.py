import tkinter as tk 

# Perform HTTP requests
import requests  

# HTML Scraping
from bs4 import BeautifulSoup 

# Random
from random import choice

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

def filmSelect():
    global filmYear
    filmYear = choice(list(nFilms.keys()))
    print(filmYear)
    if filmYear == "2015-2017 List":
        return choice(list(nFilms["2015-2017 List"]))
    elif filmYear == "2018 List":
        return choice(list(nFilms["2018 List"]))
    elif filmYear == "2019 List":
        return choice(list(nFilms["2019 List"]))
    elif filmYear == "2020 List":
        return choice(list(nFilms["2020 List"]))
    elif filmYear == "2021 List":
        return choice(list(nFilms["2021 List"]))
    elif filmYear == "2022 List":
        return choice(list(nFilms["2022 List"]))

urls = ["https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(2015-2017)",
        "https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(2018)",
        "https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(2019)",
        "https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(2020)",
        "https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(2021)",
        "https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(since_2022)"]

def onClick():
    film = filmSelect()
    filmTxt.config(text=film)

root = tk.Tk()
root.title("WikiGet4NetflixGUI")
root.geometry("400x150+500+500")

introTxt = tk.Label(text="Welcome To The Random Netflix Original Selector")
filmTxt = tk.Label(text=f"Selected: ")

introTxt.pack()
filmTxt.pack()

selectBTN = tk.Button(
    text="New Selection",
    command=onClick)

exitBTN = tk.Button(
    text="Exit App",
    command=exit
    )

selectBTN.pack()
exitBTN.pack()

GetData(choice(urls))
SetData()

root.mainloop()