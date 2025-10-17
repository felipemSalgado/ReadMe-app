import requests

def search_book(title):
    url = 'https://openlibrary.org/search.json'
    params = {'title' : title}
    response = requests.get(url, params = params)

    results = []
    if response.status_code == 200:
        data = response.json()
        for book in data['docs'][:3]:
            title = book.get('title', 'Untitled')
            author = book.get('author_name', ['Author unknown'])[0]
            results.append({'title': title, 'author': author})
    else:
        results.append({'title' : f'Error : {response.status_code}', 'author' : ''})
    return results