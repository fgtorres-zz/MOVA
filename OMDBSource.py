import requests
from pprint import PrettyPrinter
import json
from Content import Content

pp = PrettyPrinter()

#API KEY FREE FROM  http://www.omdbapi.com/
apiKey = ''

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

    return new


#Function to Integrated with OMDB
def search(title):
    #Fetch Movie Data with Full Plot
    data_URL = 'http://www.omdbapi.com/?apikey='+apiKey
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

