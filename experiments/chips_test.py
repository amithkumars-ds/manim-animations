import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from manim import *
from chips import *

class ChipGallery(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        gates = VGroup(
            NotGate("NOT", in_label="A", out_label="A'").shift(LEFT*6+UP*2),
            AndGate("AND", in1_label="A", in2_label="B", out_label="AB").shift(LEFT*2+UP*2),
            OrGate("OR", in1_label="A", in2_label="B", out_label="A+B").shift(RIGHT*2+UP*2),
            XorGate("XOR", in1_label="A", in2_label="B", out_label="A^B").shift(RIGHT*6+UP*2),
            MuxGate(in1_label="A", in2_label="B", sel_label="S", out_label="Out").shift(LEFT*3+DOWN*2),
            DemuxGate(in_label="In", sel_label="S", out1_label="A", out2_label="B").shift(RIGHT*3+DOWN*2),
        )
        self.play(*[Create(g) for g in gates])
        self.wait(2)