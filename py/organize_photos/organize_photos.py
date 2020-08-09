import os


def extract_place(filename):
    return filename.split("_")[1]


def organize_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    index = []
    for filename in originals:
        place = extract_place(filename)
        if place not in index:
            index.append(place)
            os.mkdir(place)
        os.rename(filename, os.path.join(place, filename))
    print(os.listdir())


#  organize_photos("Photos")
print("Test!")
