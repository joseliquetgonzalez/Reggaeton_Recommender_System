from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import pandas as pd

# Assuming you have a DataFrame df containing your 50 favorite songs and API metadata
df = pd.read_csv('seed_song_features_output.csv')
# Extract relevant features and create a feature matrix
feature_columns = ['tempo', 'key', 'energy']  # Add more features as needed
feature_matrix = df[feature_columns].values

# Normalize the feature matrix
scaler = StandardScaler()
normalized_feature_matrix = scaler.fit_transform(feature_matrix)

# Calculate cosine similarity
similarity_matrix = cosine_similarity(normalized_feature_matrix)

# Perform clustering (adjust the number of clusters as needed)
kmeans = KMeans(n_clusters=3, random_state=42)
cluster_labels = kmeans.fit_predict(normalized_feature_matrix)

# Add cluster labels to the DataFrame
df['cluster'] = cluster_labels

# Save the results to a CSV file
df.to_csv("seed_song_clustering.csv", index=False)
