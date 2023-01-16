from manim import *
import numpy as np

class DrawGraph(Scene):
    def construct(self):
        
        # f = lambda t: 300 * np.exp(-0.12*t) - 300 * np.exp(-0.20*t)
        f = lambda t: 2*t
        
        graph = FunctionGraph(f)
        Camer
        
        self.add(graph)