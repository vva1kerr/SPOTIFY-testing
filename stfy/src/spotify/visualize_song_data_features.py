import os
import json
import matplotlib.pyplot as plt

def create_feature_plot(data):
    """
    Create a horizontal bar plot of audio features.
    
    Args:
        data (dict): Audio features data from Spotify API
    """
    features = [
        'danceability', 'energy', 'key', 'loudness', 'mode',
        'speechiness', 'acousticness', 'instrumentalness',
        'liveness', 'valence', 'tempo'
    ]
    
    values = [data[feature] for feature in features]
    
    plt.figure(figsize=(10, 6))
    plt.barh(features, values)
    plt.xlabel('Values')
    plt.title('Audio Features')
    plt.xlim([0, 1])  # Most features are normalized between 0 and 1
    plt.tight_layout()
    plt.show()
