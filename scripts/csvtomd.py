import csv
import os

def format_tags(tags):
    formatted_tags = []
    for tag in tags.split(','):
        tag = tag.replace(" ", "")
        formatted_tags.append(f"#{tag}")
    return ' '.join(formatted_tags)

# Get the CSV file path from user input
csv_file_path = input("Please enter the path to the CSV file: ")

# Check if the file exists
if not os.path.exists(csv_file_path):
    print("The specified file does not exist.")
else:
    # Read the CSV file with UTF-8 encoding
    with open(csv_file_path, 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Strip any whitespace from field names
        csv_reader.fieldnames = [name.strip() for name in csv_reader.fieldnames]
        
        # Create a Markdown file with the same name and UTF-8 encoding
        md_file_path = os.path.splitext(csv_file_path)[0] + '.md'
        with open(md_file_path, 'w', encoding='utf-8') as md_file:
            
            # Loop through each row in the CSV
            for row in csv_reader:
                try:
                    cover = row['cover']
                    title = row['title']
                    url = row['url']
                    excerpt = row['excerpt']
                    created = row['created']
                    tags = format_tags(row['tags'])
                    
                    # Write to the Markdown file
                    md_file.write(f"![]({cover})\n\n")
                    md_file.write(f"[{title}]({url}) - {excerpt}\n\n")
                    md_file.write(f"Date: {created}\n\n")
                    md_file.write(f"{tags}\n\n")
                    md_file.write("---\n\n")
                except KeyError as e:
                    print(f"Missing column: {e}")

    print(f"Markdown file has been created at {md_file_path}.")
