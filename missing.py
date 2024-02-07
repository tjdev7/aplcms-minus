import requests
from bs4 import BeautifulSoup
import os

def url_exists_locally(url):
    # Extract filename from URL
    filename = url.split('/')[-1]
    # Check if filename exists locally
    return os.path.exists(filename)

def fetch_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def extract_image_urls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')
    image_urls = [tag['src'] for tag in img_tags if 'src' in tag.attrs]
    return image_urls

def main():
    base_url = 'http://aplcms-minus.ddev.site'
    html_content = fetch_html_content(base_url)
    if html_content:
        image_urls = extract_image_urls(html_content)
        # Check image URLs for missing images and log them
        missing_images = [url for url in image_urls if not url_exists_locally(url)]
        if missing_images:
            print("Missing images:")
            for url in missing_images:
                print(url)
        else:
            print("No missing images found.")
    else:
        print("Failed to fetch HTML content from the local DDEV website.")

if __name__ == "__main__":
    main()
