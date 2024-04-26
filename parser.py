import csv
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('animes.csv')
    # Assume the title is in a column named 'title'
    titles = df['title']

    # Write the titles to a text file
    with open('anime_titles.txt', 'w', encoding='utf-8') as f:
        for title in titles:
            try:
                f.write(title + '\n')
            except UnicodeEncodeError:
                print('Error writing title:', title)
