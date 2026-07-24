import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))  # adjust depth to reach chips.py's folder

from manim import *
from chips import *

class NOTCircuit(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        title = Text("Boolean Logic Proof for NOT Gate from Nand", font_size=22, weight=BOLD, color=BLACK, font="Arial").to_edge(UP)
        self.play(Write(title))

        # NOT is just a single NAND with both inputs tied to the same signal
        g1 = NandGate('Nand1', in1_label='A', in2_label='A', out_label="A'").shift(LEFT*1)

        self.play(Create(g1))

        # tie A to both inputs: fan-out wire from the in1 pin itself down to in2
        wire1 = right_angle_wire(g1.in1.get_start(), g1.in2.get_start(), color=BLACK)
        self.play(Create(wire1))


        nand1 = Text('Nand1: Nand(A, A)', font_size=16, weight=BOLD, color=BLACK, font="Arial").shift(RIGHT*4, UP*1)
        nand1_1 = Text("= (AA)' || Idempotent Law: x.x = x", font_size=15, slant=ITALIC, color=BLACK, font="Arial").next_to(nand1, DOWN, aligned_edge=LEFT, buff=0.15)
        nand1_2 = Text("= A' -- NOT Logic", font_size=16, color=BLACK, font="Arial").next_to(nand1_1, DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(Write(nand1))
        self.play(Write(nand1_1))
        self.play(Write(nand1_2))

        self.wait(2)


class NOTTruthTable(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        title = Text("NOT built from NAND — Truth Table Proof", font_size=32, color=BLACK).to_edge(UP)
        self.play(Write(title))

        headers = ["A", "NAND(A,A)", "NOT_from_NAND", "not A", "Match?"]
        rows = []
        for a in [0, 1]:
            na = int(Nand(a, a))
            computed = int(Nand(a, a))
            expected = int(not bool(a))
            rows.append([a, na, computed, expected, "✓" if computed == expected else "✗"])

        table = Table(
            [[str(x) for x in row] for row in rows],
            col_labels=[Text(h, font_size=24, color=BLACK) for h in headers],
        ).scale(0.6).next_to(title, DOWN, buff=0.5)

        table.get_entries().set_color(BLACK)
        table.get_col_labels().set_color(BLACK)

        self.play(Create(table))
        self.wait(2)