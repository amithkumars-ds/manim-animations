import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from manim import *
from chips import *

def XOR_from_NAND(a, b):
    nandAB = Nand(a, b)
    nandA = Nand(a, nandAB)
    nandB = Nand(b, nandAB)
    return Nand(nandA, nandB)


class XORFull(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # ================= SCENE 1: Circuit Implementation =================
        title1 = Text("XOR Gate from Nand — Circuit Implementation", font_size=22, weight=BOLD, color=BLACK, font="Arial").to_edge(UP)
        self.play(Write(title1))

        g1 = NandGate('Nand1', in1_label='A', in2_label='B', out_label="(AB)'").shift(LEFT*5)
        g2 = NandGate('Nand2', in1_label='A', in2_label="(AB)'", out_label="A' + AB").shift(LEFT*1 + UP*2)
        g3 = NandGate('Nand3', in1_label='B', in2_label="(AB)'", out_label="B' + AB").shift(LEFT*1 + DOWN*2)
        g4 = NandGate('Nand4', in1_label="A' + AB", in2_label="B' + AB", out_label="A xor B").shift(RIGHT*3.5)

        gate_group = VGroup(g1, g2, g3, g4)
        self.play(*[Create(g) for g in (g1, g2, g3, g4)])

        wire1 = right_angle_wire(g1.out.get_end(), g2.in2.get_start(), color=BLACK)
        wire2 = right_angle_wire(g1.out.get_end(), g3.in2.get_start(), color=BLACK)
        wire3 = right_angle_wire(g2.out.get_end(), g4.in1.get_start(), color=BLACK)
        wire4 = right_angle_wire(g3.out.get_end(), g4.in2.get_start(), color=BLACK)

        wire_group = VGroup(wire1, wire2, wire3, wire4)
        self.play(*[Create(w) for w in wire_group])
        self.wait(4)

        self.play(FadeOut(gate_group), FadeOut(wire_group), FadeOut(title1))
        self.wait(0.5)


        # ================= SCENE 2: Boolean Logic Proof (centered) =================
        title2 = Text("Boolean Logic Proof for XOR Gate from Nand", font_size=22, weight=BOLD, color=BLACK, font="Arial").to_edge(UP)
        self.play(Write(title2))

        nand1 = Text('Nand1: Nand(A, B)', font_size=16, weight=BOLD, color=BLACK, font="Arial")
        nand1_1 = Text("= (AB)'", font_size=15, slant=ITALIC, color=BLACK, font="Arial")

        nand2 = Text("Nand2: Nand(A, (AB)')", font_size=16, weight=BOLD, color=BLACK, font="Arial")
        nand2_1 = Text("= (A.(AB)')'", font_size=15, slant=ITALIC, color=BLACK, font="Arial")
        nand2_2 = Text("= A' + (AB) || DeMorgan's + Double Negation", font_size=15, slant=ITALIC, color=BLACK, font="Arial")
        nand2_3 = Text("= A' + B -- nandA || Absorption: A' + AB = A' + B", font_size=15, slant=ITALIC, color=BLACK, font="Arial")

        nand3 = Text("Nand3: Nand(B, (AB)')", font_size=16, weight=BOLD, color=BLACK, font="Arial")
        nand3_1 = Text("= (B.(AB)')'", font_size=15, slant=ITALIC, color=BLACK, font="Arial")
        nand3_2 = Text("= B' + A -- nandB || same identity, symmetric", font_size=15, slant=ITALIC, color=BLACK, font="Arial")

        nand4 = Text("Nand4: Nand(nandA, nandB)", font_size=16, weight=BOLD, color=BLACK, font="Arial")
        nand4_1 = Text("= ((A'+B)(B'+A))'", font_size=15, slant=ITALIC, color=BLACK, font="Arial")
        nand4_2 = Text("= (AB + A'B')' || expand & simplify", font_size=15, slant=ITALIC, color=BLACK, font="Arial")
        nand4_3 = Text("= A'B + AB' -- XOR Logic || DeMorgan's on final NAND", font_size=16, color=BLACK, font="Arial")

        proof_lines = [nand1, nand1_1, nand2, nand2_1, nand2_2, nand2_3,
                       nand3, nand3_1, nand3_2, nand4, nand4_1, nand4_2, nand4_3]

        # stack all lines centered (left-aligned to each other, but the block as a whole is centered)
        proof_lines[0].next_to(title2, DOWN, buff=0.5)
        for i in range(1, len(proof_lines)):
            buff = 0.3 if proof_lines[i] in (nand2, nand3, nand4) else 0.15
            proof_lines[i].next_to(proof_lines[i-1], DOWN, aligned_edge=LEFT, buff=buff)

        proof_group = VGroup(*proof_lines)
        proof_group.move_to(ORIGIN).align_to(title2, UP).shift(DOWN*1.2)  # recenter block horizontally
        proof_group.set_x(0)

        for line in proof_lines:
            self.play(Write(line))

        self.wait(4)
        self.play(FadeOut(proof_group), FadeOut(title2))
        self.wait(0.5)


        # ================= SCENE 3: HDL Implementation =================
        title3 = Text("HDL Implementation", font_size=22, weight=BOLD, color=BLACK, font="Arial").to_edge(UP)
        self.play(Write(title3))

        hdl_code = '''CHIP Xor {
    IN a, b;
    OUT out;

    PARTS:
    Nand(a=a, b=b, out=nandAB);
    Nand(a=a, b=nandAB, out=nandA);
    Nand(a=b, b=nandAB, out=nandB);
    Nand(a=nandA, b=nandB, out=out);
}'''

        hdl_text = Code(
            code_string=hdl_code,
            language="java",
            background="rectangle",
            add_line_numbers=True,
        ).scale(0.8).next_to(title3, DOWN, buff=0.5)

        self.play(Create(hdl_text))
        self.wait(4)
        self.play(FadeOut(hdl_text), FadeOut(title3))
        self.wait(0.5)


        # ================= SCENE 4: Truth Table (slow reveal) =================
        title4 = Text("XOR built from NAND — Truth Table Proof", font_size=28, weight=BOLD, color=BLACK, font="Arial").to_edge(UP)
        self.play(Write(title4))

        headers = ["A", "B", "XOR_from_NAND", "A xor B", "Match?"]
        rows = []
        for a in [0, 1]:
            for b in [0, 1]:
                computed = int(XOR_from_NAND(bool(a), bool(b)))
                expected = int(bool(a) != bool(b))
                rows.append([a, b, computed, expected, "✓" if computed == expected else "✗"])

        table = Table(
            [[str(x) for x in row] for row in rows],
            col_labels=[Text(h, font_size=24, color=BLACK) for h in headers],
        ).scale(0.6).next_to(title4, DOWN, buff=0.5)

        table.get_entries().set_color(BLACK)
        table.get_col_labels().set_color(BLACK)

        # reveal row by row: header first, then each row's cells fade/write in sequence
        self.play(Create(table.get_horizontal_lines()), Create(table.get_vertical_lines()))
        self.play(*[Write(label) for label in table.get_col_labels()])
        self.wait(0.5)

        entries = table.get_entries()
        n_cols = len(headers)
        n_rows = len(rows)
        for r in range(n_rows):
            row_cells = entries[r*n_cols:(r+1)*n_cols]
            self.play(*[FadeIn(cell) for cell in row_cells], run_time=0.8)
            self.wait(0.6)

        self.wait(3)
        self.play(FadeOut(table), FadeOut(title4))
        self.wait(0.5)


        # ================= SCENE 5: Next Up =================
        next_up = Text("Next up -- 2:1 Mux Gate", font_size=32, weight=BOLD, color=BLACK, font="Arial")
        self.play(Write(next_up))
        self.wait(3)