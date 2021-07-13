import requests
from pprint import PrettyPrinter
import json
from objects.Content import Content
from settings import APIKeys

pp = PrettyPrinter()

#API KEY FREE FROM  http://www.omdbapi.com/


#Convert to content
def toContent(response):
    contentjson = json.loads(response)
    new = Content()
    new.id = contentjson["imdbID"]
    new.source = "OMDB"
    new.title = contentjson["Title"]
    new.country = contentjson["Country"]
    new.director_name = contentjson["Director"]
    new.release_year = contentjson["Released"]
    new.sinopse = contentjson["Plot"]
    new.score = contentjson["imdbRating"]
    new.type = contentjson["Type"]

    return new


#Function to Integrated with OMDB
def search(title):
    #Fetch Movie Data with Full Plot
    data_URL = 'http://www.omdbapi.com/?apikey=' + APIKeys.apiKeyOMDB
    year = ''
    movie = title
    params = {
        't':movie,
        'type':'',
        'y':year,
        'plot':'full'
    }
    response = requests.get(data_URL,params=params).json()
    json_object = json.dumps(response, indent=4)
    return toContent(json_object)

