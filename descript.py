from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
import re
import logging
import time

# Setup logging
logging.basicConfig(filename='script.log', level=logging.INFO)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def fetch_description(url):
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')
        meta_tag = soup.find('meta', {'name': 'description'}) or \
                   soup.find('meta', {'property': 'og:description'})
        if meta_tag and 'content' in meta_tag.attrs:
            return meta_tag['content'].strip()
    except Exception as e:
        logging.warning(f"Could not fetch description for {url}: {e}")
    return ''

def process_line(line):
    urls = re.findall(r'\((https?://[^\)]+)\)', line)
    if not urls:
        return line

    descriptions = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for url, desc in zip(urls, executor.map(fetch_description, urls)):
            time.sleep(1)  # Respectful crawling by sleeping 1 second between requests
            if desc:
                descriptions.append((url, desc))

    new_line = line
    for url, description in descriptions:
        new_line = new_line.replace(url, f"{url} - {description}")

    return new_line

def main():
    try:
        input_file = "C:\\Users\\whois\\Documents\\BOOKMRKS-MTHRFCKR-II\\MTHRFCKR2.md"
        output_file = "MFII.md"
        
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:

            for line in infile:
                logging.info(f"Processing line: {line.strip()}")
                processed_line = process_line(line)
                outfile.write(processed_line)
        
        logging.info("Finished processing the file.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
