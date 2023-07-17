import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import database

if __name__ == '__main__':
    Id = []
    title = []
    description = []
    price = []
    Type = []
    gen = ['women', 'men', 'ouds-studio', 'attar']
    for j in gen:
        for page in range(1, 5):
            url = f'https://scentsnstories.pk/collections/{j}?page={page}'
            try:
                r = requests.get(url)
                r.raise_for_status()

                soup = BeautifulSoup(r.text, 'lxml')

                item_meta = soup.find_all('div', class_="grid-item__meta")
                item_grid = soup.find_all('div', class_="grid-item grid-product")
                for i in range(1, len(item_grid)):
                    meta_main = item_meta[i].find('div', class_="grid-item__meta-main")
                    meta_secondary = item_meta[i].find('div', class_="grid-item__meta-secondary")
                    prod_id = item_grid[i].attrs['data-product-id']
                    prod_title = meta_main.div.text
                    prod_desc = meta_main.h10.text
                    prod_price = re.sub(r'\D', '',
                                        meta_secondary.find('span', class_='grid-product__price--current').span.text)
                    Id.append(prod_id)
                    title.append(prod_title)
                    description.append(prod_desc)
                    price.append(int(prod_price))
                    Type.append(j)
            except requests.exceptions.RequestException as e:
                # continue
                print(f'An error occurred while making the request: {e}')

    df = pd.DataFrame()
    df['ID'] = Id
    df['Title'] = title
    df['Description'] = description
    df['Price'] = price
    df['Type'] = Type

    print(df.info())
    df.to_csv('ScentsNStories.csv', index=False)
    database.db_table(df)
