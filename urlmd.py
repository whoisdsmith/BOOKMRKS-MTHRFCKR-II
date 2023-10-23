import requests
import re
import logging
import concurrent.futures
import time
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(filename='urlmd.log', level=logging.INFO, format='%(asctime)s - %(message)s')

session = requests.Session()
retry_after_time = 1  # In seconds

def extract_links_from_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'\[.*?\]\((https?://[^\s\)]+)\)'
    links = re.findall(pattern, content)
    return links

def fetch_title_and_description(url):
    global retry_after_time

    time.sleep(retry_after_time)
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = session.get(url, headers=headers, timeout=10, verify=False)
        
        if response.status_code == 429:
            retry_after = int(response.headers.get('Retry-After', 15))
            retry_after_time = max(retry_after_time, retry_after)
            logging.warning(f"Rate limited for {url}. Retrying after {retry_after} seconds.")
            return None
        
        elif response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string.strip() if soup.title else 'No title'
            description = soup.find('meta', attrs={'name':'description'})['content'].strip() if soup.find('meta', attrs={'name':'description'}) else 'No description'
            logging.info(f"Successfully fetched {url}")
            return f"- [{title}]({url}) - {description}\n"
        
        else:
            logging.warning(f"Failed to fetch {url}, status code: {response.status_code}")
            return None
    
    except requests.exceptions.SSLError:
        logging.error(f"SSL error occurred for {url}")
        return None
    except requests.exceptions.Timeout:
        logging.error(f"Timeout occurred for {url}")
        return None
    except Exception as e:
        logging.error(f"An error occurred for {url}: {e}")
        return None

if __name__ == "__main__":
    file_path = "Advanced Searching.md"
    output_file_path = "url.md"

    links = extract_links_from_md_file(file_path)
    results = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_title_and_description, links))

    results = [res for res in results if res is not None]

    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.writelines(results)

    print("Titles and descriptions have been saved to url.md and logs have been written to urlmd.log.")
