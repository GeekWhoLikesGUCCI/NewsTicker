import tkinter as tk
import requests
import json

def get_news():
    # Making an API request to retrieve news data
    response = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2023-01-10&sortBy=publishedAt&apiKey=7e9b91244534418e92673ea66e04e249')
    # Parsing the JSON data
    data = json.loads(response.text)
    # Extracting headlines from data
    headlines = [article['title'] for article in data['articles']]

    return headlines

def get_stocks():
    # Make an API request to retrieve stock data
    response = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=AAPL&apikey=XZH8B4H6XV70S6CQ')
    # my API key is XZH8B4H6XV70S6CQ
    data = json.loads(response.text)
    # Extracting stock data
    stock_info = f"AAPL: ${data['Global Quote']['05. price']} ({data['Global Quote']['09. change']}%)"
   
    return stock_info

def update_news(label, index):
    headlines = get_news()
    stocks = get_stocks()
    if index >= len(headlines):
        index = 0
    label.config(text=f"{headlines[index]} | \n{stocks}")
    root.after(5000, lambda: update_news(label, index + 1)) #change first number to chage time of updates

root = tk.Tk()
root.title('News Ticker')

label = tk.Label(root, text='Loading news...', font=("Helvetica", 16))
label.pack(fill="x")

update_news(label, 0)

root.mainloop()