from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import pandas as pd

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

# Function to get artist and song information by track URI
def get_track_info_by_track_uri(token, track_uri):
    track_id = track_uri.split(':')[-1]
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = get_auth_header(token)

    result = get(url, headers=headers)

    try:
        json_result = json.loads(result.content)
        return json_result

    except json.decoder.JSONDecodeError:
        print(f"Error decoding JSON. Response content: {result.content}")
        return None

# Create a list to store the dictionaries of track information
track_info_list = []

def read_csv_and_extract_uris(file_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Assuming 'URI' is the name of the column containing URIs
    uri_column = 'URI'

    # Extract the URIs from the DataFrame and convert them to a list
    track_uris = df[uri_column].tolist()

    return track_uris


file_path = '../csv_files/Seed_song_list.csv'
track_uris = read_csv_and_extract_uris(file_path)

token = get_token()

for track_uri in track_uris:
    track_info = get_track_info_by_track_uri(token, track_uri)

    if track_info:
        # Extract artist names from the list of dictionaries
        artists = [artist['name'] for artist in track_info['artists']]
        track_info_list.append({'artists': artists, 'name': track_info['name']})
        print(f"Track Information for Track URI {track_uri} added to the list.")
    else:
        print(f"Failed to retrieve track information for Track URI {track_uri}.")

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(track_info_list)

# Save the DataFrame to a CSV file
df.to_csv("seed_artist_songname_output.csv", index_label="index")
print("DataFrame saved to seed_artist_songname_output.csv")
