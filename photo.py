class Photo:
    def __init__(self, id ,orient, tagcount, tags):
        self._id = id # Unique id of the photo
        self._orient = orient # The photos orientation
        self._tagCnt = tagcount # The number of tags
        self._tags = tags # The tags associated with the photo

    def getID(self):
        """
        Returns unique id as an int
        """
        return self._id

    def getOrienType(self):
        """
        Returns the orientation type as a string.
        "V" or "H"
        """
        return self._orient

    def getTagCount(self):
        """
        Returns the number of tags associated to the photo as an int.
        """
        return self._tagCnt

    def getTags(self):
        """
        Returns a list of the tag names which are strings.
        """
        return self._tags


def main():
    photo = Photo(1, "H", 2, ["cat", "beach"])
    print("ID: ", photo.getID())
    print("Orientation Type: ",photo.getOrienType())
    print("Number of tags: ",photo.getTagCount())
    print("Tag names: ", photo.getTags())


if __name__ == main():
    main()