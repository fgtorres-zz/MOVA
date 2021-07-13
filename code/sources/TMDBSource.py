from pprint import PrettyPrinter
import json
import urllib.request
from code.objects.Content import Content
from code.settings import APIKeys

pp = PrettyPrinter()

#API KEY FREE FROM  https://developers.themoviedb.org/


#Convert to content
def toContent(response, type,imdbid):
    contentjson = response
    new = Content()
    new.id = imdbid
    new.source = "TMDB"
    try:
        new.title =  contentjson["original_name"]
    except KeyError:
        new.title = contentjson["original_title"]
        pass

    try:
        new.country = contentjson["origin_country"]
    except KeyError:
        new.country = ""
        pass

    new.director_name = ""

    try:
        new.release_year = contentjson["first_air_date"]
    except KeyError:
        new.release_year = ""
        pass

    new.sinopse = contentjson["overview"]
    new.score = contentjson["vote_average"]
    new.type = type

    return new


#Function to Integrated with OMDB
def search(imdbid):
    #Fetch Movie Data with Full Plot
    data_URL = 'https://api.themoviedb.org/3/find/' + imdbid +'?api_key=' + APIKeys.apiKeyTMDB + '&language=en-US&external_source=imdb_id'

    with urllib.request.urlopen(data_URL) as url:
        data = json.loads(url.read().decode())

    if len(data["tv_results"]) > 0:
        return toContent(data["tv_results"][0],"tv",imdbid)
    else:
        return toContent(data["movie_results"][0],"movie",imdbid)
