from bs4 import BeautifulSoup
import requests
import pandas
from tableExtractor import scrapedTable

# url from which i request data, from this link, we find the link connecting to leaderboard page
# and subsequently link to pages for separate platforms
url = 'https://apex.tracker.gg'
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')

# find all link elements, initialize empty list
linkToLeaderBoardAll = soup.findAll('a')
linkConnection = ''

# search for link which contains page of leaderboard with all plats
for link in linkToLeaderBoardAll:
    if 'all/RankScore' in link.get('href'):
        linkConnection = link.get('href')

# with link to leaderboard with all plats, we can form url's for other platforms (pc, psn, xbx)
def linkRet():
    linkAll = url + linkConnection
    return linkAll

linkForAllPlatform = url + linkConnection
urlPC = linkForAllPlatform.replace('all', 'origin')
urlPSN = linkForAllPlatform.replace('all', 'psn')
urlXBOX = linkForAllPlatform.replace('all', 'xbl')

print(urlPC, urlPSN, urlXBOX)

def allLinks():
    return [urlPC, urlPSN, urlXBOX]

pcTable = scrapedTable(urlPC)
psnTable = scrapedTable(urlPSN)
xboxTable = scrapedTable(urlXBOX)



# used this to find class identifiers of table. however, leaderboards page only has 1 table either way which makes it easier
#for table in soup.find_all('table'):
#    print(table.get('class'))

# finding table using its specifier
#table = soup.find('table', class_='trn-table')







