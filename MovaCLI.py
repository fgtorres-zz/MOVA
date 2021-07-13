from Content import Content
import OMDBSource
import WatchModeSource

#Get a query of content
#query = input("Enter the content name: ")

query = "Family Guy"

contentOMDB = OMDBSource.search(query)

print("Title: ", contentOMDB.title)
print("Score OMDB:", contentOMDB.score)

data = WatchModeSource.search(contentOMDB.id)

print("Score WatchMode:", data.score)