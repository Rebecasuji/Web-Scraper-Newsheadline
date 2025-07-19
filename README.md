# Web-Scraper-Newsheadline
# 📰 Web Scraper - News Headlines

This is a simple Python-based web scraper that automatically collects the **top news headlines** from [Google News](https://news.google.com/topstories?hl=en-GB&gl=GB&ceid=GB:en) and saves them to a `.txt` file. It's a lightweight script built using `requests` and `BeautifulSoup`, perfect for beginners exploring web scraping and data collection automation.

---

## ✅ Features

- Fetches live top news headlines from Google News
- Parses `<h2>` tags to extract article titles and links
- Saves results neatly in a local `headlines.txt` file
- Written in clean and readable Python with inline guidance
- Requires no JavaScript rendering (fast & lightweight)

---

## 🛠️ Tools & Technologies Used

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/)
- VS Code for development
- Git & GitHub for version control

---

## 🚀 How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/Rebecasuji/Web-Scraper-Newsheadline.git
cd Web-Scraper-Newsheadline
Install dependencies
pip install requests beautifulsoup4
To run
python news_scraper.py
SAMPLE  OUTPUT
India’s Space Program Reaches New Heights
https://news.google.com/articles/CBMiZWh0...

AI Revolutionizing Healthcare Sector
https://news.google.com/articles/CBMiYWh0...

---

### ✅ Next Step:
1. Save this as `README.md` in your project folder.
2. Then run:
```bash
git add README.md
git commit -m "Add README file"
git push
# #MINI GUIDE
Use requests for fetch html
use beautifulsoup to parse <h2>or title tags
save the titles in a.txt file##
