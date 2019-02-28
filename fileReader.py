from photo import *

class FileReader():

    def __init__(self, filename):
        self._fileName = filename
        self._Photos = []
        self._seqNumber = 1
        self._numSlides = 0

    def readFile(self):
        file = open(self._fileName, "r")

        numSlides = int(file.readline())
        self._numSlides = numSlides

        for line in file:
            photo = Photo()
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
    print(file._numSlides)
    #for photo in photos:
        #print(photo.getID())

if __name__ == main():
    main()