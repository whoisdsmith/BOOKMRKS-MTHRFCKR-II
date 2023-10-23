import requests
from bs4 import BeautifulSoup
import re
import logging

# Setup logging
logging.basicConfig(filename='script.log', level=logging.INFO)

def fetch_title_and_description(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.title.string if soup.title else ''
        description = soup.find('meta', attrs={'name': 'description'})
        description = description['content'] if description else ''
        return title.strip(), description.strip()
    except Exception as e:
        logging.warning(f"Could not fetch data for {url}: {e}")
        return '', ''

def process_line(line):
    # Find Markdown links with URL as title
    pattern = r'\[(https?://[^\]]+)\]\((https?://[^\)]+)\)'
    matches = re.findall(pattern, line)
    
    for match in matches:
        title, description = fetch_title_and_description(match[0])
        if title:
            line = line.replace(match[0], title)
            line = line.replace(match[1], f"{match[1]} - {description}") if description else line
            
    return line

def main():
    try:
        with open("C:\\Users\\whois\\Documents\\BOOKMRKS-MTHRFCKR-II\\MTHRFCKRII.md", 'r', encoding='utf-8') as infile:
            with open("MTHRFCKR2.md", 'w', encoding='utf-8') as outfile:
                for line in infile:
                    logging.info(f"Processing line: {line.strip()}")
                    processed_line = process_line(line)
                    outfile.write(processed_line)
        logging.info("Finished processing the file.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
