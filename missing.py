import requests
from bs4 import BeautifulSoup
import os

def create_local_path(url, local_base_path, remote_base_url):
    # Strip the remote base URL from the image URL to get the relative path
    if url.startswith(remote_base_url):
        relative_path = url[len(remote_base_url):]
    else:
        relative_path = url
    # Create full local path
    local_path = os.path.join(local_base_path, relative_path.lstrip('/'))
    return local_path

def url_exists_locally(url, local_base_path, remote_base_url):
    local_path = create_local_path(url, local_base_path, remote_base_url)
    return os.path.exists(local_path)

def fetch_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def extract_image_urls(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')
    image_urls = [base_url + tag['src'] if tag['src'].startswith('/') else tag['src'] 
                  for tag in img_tags if 'src' in tag.attrs]
    return image_urls

def download_image(image_url, local_base_path, remote_base_url):
    local_path = create_local_path(image_url, local_base_path, remote_base_url)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(local_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded to {local_path}")
    else:
        print(f"Failed to download {image_url}")

def main():
    local_base_url = 'http://aplcms-minus.ddev.site' # This is your local base URL, but it's not used in create_local_path directly
    remote_base_url = 'https://library.austintexas.gov'
    html_directory = './html'
    
    html_content = fetch_html_content(local_base_url)
    if html_content:
        image_urls = extract_image_urls(html_content, remote_base_url)
        # Check image URLs for missing images and download them
        for url in image_urls:
            if not url_exists_locally(url, html_directory, remote_base_url):
                download_image(url, html_directory, remote_base_url)
    else:
        print("Failed to fetch HTML content from the local DDEV website.")

if __name__ == "__main__":
    main()
