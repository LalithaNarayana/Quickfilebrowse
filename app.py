from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        search_option = request.form['search_option']
        
        if search_option == 'images':
            image_results = search_images(query)
            return render_template('index.html', search_results=[], image_results=image_results)
        else:
            search_results = search_files(query, search_option)
            return render_template('index.html', search_results=search_results, image_results=[])
            
    return render_template('index.html', search_results=[], image_results=[])

def search_files(query, filetype):
    headers = {'User-Agent': '(Windows NT 11.0; Win64; x64) Chrome/126.0.6478.62'}
    
    if filetype == 'all_files':
        filetypes = ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx']
        search_url = f"https://www.google.com/search?q={query}+" + "+OR+".join([f"filetype:{ft}" for ft in filetypes])
    else:
        search_url = f"https://www.google.com/search?q={query}+filetype:{filetype}"
    
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    links = []
    valid_extensions = ('pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx')
    for link in soup.find_all('a', href=True):
        href = link['href']
        if "url?q=" in href and not "webcache" in href:
            url = href.split("url?q=")[1].split("&sa=U")[0]
            if len(url) > 135:
                continue  # Skip URLs longer than 135 characters
            if filetype == 'all_files':
                if url.lower().endswith(valid_extensions):
                    links.append(url)
            else:
                if url.lower().endswith(f'.{filetype}'):
                    links.append(url)    
    return links


def search_images(query):
    headers = {'User-Agent': '(Windows NT 10.0; Win64; x64) Chrome/126.0.6478.62'}
    search_url = f"https://www.google.com/search?tbm=isch&q={query}"
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    images = []
    for img in soup.find_all('img'):
        img_url = img.get('src')
        if img_url and img_url.startswith('http'):
            images.append(img_url)
    
    return images

if __name__ == '__main__':
    app.run(debug=True)