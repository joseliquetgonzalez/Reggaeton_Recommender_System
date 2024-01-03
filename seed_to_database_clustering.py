from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Assuming you have a DataFrame df containing your 50 favorite songs and API metadata
df = pd.read_csv('seed_song_features_output.csv')
# Extract relevant features and create a feature matrix
feature_columns = ['tempo', 'key', 'energy']  # Add more features as needed
feature_matrix = df[feature_columns].values

# Normalize the feature matrix
scaler = StandardScaler()
normalized_feature_matrix = scaler.fit_transform(feature_matrix)

# Assuming you have a DataFrame spotify_df containing the entire Spotify dataset
spotify_df = pd.read_csv('spotify-datasets/kaggle-yamaerenay-dataset/tracks.csv')
# Extract relevant features from the Spotify dataset
spotify_feature_matrix = spotify_df[feature_columns].values

# Normalize the Spotify feature matrix
normalized_spotify_feature_matrix = scaler.transform(spotify_feature_matrix)

# Calculate cosine similarity between your 50 songs and all songs in the Spotify dataset
similarity_matrix = cosine_similarity(normalized_feature_matrix, normalized_spotify_feature_matrix)

# Find the most similar songs from the Spotify dataset for each of your 50 songs
recommended_songs_indices = similarity_matrix.argmax(axis=1)

# Extract recommended songs from the Spotify dataset
recommended_songs = spotify_df.iloc[recommended_songs_indices]

# Save the recommended songs to a CSV file
recommended_songs.to_csv("seed_to_database_clustering_output.csv", index=False)
