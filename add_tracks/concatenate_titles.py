
tracks_titles = []

for i in range(75, 1275, 25):
    titles_number = i

    file = f"tracks_titles/tracks_next_{titles_number}_titles.txt"

    with open(file=file, mode="rt", encoding="utf-8") as f:
        titles = f.readlines()

        titles_copy = titles.copy()
        titles = []

        for value in titles_copy:
            titles.append(value)

        tracks_titles.extend(titles)
    

file = "tracks_titles/tracks_titles.txt"

with open(file=file, mode="wt", encoding="utf-8") as f:
    f.writelines(tracks_titles)
