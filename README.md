# 🎵 YouTube Music Recommendation System

This project focuses on building a **Content-Based Music Recommendation System** using metadata scraped from YouTube music videos. The aim is to learn and apply real-world data cleaning, NLP, and recommendation system concepts from scratch using manually curated and preprocessed data.

## Project Objective
To create a **content-based recommendation system** that suggests similar songs based on the textual metadata of YouTube music videos, such as video titles and descriptions. This project was designed not only to build a working model but also to **gain hands-on experience in data scraping, data cleaning**.

## Dataset Description
The dataset contains information about various **Indian and English music videos** scraped from YouTube using the **YouTube Data API**. Music content includes multiple languages (Hindi, Tamil, Punjabi, Malayalam, English, Urdu, etc.) and genres (Ghazals, Sufi, Pop, Bollywood, Indie, etc.).

### Data Fields
1. Data set - youtube_music_dataset
- `Video ID`
- `Video Title`
- `Video Description`
- `Channel Title`
- `Channel ID`
- `Published Date`
- `View Count`
- `Like Count`
- `Comment Count`
- `Comments (Text)`       

    **Search Queries Used**
    
    Sample search queries to collect the data: old hindi songs", "kishore kumar songs", "sufi songs", "artist:atif aslam",
    "ghazals", "indipop songs 90s", "english songs", "coke studio", "punjabi songs", etc.

2. Data set - cleanedata.csv
- `clean_text`
- `song_clean`

## Data Limitations
While the dataset offers diverse musical content, it also comes with several limitations: -- Youtube_music_dataset.csv
1. Irrelevant Results:
   - Despite targeted search queries, some videos like trailers, live streams, jukeboxes, or playlists were included, which are not suitable for a song-based recommendation system.
2. Unstructured Descriptions:
   - YouTube video descriptions vary greatly across channels, making it difficult to consistently extract structured details like singer, composer, or genre.
3. Language Variance:
   - Texts are written in multiple languages (e.g., Hindi, Tamil, Malayalam, Urdu), which makes uniform preprocessing difficult, especially for NLP-based models trained on English text.
4. Limited Metadata Accuracy:
   - Metrics such as likes, views, or comments might not always reflect the actual popularity or quality of a song due to API limitations or restricted access.
5. Missing or Incomplete Data:
   - Some videos have missing descriptions, no comments, or comment counts set to zero, likely because comments were turned off or unavailable at the time of data scraping.
6. Shorts and Non-Music Content:
   - YouTube Shorts and non-music content (e.g., interviews or promos) occasionally appear in the dataset, requiring additional manual filtering.

## Features
- **Manual song search**: Type in a song name and get 10 recommendations.
- **Dropdown selection**: Choose a song from a list to get recommendations.
- Gracefully handles missing or unknown songs with user-friendly messages.
- Built with **Streamlit** for a clean and interactive UI.

## Tools and Libraries
1. Programming Language: Python
2. Libraries:
    - pandas
    - numpy
    - matplotlib
    - sigmoid_kernel
    - streamlit

## Working
 1. **Preprocessing**: 
     - YouTube video descriptions were extracted and cleaned (lowercased, punctuations removed, etc.).
     - Duplicate songs were removed.
     - Dataset was **manually refined** for consistency.
 2. **Vectorization**:
     - TF-IDF vectorizer was used on the cleaned song description text.
 3. **Similarity Calculation**:
     - Cosine similarity is calculated between songs based on their TF-IDF vectors.
 4. **Recommendation**:
     - The system returns top 10 most similar songs based on description similarity.


## Project Structure
``` bash
Youtube music-recommendation-system/
│
├── data/
│   └── youtube_music_dataset.csv # Raw data Scraped using API
|   └── cleanedata.csv
├── app.py                      # Streamlit app script
├── preprocessing.ipynb         # Preprocessing and feature engineering notebook
│
├── README.md                   # Project documentation
└── requirements.txt 
```
