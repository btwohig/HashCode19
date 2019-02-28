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
        # 5 is just a dummy value
        return 5
    
    
def main():
    """ Mini test function. """
    
    ss = SlideShow()
    ss.add_slide("slideA")
    ss.add_slide("slideB")
    print(ss.get_slide_count(), "<- should be: 2")
    print(ss.calculate_total_interest_factor(), "<- should be: 5")
    

if __name__ == "__main__":
    main()
