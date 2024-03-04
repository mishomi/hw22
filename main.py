import json

with open('movies.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for page in data:
    for movie in page['results']:
        if movie['release_date'][:4] > '2000' and 'Crime' in movie['genres']:
            t = movie['genres'].index('Crime')
            movie['genres'][t] = 'New_Crime'

        if movie['release_date'][:4] <= '2000' and 'Drama' in movie['genres']:
            t = movie['genres'].index('Drama')
            movie['genres'][t] = 'Old_Drama'

        if movie['release_date'][:4] == '2000':
            movie['genres'].append('New_Century')

with open('movies.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
