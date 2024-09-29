# PDF Downloader

This project is a simple PDF downloader script written in Python. It allows you to download a PDF file from a given URL and save it to a specific folder within your project directory. The script also displays the download progress as a percentage.

## Features

- Validates the provided URL.
- Downloads the file from the URL.
- Saves the file in the `files` folder within the project directory.
- Displays the download progress as a percentage.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/devolutionary-wizard/pdf-downloader.git
   cd pdf-downloader
   ```

2. Install the required dependencies:
   ```sh
   pip install requests
   ```

## Usage

1. Run the script:

   ```sh
   python main.py
   ```

2. Enter the file URL when prompted.

## Example

```sh
Enter the file URL: https://harsh0620.github.io/PaperWrapper/Pdfs/selfdev/thich-nhat-hanh.pdf
Download progress: 50.00%
Download progress: 100.00%
```
