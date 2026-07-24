import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))  # adjust depth to reach chips.py's folder

from manim import *
from chips import *

class ORCircuit(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        title = Text("Boolean Logic Proof for OR Gate from Nand", font_size=22, weight=BOLD, color=BLACK, font="Arial").to_edge(UP)
        self.play(Write(title))

        # instantiate 3 NAND gates: two act as inverters, one combines
        g1 = NandGate('Nand1', in1_label='A', in2_label='A', out_label="A'").shift(LEFT*4 + UP*1.5)
        g2 = NandGate('Nand2', in1_label='B', in2_label='B', out_label="B'").shift(LEFT*4 + DOWN*1.5)
        g3 = NandGate('Nand3', in1_label="A'", in2_label="B'", out_label="A+B").shift(RIGHT*1)

        self.play(*[Create(g) for g in (g1, g2, g3)])

        # wire g1's output and g2's output into g3's two inputs
        wire1 = right_angle_wire(g1.out.get_end(), g3.in1.get_start(), color=BLACK)
        wire2 = right_angle_wire(g2.out.get_end(), g3.in2.get_start(), color=BLACK)
        self.play(Create(wire1), Create(wire2))


        nand1 = Text('Nand1: Nand(A, A)', font_size=16, weight=BOLD, color=BLACK, font="Arial").shift(RIGHT*4, UP*2.5)
        nand1_1 = Text("= (AA)' = A'", font_size=15, slant=ITALIC, color=BLACK, font="Arial").next_to(nand1, DOWN, aligned_edge=LEFT, buff=0.15)

        nand2 = Text('Nand2: Nand(B, B)', font_size=16, weight=BOLD, color=BLACK, font="Arial").next_to(nand1_1, DOWN, aligned_edge=LEFT, buff=0.3)
        nand2_1 = Text("= (BB)' = B'", font_size=15, slant=ITALIC, color=BLACK, font="Arial").next_to(nand2, DOWN, aligned_edge=LEFT, buff=0.15)

        nand3 = Text("Nand3: Nand(A', B')", font_size=16, weight=BOLD, color=BLACK, font="Arial").next_to(nand2_1, DOWN, aligned_edge=LEFT, buff=0.3)
        nand3_1 = Text("= (A'B')' || (xy)' DeMorgan's 2nd Law expansion", font_size=15, slant=ITALIC, color=BLACK, font="Arial").next_to(nand3, DOWN, aligned_edge=LEFT, buff=0.15)
        nand3_2 = Text("= (A')' + (B')' || Double Negation Law: (x')' = x", font_size=15, slant=ITALIC, color=BLACK, font="Arial").next_to(nand3_1, DOWN, aligned_edge=LEFT, buff=0.15)
        nand3_3 = Text("= A + B -- OR Logic ", font_size=15, color=BLACK, font="Arial").next_to(nand3_2, DOWN, aligned_edge=LEFT, buff=0.15)


        self.play(Write(nand1))
        self.play(Write(nand1_1))
        self.play(Write(nand2))
        self.play(Write(nand2_1))
        self.play(Write(nand3))
        self.play(Write(nand3_1))
        self.play(Write(nand3_2))
        self.play(Write(nand3_3))

        self.wait(2)


def Nand(a, b):
    return not (a and b)

def OR_from_NAND(a, b):
    return Nand(Nand(a, a), Nand(b, b))


class ORTruthTable(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        title = Text("OR built from NAND — Truth Table Proof", font_size=32, color=BLACK).to_edge(UP)
        self.play(Write(title))

        headers = ["A", "B", "NAND(A,A)", "NAND(B,B)", "OR_from_NAND", "A or B", "Match?"]
        rows = []
        for a in [0, 1]:
            for b in [0, 1]:
                na = int(Nand(a, a))
                nb = int(Nand(b, b))
                computed = int(OR_from_NAND(bool(a), bool(b)))
                expected = int(bool(a) or bool(b))
                rows.append([a, b, na, nb, computed, expected, "✓" if computed == expected else "✗"])

        table = Table(
            [[str(x) for x in row] for row in rows],
            col_labels=[Text(h, font_size=24, color=BLACK) for h in headers],
        ).scale(0.6).next_to(title, DOWN, buff=0.5)

        table.get_entries().set_color(BLACK)
        table.get_col_labels().set_color(BLACK)

        self.play(Create(table))
        self.wait(2)