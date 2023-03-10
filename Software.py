# Code by Andrew William Hill
# Software designed for RPi4 using a LCD News Ticker



#from rpi_lcd import LCD #MUST INSTALL pip install rpi_lcd feedparser TO WORK 
#from time import sleep 
#import feedparser 

# rssFeed stores the really simple syndication for our news feed
rssFeed = feedparser.parse("https://newsapi.org/v2/everything?q=tesla&from=2023-01-10&sortBy=publishedAt&apiKey=7e9b91244534418e92673ea66e04e249")
lcd = LCD()
sleep(1) #sleep one second

# I used a for loop to create 5 headlines
for i in range(5): #if you want more than one headline chage 5 to any number of headlines you want displayed 
    print(rssFeed['entries'][i]['title'])

def get_news():
    # Making an API request to retrieve news data
    response = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2023-01-10&sortBy=publishedAt&apiKey=7e9b91244534418e92673ea66e04e249')
    # Parsing the JSON data
    data = json.loads(response.text)
    # Extracting headlines from data
    headlines = [article['title'] for article in data['articles']]

    return headlines

split = textwrap.wrap(text, 16) #making the rssFeed only 16 characters length
lcd.text("Tom's Hardware", 1)
