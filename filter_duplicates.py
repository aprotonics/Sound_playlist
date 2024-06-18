
titles = []
file = "tracks_titles/tracks_titles.txt"

with open(file=file, mode="rt", encoding="utf-8") as f:
    titles = f.readlines()

    titles_copy = titles.copy()
    titles = []

    for value in titles_copy:
        value = value.split(" \n")
        value = value[0]
        titles.append(value)

print(len(titles))

tracks_titles = []

for value in titles:
    if value not in tracks_titles:
        tracks_titles.append(value)

print(len(tracks_titles))

file = "tracks_titles_filtered.txt"

with open(file=file, mode="wt", encoding="utf-8") as f:
    titles = tracks_titles.copy()
    tracks_titles = []

    for value in titles:
        value = value + " \n"
        tracks_titles.append(value)
    
    f.writelines(tracks_titles)

tracks_titles = set()

for value in titles:
    tracks_titles.add(value)

print(len(tracks_titles))

file = "tracks_titles_filtered2.txt"

with open(file=file, mode="wt", encoding="utf-8") as f:
    titles = tracks_titles.copy()
    tracks_titles = []

    for value in titles:
        value = value + " \n"
        tracks_titles.append(value)
    
    f.writelines(tracks_titles)
