# Reggaetón Recommender System
# by José E. Liquet y González

## Project Overview 
---
This project will be my final output of my journey through the [BrainStation](https://brainstation.io/)'s Data Science program. My main goal with this project is to build a song recommending system using my favorite genre, Reggaetón, as seed.

Currently, I have experienced that Spotify's recommending algorithm has become redundant: essentially pushing the same popular artists and songs, but nothing actually novel. My hope is to find a recommending system that picks songs of one liking and recommends similar songs that are novel, from small artists, and from a different genre altogether. In other words: I would love to have a recommender system that recommends you similar music but from outside of one's listening habits.

Although I am no expert, my aim with this project is to learn about recommendation systems and build one were I can find new songs that share song feature similarities with my selected Reggaetón songs. My ideal output are diverse songs that share sufficient similarities with Reggaetón without having to be exclusively Reggaetón. Furthermore, this code will be easily adaptable to other user's preferred music.

## Data Source
---
The seed song list that I made from selected Reggaetón songs for this project can be downloaded [here](https://github.com/joseliquetgonzalez/Reggaeton_Recommender_System/blob/main/Seed_song_list.csv).

As for the datasets to get songs recommended from, I used several public ones found in Kaggle: mainly the "[Spotify 1.2M+ Songs](https://www.kaggle.com/datasets/rodolfofigueroa/spotify-12m-songs)" and "[Spotify Dataset 1921-2020, 600k+ Tracks](https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks)", with occasional use of the "[Most Streamed Spotify Songs 2023](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023?resource=download)" dataset

## Data Breakdown
---
Overall, the files I work with contain Spotify's Web API "Tracks' Audio Features" metadata.  

I started my dataset by manually selecting the songs I liked, and copying the [URI code](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) from the Spotify Web Player. With the track's URI code I queried the track's audio features and saved them in the [Seed_song_features_output.csv](https://github.com/joseliquetgonzalez/Reggaeton_Recommender_System/blob/main/seed_song_features_output.csv) file.

Column breakdown of Seed_song_features_output.csv is as follows:

- **index:** Row index number for each individual song in the Seed_song_features_output.csv
- **danceability:**  Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
- **energy:**  Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
- **key:** The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1. 
- **loudness:** The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db.
- **mode:** Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.
- **speechiness:**  Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.
- **acousticness:**  A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
- **instrumentalness:** Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
- **liveness:** Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live. 
- **valence:** A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry). 
- **tempo:**  The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
- **type:**  The object type.
- **id:** The Spotify ID for the track.
- **uri:** The Spotify URI for the track.
- **track_href:** A link to the Web API endpoint providing full details of the track.
- **analysis_url:**  A URL to access the full audio analysis of this track. An access token is required to access this data.
- **duration_ms:**  The duration of the track in milliseconds.
- **time_signature:**  An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4".

| index | danceability | energy | key | loudness | mode | speechiness | acousticness | instrumentalness | liveness | valence | tempo  | type           | id                     | uri                                  | track_href                                               | analysis_url                                                     | duration_ms | time_signature |
|-------|--------------|--------|-----|----------|------|-------------|--------------|------------------|----------|---------|--------|----------------|------------------------|--------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|-------------|----------------|
| 0     | 0.82         | 0.788  | 6   | -5.478   | 0    | 0.191       | 0.272        | 1.65e-06         | 0.0404   | 0.648   | 93.961 | audio_features | 0tDSgSmZsbxCkdkfUPjg59 | spotify:track:0tDSgSmZsbxCkdkfUPjg59 | https://api.spotify.com/v1/tracks/0tDSgSmZsbxCkdkfUPjg59 | https://api.spotify.com/v1/audio-analysis/0tDSgSmZsbxCkdkfUPjg59 | 195573      | 4              |


## Steps to Complete 
---

- [x] Make GitHub repository
- [x] Find and generate datasets
- [x] Exploratory Data Analysis
- [X] Start clustering work between my songs and the dataset
- [ ] Try different distance methods and clustering algorithms
- [ ] Finalize recommendation system

## Ideas 
---

- [ ] Build Streamlit App for users to add their songs
- [ ] Write a blog post

