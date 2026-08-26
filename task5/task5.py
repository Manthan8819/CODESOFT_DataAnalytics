import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# --- PART 1: WEB SCRAPING ---
url = "http://books.toscrape.com/"
response = requests.get(url)

# Specify utf-8 encoding to handle currency symbols correctly
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
books = soup.find_all('article', class_='product_pod')

data = []

for book in books:
    title = book.h3.a['title']
    price_str = book.find('p', class_='price_color').text
    
    # Extract ONLY digits and dots (removes £, Â, $, etc.)
    price_clean = re.sub(r'[^\d.]', '', price_str)
    price = float(price_clean)
    
    rating_class = book.find('p', class_='star-rating')['class'][1]
    
    data.append({
        'Title': title,
        'Price': price,
        'Rating': rating_class
    })

# --- PART 2: DATA CLEANING & EXPORT ---
df = pd.DataFrame(data)

rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['RatingNumeric'] = df['Rating'].map(rating_map)

df.to_csv('extracted_books.csv', index=False)
print("Data successfully scraped and saved to 'extracted_books.csv'!\n")
print(df.head())

# --- PART 3: EXPLORATORY DATA ANALYSIS & VISUALIZATION ---
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Price Distribution
sns.histplot(df['Price'], kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('Distribution of Book Prices')
axes[0].set_xlabel('Price (£)')

# Plot 2: Average Price by Rating
sns.barplot(data=df, x='RatingNumeric', y='Price', ax=axes[1], palette='crest')
axes[1].set_title('Average Price by Star Rating')
axes[1].set_xlabel('Star Rating (1 to 5)')
axes[1].set_ylabel('Average Price (£)')

plt.tight_layout()
plt.show()
