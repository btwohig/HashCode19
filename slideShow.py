class SlideShow(object):
    """ Class representing a slide show.
    
        Attributes:
            _slide_count: An int representing the number of slides in the slide
                          show.
            _slides: An array of Slide objects representing the slides in the
                     slide show.

    """
    _slide_count = 0
    _slides = []
    
    def add_slide(self, slide):
        """ Add a Slide object to this slide show.
        
            Args:
                slide: A Slide object representing a slide.
        
        """
        self._slides.append(slide)
        self._slide_count += 1
        
    def get_slide_count(self):
        """ Return the number of slides in the slide show instance.
        
            Returns:
                An int representing the number of slides in the slide show.
        
        """
        return self._slide_count
    
    def calculate_total_interest_factor(self):
        """ Calculate the sum of interest factors in this slide show.
        
            Look at two neighbouring slides in turn, calculate the interest
            factor, and add this to a total.
        
            Returns:
                An int representing the sum of interest factors between each
                neighbouring pair of slides.
        
        """
        total_interest_factor = 0
        
        for i in range(self._slide_count - 1):
            current_slide = self._slides[i]
            subsequent_slide = self._slides[i + 1]
            # This is the essence of our this code - TODO
            interest_factor = self.calculate_interest_factor(current_slide,
                                                             subsequent_slide)
            total_interest_factor += interest_factor
        
        return total_interest_factor
    
    def calculate_interest_factor(self, slide1, slide2):
        """ Determine how interesting two neighbouring slides are.
        
            Essentially the minimum of the following:
                Number of common tags between slide1 and slide2
                Number of tags in slide1 but not in slide2
                Number of tags in slide2 but not in slide1
        
            Returns:
                An int representing the interest factor.
        
        """
        
        # Get the tags that in common with both slides.
        common_tag = self.tags_in_common(slide1, slide2)
        
        # Get the tags that are unique to each slide.
        tags_in_slide1_only = self.tags_in_first_slide_only(slide1, slide2)
        tags_in_slide2_only = self.tags_in_first_slide_only(slide2, slide1)
        
        # Calculate interest factor for this pair of slides.
        interest_factor = min(len(common_tag), len(tags_in_slide1_only),
                              len(tags_in_slide2_only))
        
        return interest_factor
    
    def tags_in_common(self, slide1, slide2):
        """ Return the number of tags in common between two slides' tags. """
        
        tags_in_slide1 = slide1.get_tags()
        tags_in_slide2 = slide2.get_tags()
        
        return tags_in_slide2.intersection(tags_in_slide1)
    
    def tags_in_first_slide_only(self, slide1, slide2):
        """ Return the number of tags that are only in slide1. """
        
        tags_in_slide1 = slide1.get_tags()
        tags_in_slide2 = slide2.get_tags()
        
        return tags_in_slide1 - tags_in_slide2
    
    
class DummySlideA(object):
    """ Dummy Slide class for testing. """
    
    def get_tags(self):
        return {1, 3, 5, 7, 9}


class DummySlideB(object):
    """ Another Dummy Slide class for testing. """
    
    def get_tags(self):
        return {2, 4, 6, 7, 8, 9}

    
def main():
    """ Mini test function. """
    
    ss = SlideShow()
    ss.add_slide(DummySlideA())
    ss.add_slide(DummySlideB())
    print(ss.get_slide_count(), "<- should be: 2")
    print(ss.calculate_total_interest_factor(), "<- should be: 2")
    

if __name__ == "__main__":
    main()
