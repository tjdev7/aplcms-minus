import requests
from bs4 import BeautifulSoup
import os
import sys

def create_local_path(url, local_base_path, base_url):
    # Adjust the URL to be relative if it's not already
    if url.startswith(('http://', 'https://')):
        url = url.split(base_url)[-1]
    local_path = os.path.join(local_base_path, url.lstrip('/'))
    return local_path

def url_exists_locally(url, local_base_path, base_url):
    local_path = create_local_path(url, local_base_path, base_url)
    return os.path.exists(local_path)

def fetch_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def extract_image_urls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')
    image_urls = [tag['src'] for tag in img_tags if 'src' in tag.attrs and not tag['src'].startswith(('http://', 'https://'))]
    return image_urls

def download_image(image_url, local_base_path, base_url, remote_base_url):
    # Use the remote base URL for downloading the image
    full_image_url = remote_base_url + image_url if not image_url.startswith(('http://', 'https://')) else image_url
    local_path = create_local_path(image_url, local_base_path, base_url)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    response = requests.get(full_image_url)
    if response.status_code == 200:
        with open(local_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded to {local_path}")
    else:
        print(f"Failed to download {full_image_url}")

def main():
    local_base_url = 'http://aplcms-minus.ddev.site'  # Default local base URL
    remote_base_url = 'https://library.austintexas.gov'  # Remote (production) base URL
    html_directory = './html'
    
    start_url_path = sys.argv[1] if len(sys.argv) > 1 else ''
    start_url = f"{local_base_url}/{start_url_path.lstrip('/')}" if start_url_path else local_base_url

    html_content = fetch_html_content(start_url)
    if html_content:
        image_urls = extract_image_urls(html_content)
        for url in image_urls:
            if not url_exists_locally(url, html_directory, local_base_url):
                download_image(url, html_directory, local_base_url, remote_base_url)
    else:
        print("Failed to fetch HTML content.")

if __name__ == "__main__":
    main()
