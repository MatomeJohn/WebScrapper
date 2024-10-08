from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Function to fetch and parse data from TechCrunch
def fetch_techcrunch_articles():
    url = "https://techcrunch.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    
    for article in soup.find_all('article'):
        title = article.find('h2')
        link = article.find('a', href=True)['href'] if article.find('a') else None
        pub_date = article.find('time')['datetime'] if article.find('time') else "No date available"
        
        if title and link:
            articles.append({
                'title': title.get_text(),
                'link': link,
                'date': pub_date
            })
    return articles

@app.route('/')
def home():
    articles = fetch_techcrunch_articles()
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
