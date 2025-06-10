import os
import json
import pandas as pd
import numpy as np

def remove_outliers(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    df_out = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
    return df_out

def show_statistics_with_outliers(folder_path):
    file_names = [f for f in os.listdir(folder_path) if f.endswith('.json') and '_features' in f]
    all_data = []

    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Extracting only the desired keys from the data
        extracted_data = {key: data[key] for key in [
            'danceability', 'energy', 'key', 'loudness', 'mode', 
            'speechiness', 'acousticness', 'instrumentalness', 
            'liveness', 'valence', 'tempo', 'time_signature']}
        
        all_data.append(extracted_data)

    # Convert the list of dictionaries to DataFrame
    all_data = pd.DataFrame(all_data)
    
    # Ensure the values are numeric
    all_data = all_data.apply(pd.to_numeric, errors='coerce')
    
    # Drop rows with NaN values if any
    all_data = all_data.dropna()
    
    stats = all_data.describe().transpose()[['mean', 'min', 'max']]
    stats['median'] = all_data.median()
    
    # Rearrange the columns to be in the order: mean, median, max, min
    stats = stats[['mean', 'median', 'max', 'min']]
    
    print("\nStatistics with outliers:")
    print(stats)

def show_statistics_without_outliers(folder_path):
    file_names = [f for f in os.listdir(folder_path) if f.endswith('.json') and '_features' in f]
    all_data = []

    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Extracting only the desired keys from the data
        extracted_data = {key: data[key] for key in [
            'danceability', 'energy', 'key', 'loudness', 'mode', 
            'speechiness', 'acousticness', 'instrumentalness', 
            'liveness', 'valence', 'tempo', 'time_signature']}
        
        all_data.append(extracted_data)

    # Convert the list of dictionaries to DataFrame
    all_data = pd.DataFrame(all_data)
    
    # Ensure the values are numeric
    all_data = all_data.apply(pd.to_numeric, errors='coerce')
    
    # Drop rows with NaN values if any
    all_data = all_data.dropna()
    
    # Remove outliers
    all_data = remove_outliers(all_data)
    
    stats = all_data.describe().transpose()[['mean', 'min', 'max']]
    stats['median'] = all_data.median()
    
    # Rearrange the columns to be in the order: mean, median, max, min
    stats = stats[['mean', 'median', 'max', 'min']]
    
    print("\nStatistics without outliers:")
    print(stats)

def print_simple_statistics(folder_path):
    file_names = [f for f in os.listdir(folder_path) if f.endswith('.json') and '_features' in f]
    all_data = { 
        'danceability': [],
        'energy': [],
        'key': [],
        'loudness': [],
        'mode': [],
        'speechiness': [],
        'acousticness': [],
        'instrumentalness': [],
        'liveness': [],
        'valence': [],
        'tempo': []
    }

    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        for feature in all_data.keys():
            all_data[feature].append(data[feature])
    
    print("\nSimple statistics:")
    for feature, values in all_data.items():
        values = np.array(values)
        mean_value = np.mean(values)
        min_value = np.min(values)
        max_value = np.max(values)

        print(f'\nStatistics for {feature}:')
        print(f'    Mean: {mean_value:.2f}')
        print(f'    Min: {min_value:.2f}')
        print(f'    Max: {max_value:.2f}')

if __name__ == "__main__":
    # Replace with your folder path
    folder_path = '/path/to/your/SONG_DATA'
    
    show_statistics_with_outliers(folder_path)
    show_statistics_without_outliers(folder_path)
    print_simple_statistics(folder_path) 