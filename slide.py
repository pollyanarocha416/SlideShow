class Slideshow:
    def __init__(self, slides):
        self.slides = slides
        self.atual = 1

    def verNovoSlide(self):
         self.atual += 1

    def play(self):
        while(self.atual <= self.slides):
            print('Slide', self.atual)
            self.verNovoSlide()

slide = Slideshow(5)
slide.play()