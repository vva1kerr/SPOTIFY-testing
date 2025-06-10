import os
import json
import pandas as pd

def show_track_statistics(folder_path):
    file_names = [f for f in os.listdir(folder_path) if f.endswith('.json') and '_analysis' in f]
    all_data = []

    tags = {
        'track': [
            'offset_seconds', 'window_seconds', 'end_of_fade_in', 
            'start_of_fade_out', 'loudness', 'tempo', 'tempo_confidence',
            'time_signature', 'time_signature_confidence', 'key', 
            'key_confidence', 'mode', 'mode_confidence'
        ]
    }

    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Extracting only the desired keys from the data
        extracted_data = {}
        for key, tag_list in tags.items():
            for tag in tag_list:
                value = data.get(key, {}).get(tag)
                if value is not None:
                    extracted_data[f'{key}_{tag}'] = value

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

    print("\nTrack Analysis Statistics:")
    print(stats)

if __name__ == "__main__":
    # Replace with your folder path
    folder_path = '/path/to/your/SONG_DATA'
    show_track_statistics(folder_path) 