import os
import json
import matplotlib.pyplot as plt

def visualize_data(folder_path):
    # List all the JSON files in the given folder path with "_features" in the title
    file_names = [f for f in os.listdir(folder_path) if f.endswith('.json') and '_features' in f]

    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        
        # Load the JSON data from the file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Extract the data
        features = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
        values = [data[feature] for feature in features]

        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.barh(features, values)
        plt.xlabel('Values')
        plt.title(f'Audio Features of {file_name}')
        plt.xlim([0, 1])  # assuming all features are normalized between 0 and 1 (except some features)
        plt.show()

# Example usage
# Pass the folder path as argument to the function
visualize_data('/Users/walkerhutchinson/Desktop/SPOTIFY_STUFF/SONG_DATA')
