import TMDBSource
from Content import Content
import OMDBSource
import WatchModeSource

#Get a query of content
#query = input("Enter the content name: ")

query = "Bad boys"

contentOMDB = OMDBSource.search(query)

print("Title: ", contentOMDB.title)
print("Score OMDB:", contentOMDB.score)

data = WatchModeSource.search(contentOMDB.id)

print("Score WatchMode:", data.score)

dataTMDB = TMDBSource.search(contentOMDB.id)

print("Score TMDB:", dataTMDB.score)