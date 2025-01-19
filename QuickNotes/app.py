from bs4 import BeautifulSoup
import requests


class base_parser:
    def __init__(self,url):
        html_code = requests.get(url).text
        self.soup = BeautifulSoup(html_code,'html.parser')
        

class Billionaires:
    def get_data(self):
        soup = base_parser('https://en.wikipedia.org/wiki/The_World%27s_Billionaires').soup
        data = soup.find('table',class_='wikitable sortable')
        tr = data.find_all('tr')
        names = []
        for i in tr[1:]:
            nm = i.find_all('td')[1]
            names.append(nm.text)
        return names
    
class populations:
    def get_data(self):
        soup = base_parser('https://en.wikipedia.org/wiki/World_population#Ten_most_populous_countries').soup
        data = soup.find('table',class_='sortable wikitable sticky-header static-row-numbers sort-under col1left col5left')
        tr = data.find_all('tr')
        names = []
        for i in tr[1:]:
            nm = i.find_all('td')[0]
            names.append(nm.text.replace('\xa0','').replace('\n',''))
        return names
    
class Tourism:
    def get_data(self):
        soup = base_parser('https://en.wikipedia.org/wiki/World_Tourism_rankings').soup
        
        data = soup.find('table',class_='wikitable sortable')
        tr = data.find_all('tr')
        names = []
        for i in tr[1:]:
            nm = i.find_all('td')[1]
            names.append(nm.text.replace('\xa0','').replace('\n',''))
        return names

class social_platforms:
    def get_data(self):
        soup = base_parser('https://en.wikipedia.org/wiki/List_of_social_platforms_with_at_least_100_million_active_users').soup
        data = soup.find('table',class_='wikitable sortable')
        tr = data.find_all('tr')
        names = []
        for i in tr[1:]:
            nm = i.find_all('td')[1]
            names.append(nm.text.replace('\xa0','').replace('\n',''))
        return names

class Expensive_Brands:
    def get_data(self):
        soup = base_parser('https://en.wikipedia.org/wiki/List_of_most_valuable_brands').soup
        data = soup.find('table',class_='wikitable sortable')
        tr = data.find_all('tr')
        names = []
        for i in tr[1:]:
            nm = i.find_all('td')[1]
            names.append(nm.text.replace('\xa0','').replace('\n',''))
        return names

class DangerousAnimals:
    def get_data(self):
        soup = base_parser('https://en.wikipedia.org/wiki/List_of_deadliest_animals_to_humans').soup
        data = soup.find('table',class_='wikitable')
        tr = data.find_all('tr')
        names = []
        for i in tr[1:]:
            nm = i.find_all('td')[1]
            names.append(nm.text.replace('\xa0','').replace('\n',''))
        return names


class WatchedMovies:
    def get_data(self):
        soup = base_parser('https://en.wikipedia.org/wiki/List_of_highest-grossing_films').soup
        data = soup.find('table',class_='wikitable sortable')
        tr = data.find_all('tr')
        names = []
        for i in tr[1:]:
            nm = i.find_all('td')[1]
            names.append(nm.text.replace('\xa0','').replace('\n',''))
        return names

class subscribed_YouTube_channels:
    def get_data(self):
        soup = base_parser('https://en.wikipedia.org/wiki/List_of_most-subscribed_YouTube_channels').soup
        data = soup.find('table',class_='sortable wikitable')
        tr = data.find_all('tr')
        names = []
        for i in tr[1:]:
            nm = i.find_all('td')[1]
            names.append(nm.text.replace('\xa0','').replace('\n',''))
        return names










