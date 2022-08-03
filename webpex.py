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
        break

linkForAllRegions = url + linkConnection
urlPC = linkForAllRegions.replace('all', 'origin')
urlPSN = linkForAllRegions.replace('all', 'psn')
urlXBOX = linkForAllRegions.replace('all', 'xbl')

#region links, identified by 'country=' in string link
urlPC_US = urlPC
urlPC_JP = urlPC.replace('country=us', 'country=jp')
urlPC_All = urlPC.replace('country=us&', '')

urlPSN_US = urlPSN
urlPSN_JP = urlPSN.replace('country=us', 'country=jp')
urlPSN_All = urlPSN.replace('country=us&', '')

urlXBOX_US = urlXBOX
urlXBOX_JP = urlXBOX.replace('country=us', 'country=jp')
urlXBOX_All = urlXBOX.replace('country=us&', '')


def allLink():
    return [urlPC_All, urlPSN_All, urlXBOX_All]

def usLink():
    return [urlPC_US, urlPSN_US, urlXBOX_US]

def jpLink():
    return [urlPC_JP, urlPSN_JP, urlXBOX_JP]







