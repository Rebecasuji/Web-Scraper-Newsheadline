# ===============================
# 📰 Google News Headline Scraper
# ===============================
# Objective:
# Scrape top news headlines from Google News using requests and BeautifulSoup,
# parse <h3> or title tags, and save the titles into a text file (headlines.txt)

# ========== IMPORTS ==========
import requests
from bs4 import BeautifulSoup

# ========== STEP 1: FETCH THE HTML ==========
url = 'https://news.google.com/topstories?hl=en-GB&gl=GB&ceid=GB:en'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise error if status is not 200
except requests.RequestException as e:
    print("Failed to retrieve the page:", e)
    exit()

# ========== STEP 2: PARSE WITH BEAUTIFULSOUP ==========
soup = BeautifulSoup(response.text, 'html.parser')

# ========== STEP 3: FIND HEADLINE TAGS ==========
# Most Google News headlines are inside <h3> tags with anchor <a>
headlines = []
for h3 in soup.find_all('h3'):
    a_tag = h3.find('a')
    if a_tag:
        title = a_tag.get_text(strip=True)
        # Google News uses relative URLs, so prepend the base URL
        link = "https://news.google.com" + a_tag['href'][1:]  # remove '.' in ./articles/...
        headlines.append(f"{title}\n{link}\n")

# ========== STEP 4: SAVE TO TEXT FILE ==========
file_name = 'headlines.txt'
try:
    with open(file_name, 'w', encoding='utf-8') as f:
        for line in headlines:
            f.write(line + "\n")
    print(f"✅ {len(headlines)} headlines saved to {file_name}")
except IOError as e:
    print("Failed to write to file:", e)

# ========== MINI-GUIDANCE ==========
# 1. requests.get(url) - Fetches raw HTML
# 2. BeautifulSoup(response.text, 'html.parser') - Parses HTML content
# 3. soup.find_all('h3') - Finds headline tags
# 4. Save to headlines.txt with proper formatting
