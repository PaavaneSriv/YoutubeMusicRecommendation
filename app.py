import streamlit as st
import pandas as pd
import joblib 

# Setting web page
st.set_page_config(
    page_title="Youtube Music Recommendation",
    page_icon=":musical_note:",
    layout="wide",
    initial_sidebar_state="auto")


st.title("🎵 Youtube Music Recommendation")
st.write("Search the song or choose a song from the list")
#st.write("This system will recommend you hindi/multilanguage/Engligh songs based on your preferences \n\n " \
#"Note: This sytem will only recommemd songs of India (Multilanguage indian songs) and very few english songs.")

# Load model and data
df = pd.read_csv("cleanedata.csv")
tfidf_vectorizer = joblib.load("tfidf_vectorizer.pkl")
sigmoid = joblib.load("sigmoid.pkl")

# Tip: Always Reset Index Before Using Position-Based Access
df = df.reset_index(drop=True)

# Creating a series for the preproccessed song column
indi = pd.Series(df.index, index=df['song_clean']).drop_duplicates()


def recommendation(name, sig=sigmoid):
    # This retrieves the row number corresponding to the song name.  eg: indi['weeknd starboy ft daft punk official video']
    index = indi[name]
    # Get Similarity Scores for That Song
    sigmoid_scores = list(enumerate(sig[index]))
    # Sorts the list of songs in descending order of similarity score.
    sigmoid_scores = sorted(sigmoid_scores, key=lambda x: x[1], reverse=True)
    # Pick Top 10 Most Similar Songs (Excluding Itself)
    sigmoid_scores = sigmoid_scores[1:11]
    # Extract the Index Values of These Songs
    song_indices = [i[0] for i in sigmoid_scores]
    # Returns the top 10 most similar song titles as output.
    return df['song_clean'].iloc[song_indices]

music_list = df["song_clean"].to_list()

#User input (manual entry)
search_input = st.text_input("Enter a song name:")


# Or dropdown selection
selected_song = st.selectbox("Or select a song from the list:", [""] + music_list)

# Determine which input to use ---
input_song = search_input.strip() if search_input.strip() else selected_song
st.caption("click the button")

if st.button("Recommend Song"):
    if input_song:
        st.subheader(f"🎧Top 10 Recommendation for '{input_song}'", divider = True)
        if input_song in music_list:
                recommendations = recommendation(input_song)
                cols = st.columns(10)
                for i, song in enumerate(recommendations):
                    with cols[i]:
                        st.write(song)
        else:
            st.warning("❌ Song not available / recommendation not available.")
    else:
        st.info("Please enter or select a song to get recommendations.")

st.divider()
st.caption("This system will recommend you hindi/multilanguage/Engligh songs based on your preferences")
st.caption("Note: This sytem will only recommemd songs of India (Multilanguage indian songs) and very few english songs.")


# random trial and error
 #st.subheader(f"🎧Top 10 Recommendation'{selected_song}'", divider = True)
 #st.success(f"🎧 Top 10 Recommendations for '{input_song}' ")