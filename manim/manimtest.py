from manim import *
import numpy as np

class DrawCircle(Scene):
    def construct(self):
        unitCircle = Circle(color=RED, )
        ax = Axes()
        # ax = Axes([0, 5, 1],[-1,1,1])
        
        self.play(FadeIn(unitCircle, ax))
        self.wait(5)