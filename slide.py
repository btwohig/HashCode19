from photo import *


class Slide:
    def __init__(self):
        self.photos = [] #array of photos in the slide
        self.photoCnt = 0  #number of photos in the slide
        self.tags = set()#set of the tags of current photo

    def add_photo(self, photo):
        self.photos += [photo]
        self.photoCnt += 1
        for e in photo.getTags():
            self.tags.add(e)

    def add_photos(self, photo1, photo2):
        self.photos += photo1, photo2
        self.photoCnt += len(self.photos)
        for e in photo1.getTags():
            self.tags.add(e)
        for e in photo2.getTags():
            self.tags.add(e)


    def get_photos(self):
        return self.photos

    def get_photoCnt(self):
        return self.photoCnt

    def get_tags(self):
        return self.tags


def main():
    slide = Slide()
    slide1 = Slide()
    photo1 = Photo(1, "H", 2, ["cat", "beach"])
    photo = Photo(2, "V", 2, ["cat", "beach"])
    photo3 = Photo(3, "V", 2, ["dog", "beach"])
    slide.add_photo(photo1)
    slide1.add_photos(photo, photo3)
    print(slide.photos[0].getID())
    print(slide.tags)
    print(slide.photoCnt)
    print(slide1.photos[0].getID())
    print(slide1.tags)
    print(slide1.photoCnt)


if __name__ == main():
    main()


