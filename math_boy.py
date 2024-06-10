#__author__ = 'Susan Davis, sed2001@ad.unc.edu, Onyen=sed2001'
# Ed Sheeran Sentiment Analysis

# Load Libraries
import pandas as pd
import string
import seaborn as sns
import matplotlib.pyplot as plt
import collections
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

# Load Data

ed = pd.read_csv('EdSheeran.csv')

# inspect the data
print(ed.head(30))

ed.info()

print(ed.Album.unique())

# remove non-stand alone albums

stand_alone = ['÷ (Divide)', '× (Multiply)', '+ (Plus)']

ed = ed.loc[ed['Album'].isin(stand_alone)]
print(ed.Album.unique())


# Convert the 'album_year' column to integers
ed['Year'] = ed['Year'].astype(int)
# Set options to display all columns
pd.set_option('display.max_columns', None)
print(ed.head(10))

# Clean the lyric text: lowercase everything, remove punctuation, exclude stop words

# Lowercase
ed['clean_lyric'] = ed['Lyric'].str.lower()


# Remove punctuation
ed['clean_lyric'] = ed['clean_lyric'].str.replace(r'[^\w\s]', '', regex=True)


# List of stop words (susan words)
stop = [
    'the', 'a', 'this', 'that', 'to', 'is', 'am', 'was', 'were', 'be', 'being', 'been', 'and',
    'or', 'but', 'if', 'then', 'else', 'when', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
    'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'from',
    'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once',
    'here', 'there', 'where', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some',
    'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't',
    'can', 'will', 'just', 'don', 'should', 'now', 'i', 'me', 'my', 'myself', 'we', 'our',
    'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his',
    'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their',
    'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'whose', 'why', 'how', 'an', 'do',
    'does', 'did', 'doing', 'has', 'have', 'had', 'having', 'are'
]

# list of stop words (package words)
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

#tokenize words (dont need to do this, since we did .lower above)
#clean_lyric = word_tokenize(lyric)


# Remove stop words (susan)
ed['clean_lyric'] = ed['clean_lyric'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop]))

#remove stop words (example)
clean_lyric = ed['clean_lyric']

for w in clean_lyric:
    if w not in stop_words:
        filtered_sentence.append(w)
 
print(word_tokens)
print(filtered_sentence)


# check that data was properly cleaned
print(ed.head(10))