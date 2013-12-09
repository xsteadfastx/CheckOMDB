import requests


class CheckOMDB:
        def __init__(self, FilmName):
                self.FilmName = FilmName

        def GetFilmInfo(self):
                url = 'http://www.omdbapi.com/?t=%s' % self.FilmName
                FilmInfo = requests.get(url)
                data = FilmInfo.json()
                return data

        def GetFilmPlot(self):
                return self.GetFilmInfo()['Plot']

        def GetFilmActors(self):
                return self.GetFilmInfo()['Actors']

        def GetFilmYear(self):
                return self.GetFilmInfo()['Year']

if __name__ == "__main__":
        marie = CheckOMDB('Marie Antoinette')
        print marie.GetFilmPlot()
