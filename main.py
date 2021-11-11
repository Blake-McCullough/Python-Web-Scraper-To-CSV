#Made By Blake McCullough
#Discord- Spoiled_Kitten#4911
#Github- https://github.com/Blake-McCullough/




#To help with creating with CSV files
import csv

#For the actual web scraping
import requests
from bs4 import BeautifulSoup

# import pandas with shortcut 'pd'
import pandas as pd  

#Helps to break up the command terminal for easier reading
def BreakText():
  print('------------------------')

#Scrapes table on given url and puts it into a csv
def scrape_data(url):
#Lets user know of actions occuring
    print("Scraping data from",url)
#Gets site from URL
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
#FInds any tables
    table = soup.find_all('table')[0]
#gets data
    rows = table.select('tbody > tr')
#Identifies for a header
    header = [th.text.rstrip() for th in rows[0].find_all('th')]
#Saves found data to 'output.csv'
    with open('output.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for row in rows[0:]:
            data = [th.text.rstrip() for th in row.find_all('td')]
            writer.writerow(data)
    #Lets user know of actions occuring
    print("Saved to output.csv")
    BreakText()


#removes a column with matching header value
def Column_Remove(filename,column_Value):
  #Lets user know of actions occuring
    print("Removing column with:",column_Value,"\nFrom: ",filename)
  # read_csv function which is used to read the required CSV file
    data = pd.read_csv(filename,header=0)
    # pop function which is used in removing or deleting columns from the CSV files
    data.pop(column_Value)
    #Saves the file with column removed to 'column-removed.csv'
    data.to_csv("column-removed.csv", index=False)
    #Lets user know of actions occuring
    print("\nSuccessfully removed column:",column_Value,"\nFrom:",filename)
    BreakText()

#Adds header if not there already (manual check needed)
def Add_Header(filename,headers):
  #Lets user know of actions occuring
  print("Adding headers: \n",headers,"\nTo",filename)
  # read_csv function which is used to read the required CSV file
  file = pd.read_csv(filename,header=None)
  #Sets headers to be added from variable
  headerList = headers
  #Sets
  file.to_csv("header-added.csv", header=headerList, index=False)
  #Lets user know of actions occuring
  print("\nSuccesfully added headers: \n",headers,"\nTo",filename)
  BreakText()


#scrape_data(url)
url = "https://vrmasterleague.com/EchoArena/Standings/2NluW_UsAmhquDWQX-CfFg2"
scrape_data(url)



#Add_Header(filename,headerlist)
filename="output.csv"
headerList = ['POS','DIV','TEAM','GP','WIN','LOSS','PTS','MMR' ]
Add_Header(filename,headerList)


#Column_Remove(filename,columnremove)
filename="header-added.csv"
columnremove = "DIV"
Column_Remove(filename,columnremove)
