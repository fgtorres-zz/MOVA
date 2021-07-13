import urllib.request
import json
from code.objects.Content import Content
from code.settings import APIKeys


#API KEY FREE FROM  https://api.watchmode.com


#Convert to content
def toContent(response):
    contentjson = response
    new = Content()
    new.id = contentjson["imdb_id"]
    new.source = "WatchMode"
    new.title = contentjson["original_title"]
    new.country = ""
    new.director_name = ""
    new.release_year = contentjson["year"]
    new.sinopse = contentjson["plot_overview"]
    new.score = contentjson["user_rating"]
    new.type = contentjson["type"]

    return new


#Function to Integrated with OMDB
def search(imdbid):
    #Fetch Movie Data with Full Plot
    data_URL = 'https://api.watchmode.com/v1/search/?apiKey=' + APIKeys.apiKeyWatchMode + '&search_field=imdb_id&search_value=' + imdbid

    with urllib.request.urlopen(data_URL) as url:
        data = json.loads(url.read().decode())
        return searchDetails(data["title_results"][0]["id"])


def searchDetails(id):
    # Fetch Movie Data with Full Plot
    id = str(id)
    data_URL = 'https://api.watchmode.com/v1/title/' + id + '/details/?apiKey=' + APIKeys.apiKeyWatchMode
    with urllib.request.urlopen(data_URL) as url:
        data = json.loads(url.read().decode())
        return toContent(data)



