class Content:

    def __init__(self):
        self.id = ""

    #GETs
    def getid(self):
        return self.id

    def gettype(self):
        return self.type

    def gettitle(self):
        return self.title

    def getdirectorname(self):
        return self.director_name

    def getcountry(self):
        return self.country

    def getreleaseyear(self):
        return self.release_year

    def getsinopse(self):
        return self.sinopse

    def getscore(self):
        return self.score

    def getsource(self):
        return self.source

    #SETS
    def setid(self, id):
        self.id = id

    def settype(self, type):
        self.type = type

    def settitle(self, title):
        self.title = title

    def setdirectorname(self, director_name):
        self.director_name = director_name

    def setcountry(self, country):
        self.country = country

    def setreleaseyear(self,release_year):
        self.release_year = release_year

    def setsinopse(self,sinopse):
        self.sinopse = sinopse

    def setscore(self,score):
        self.score = score

    def setsource(self,source):
        self.source = source

    def toCSV(self):
        print(self.id,",",self.type,",",self.title,",",self.director_name,",",self.country,",", self.release_year,",",
        self.sinopse,",", self.score ,",", self.source)