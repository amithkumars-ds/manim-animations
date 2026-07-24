import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))  # adjust depth to reach chips.py's folder

from manim import *
from chips import *

class ANDCircuit(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        title = Text("Boolean Logic Proof for AND Gate from Nand", font_size=22, weight=BOLD, color=BLACK, font="Arial").to_edge(UP)
        self.play(Write(title))

        # instantiate 2 NAND gates: first combines A,B, second inverts the result
        g1 = NandGate('Nand1', in1_label='A', in2_label='B', out_label="(AB)'").shift(LEFT*4)
        g2 = NandGate('Nand2', in1_label="(AB)'", in2_label="(AB)'", out_label="A.B").shift(RIGHT*1)

        self.play(*[Create(g) for g in (g1, g2)])

        # wire g1's single output to BOTH inputs of g2 (tied together, like Nand(x,x))
        wire1 = right_angle_wire(g1.out.get_end(), g2.in1.get_start(), color=BLACK)
        wire2 = right_angle_wire(g1.out.get_end(), g2.in2.get_start(), color=BLACK)
        self.play(Create(wire1), Create(wire2))


        nand1 = Text('Nand1: Nand(A, B)', font_size=16, weight=BOLD, color=BLACK, font="Arial").shift(RIGHT*4, UP*2.5)
        nand1_1 = Text("= (AB)'", font_size=15, slant=ITALIC, color=BLACK, font="Arial").next_to(nand1, DOWN, aligned_edge=LEFT, buff=0.15)

        nand2 = Text("Nand2: Nand((AB)', (AB)')", font_size=16, weight=BOLD, color=BLACK, font="Arial").next_to(nand1_1, DOWN, aligned_edge=LEFT, buff=0.3)
        nand2_1 = Text("= ((AB)'(AB)')' || Nand(x,x) = x'", font_size=15, slant=ITALIC, color=BLACK, font="Arial").next_to(nand2, DOWN, aligned_edge=LEFT, buff=0.15)
        nand2_2 = Text("= ((AB)')' || x.x = x (Idempotent Law)", font_size=15, slant=ITALIC, color=BLACK, font="Arial").next_to(nand2_1, DOWN, aligned_edge=LEFT, buff=0.15)
        nand2_3 = Text("= AB || Double Negation Law: (x')' = x", font_size=15, slant=ITALIC, color=BLACK, font="Arial").next_to(nand2_2, DOWN, aligned_edge=LEFT, buff=0.15)
        nand2_4 = Text("= A . B -- AND Logic", font_size=16, color=BLACK, font="Arial").next_to(nand2_3, DOWN, aligned_edge=LEFT, buff=0.15)


        self.play(Write(nand1))
        self.play(Write(nand1_1))
        self.play(Write(nand2))
        self.play(Write(nand2_1))
        self.play(Write(nand2_2))
        self.play(Write(nand2_3))
        self.play(Write(nand2_4))

        self.wait(2)


def AND_from_NAND(a, b):
    return Nand(Nand(a, b), Nand(a, b))


class ANDTruthTable(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        title = Text("AND built from NAND — Truth Table Proof", font_size=32, color=BLACK).to_edge(UP)
        self.play(Write(title))

        headers = ["A", "B", "NAND(A,B)", "AND_from_NAND", "A and B", "Match?"]
        rows = []
        for a in [0, 1]:
            for b in [0, 1]:
                nab = int(Nand(a, b))
                computed = int(AND_from_NAND(bool(a), bool(b)))
                expected = int(bool(a) and bool(b))
                rows.append([a, b, nab, computed, expected, "✓" if computed == expected else "✗"])

        table = Table(
            [[str(x) for x in row] for row in rows],
            col_labels=[Text(h, font_size=24, color=BLACK) for h in headers],
        ).scale(0.6).next_to(title, DOWN, buff=0.5)

        table.get_entries().set_color(BLACK)
        table.get_col_labels().set_color(BLACK)

        self.play(Create(table))
        self.wait(2)