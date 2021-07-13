from Content import Content
import OMDBSource

#Get a query of content
#query = input("Enter the content name: ")

query = "Family Guy"

contentOMDB = OMDBSource.search(query)

print("Title: ", contentOMDB.title)
print("Score OMDB:", contentOMDB.score)
