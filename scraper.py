import requests
from bs4 import BeautifulSoup

# Function to fetch the webpage content and parse it
def fetch_data(url):
    try:
        # Send a GET request to the website
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        else:
            print("Failed to retrieve data. Status code:", response.status_code)
    except Exception as e:
        print("Error fetching data:", e)

# Scrape article titles, links, and publication dates from TechCrunch homepage
def scrape_techcrunch(soup):
    articles = []
    for article in soup.find_all('article'):
        # Extract article title
        title = article.find('h2')
        # Extract article link
        link = article.find('a', href=True)['href'] if article.find('a') else None
        # Extract publication date
        pub_date = article.find('time')['datetime'] if article.find('time') else "No date available"
        
        if title and link:
            articles.append({
                'title': title.get_text(),
                'link': link,
                'date': pub_date
            })
    return articles

# Test the program
url = "https://techcrunch.com/"
soup = fetch_data(url)
if soup:
    articles = scrape_techcrunch(soup)
    
    # Presenting the data in a user-friendly format (command-line)
    for i, article in enumerate(articles, 1):
        print(f"{i}. {article['title']}")
        print(f"Link: {article['link']}")
        print(f"Published on: {article['date']}\n")
