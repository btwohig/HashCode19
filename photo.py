class Photo:
    def __init__(self):
        self._id = None # Unique id of the photo
        self._orient = None # The photos orientation
        self._tagCnt = 0 # The number of tags
        self._tags = [] # The tags associated with the photo

    def getID(self):
        """
        Returns unique id as an int
        """
        return self._id

    def setID(self, id):
        self._id = id

    def getOrienType(self):
        """
        Returns the orientation type as a string.
        "V" or "H"
        """
        return self._orient

    def setOrienType(self, orienType):
        self._orient = orienType

    def getTagCount(self):
        """
        Returns the number of tags associated to the photo as an int.
        """
        return self._tagCnt

    def setTagCount(self, tagCount):
        self._tagCnt = tagCount

    def getTags(self):
        """
        Returns a list of the tag names which are strings.
        """
        return self._tags

    def setTags(self, tags):
        self._tags = tags


def main():
    photo = Photo()
    photo.setID(1)
    photo.setOrienType("H")
    photo.setTagCount(2)
    photo.setTags(["cat", "beach"])
    print("ID: ", photo.getID())
    print("Orientation Type: ",photo.getOrienType())
    print("Number of tags: ",photo.getTagCount())
    print("Tag names: ", photo.getTags())


if __name__ == main():
    main()