import requests
from urllib.parse import urlparse
import os

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

url = input("Enter the file URL: ")

# Extract the filename from the URL
file_name = os.path.basename(urlparse(url).path)

# Use the current working directory and append 'files' folder
project_directory = os.getcwd()
files_directory = os.path.join(project_directory, 'files')
file_path = os.path.join(files_directory, file_name)

if not is_valid_url(url):
    print("Invalid URL. Please enter a valid URL.")
else:
    try:
        # Send a GET request to fetch the file
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check if the request was successful

        # Ensure the 'files' directory exists
        os.makedirs(files_directory, exist_ok=True)

        # Get the total file size from the response headers
        total_size = int(response.headers.get('content-length', 0))
        downloaded_size = 0

        # Write the file to disk in binary mode
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    downloaded_size += len(chunk)
                    progress = (downloaded_size / total_size) * 100
                    print(f"Download progress: {progress:.2f}%", end='\r')

        print(f"\nFile downloaded successfully as {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the file: {e}")
    except IOError as e:
        print(f"Error writing the file: {e}")