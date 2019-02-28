from photo import *

class FileReader():

    def __init__(self, filename):
        self._fileName = filename
        self._Photos = []
        self._seqNumber = 1

    def readFile(self):
        file = open(self._fileName, "r")

        numSlides = int(file.readline())

        for line in file:
            photo = Photo()
            print(line)
            line = line.split()
            photo.setID(self._seqNumber)
            self._seqNumber += 1

            photo.setOrienType(line[0])
            photo.setTagCount(line[1])
            photo.setTags(line[2:])

            self._Photos.append(photo)

        return self._Photos




def main():
    file = FileReader("a_example.txt")
    photos = file.readFile()
    for photo in photos:
        print(photo.getID())

if __name__ == main():
    main()