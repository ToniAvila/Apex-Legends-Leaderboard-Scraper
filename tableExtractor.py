from bs4 import BeautifulSoup
import requests
import pandas


# class which extracts data from table and forms a dataframe for ease of use
class scrapedTable:
    def __init__(self, leaderboardURL):
        self.url = leaderboardURL
        self.data = requests.get(self.url).text
        self.soup = BeautifulSoup(self.data, 'html.parser')
        self.table = self.soup.find('table', class_='trn-table')


    def createDataFrame(self):

        # creating a pandas data frame to store the important data
        df = pandas.DataFrame(columns=['Rank', 'Username', 'RP', 'Account Level'])


        # for all rows in the tables body
        for row in self.table.tbody.find_all('tr'):    
            # Find all data for each column

            # finding all data cells within each row
            columns = row.find_all('td')
    
            # if the columns are not empty
            if(columns != []):

                rank = columns[0].text.strip()

                # only want top 10 right now
                if rank == '11':
                    break

                user = columns[1].text.strip()

                # note: we skip index 2 because there's a placeholder "collapse" data cell

                rp = columns[3].text.strip()
                accLvl = columns[4].text.strip()

            df = df.append({'Rank': rank,  'Username': user, 'RP': rp, 'Account Level': accLvl}, ignore_index=True)

        df = df.style.set_table_styles([dict(selector='th', props=[('text-align', 'center')])])
        df.set_properties(**{'text-align': 'center'}).hide_index()
        

        return df