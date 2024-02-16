import requests
import json

def download_manifest(api_key):
    manifest_url = 'http://www.bungie.net/Platform/Destiny2/Manifest/'
    headers = {
        'X-API-Key': api_key
    }

    try:
        response = requests.get(manifest_url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        manifest_data = response.json()
        print(manifest_data['Response']['jsonWorldComponentContentPaths']['en'])

        for tablename, url, in manifest_data['Response']['jsonWorldComponentContentPaths']['en'].items():
            # Extract the manifest URL from the response
            manifest_json_url = 'http://www.bungie.net' + url

            # Download the manifest JSON
            response = requests.get(manifest_json_url, headers=headers)
            response.raise_for_status()

            # Save the manifest JSON to a file
            with open(f'{tablename}.json', 'w') as f:
                json.dump(response.json(), f, indent=4)
            
            print(f"{tablename}.json downloaded successfully and saved as "+ f"{tablename}.json")

    except requests.exceptions.RequestException as e:
        print("Error downloading manifest:", e)

# Replace 'YOUR_API_KEY' with your actual Bungie API key
api_key = '14e8991258cb40dbb21198e66f69edbe'
download_manifest(api_key)