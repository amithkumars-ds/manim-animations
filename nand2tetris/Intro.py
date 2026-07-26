import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from manim import *
from chips import *

class SeriesIntro(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # ================= SCENE 1: Intro =================
        intro_title = Text("From NAND to Tetris", font_size=44, weight=BOLD, color=BLACK, font="Arial")
        intro_sub = Text("Building a computer, from first principles", font_size=22, color=BLACK, font="Arial")
        intro_sub.next_to(intro_title, DOWN, buff=0.4)

        self.play(Write(intro_title))
        self.play(Write(intro_sub))
        self.wait(2)
        self.play(FadeOut(intro_title), FadeOut(intro_sub))
        self.wait(0.3)

        # ================= SCENE 2: NAND -> Tetris block morph (colored) =================
        nand = NandGate("NAND", in1_label="A", in2_label="B", out_label="out").scale(1.3)
        self.play(Create(nand))
        self.wait(1)

        sq = 0.6
        tetris_color = "#F97316"  # orange accent, matches your silicon-is-all-you-need branding
        block1 = Square(side_length=sq, color=BLACK, fill_color=tetris_color, fill_opacity=1).shift(LEFT*sq/2 + UP*sq/2)
        block2 = Square(side_length=sq, color=BLACK, fill_color=tetris_color, fill_opacity=1).shift(RIGHT*sq/2 + UP*sq/2)
        block3 = Square(side_length=sq, color=BLACK, fill_color=tetris_color, fill_opacity=1).shift(LEFT*sq*1.5 + UP*sq/2)
        block4 = Square(side_length=sq, color=BLACK, fill_color=tetris_color, fill_opacity=1).shift(RIGHT*sq/2 + DOWN*sq/2)
        tetris_block = VGroup(block1, block2, block3, block4)

        self.play(Transform(nand, tetris_block))
        self.wait(2)
        self.play(FadeOut(nand))
        self.wait(0.3)

        # ================= SCENE 3: Chapters, one at a time with components =================
        chapters_data = [
            ("1. Boolean Logic", ["NAND, NOT, AND, OR, XOR", "Multiplexors & Demultiplexors"]),
            ("2. Boolean Arithmetic", ["Half Adder & Full Adder", "Multi-bit Adder", "ALU (Arithmetic Logic Unit)"]),
            ("3. Memory", ["Data Flip-Flop (DFF)", "Registers & RAM", "Program Counter"]),
            ("4. Computer Architecture", ["CPU (combining ALU + Registers)", "Instruction Memory", "Full Computer Wiring"]),
            ("5. Machine Language", ["A-Instructions & C-Instructions", "Symbols & Addressing"]),
            ("6. Assembler", ["Parsing .asm files", "Symbol Table Resolution", "Translating to Binary Machine Code"]),
        ]

        chapter_titles_for_roadmap = []

        for chap_title, components in chapters_data:
            title_mob = Text(chap_title, font_size=32, weight=BOLD, color=BLACK, font="Arial").to_edge(UP)
            self.play(Write(title_mob))
            chapter_titles_for_roadmap.append(chap_title)

            comp_lines = [Text(c, font_size=22, color=BLACK, font="Arial") for c in components]
            comp_lines[0].next_to(title_mob, DOWN, buff=0.6)
            for i in range(1, len(comp_lines)):
                comp_lines[i].next_to(comp_lines[i-1], DOWN, aligned_edge=LEFT, buff=0.3)

            comp_group = VGroup(*comp_lines)
            comp_group.move_to(ORIGIN).align_to(title_mob, UP).shift(DOWN*1.2)

            for line in comp_lines:
                self.play(Write(line))
                self.wait(0.3)

            self.wait(1.5)
            self.play(FadeOut(title_mob), FadeOut(comp_group))
            self.wait(0.3)

        # ================= Final roadmap after chapter 6 =================
        roadmap_title = Text("The Full Roadmap", font_size=32, weight=BOLD, color=BLACK, font="Arial").to_edge(UP)
        self.play(Write(roadmap_title))

        roadmap_lines = [Text(c, font_size=26, color=BLACK, font="Arial") for c in chapter_titles_for_roadmap]
        roadmap_lines[0].next_to(roadmap_title, DOWN, buff=0.6)
        for i in range(1, len(roadmap_lines)):
            roadmap_lines[i].next_to(roadmap_lines[i-1], DOWN, aligned_edge=LEFT, buff=0.35)

        roadmap_group = VGroup(*roadmap_lines)
        roadmap_group.move_to(ORIGIN).align_to(roadmap_title, UP).shift(DOWN*1.3)

        for line in roadmap_lines:
            self.play(Write(line))
            self.wait(0.3)

        self.wait(2)
        self.play(FadeOut(roadmap_group), FadeOut(roadmap_title))
        self.wait(0.3)

        # ================= SCENE 4: Sudoku teaser (one line) =================
        teaser = Text(
            "And once the computer is complete... we'll build a Sudoku game on it.",
            font_size=28, weight=BOLD, color=BLACK, font="Arial"
        )
        self.play(Write(teaser))
        self.wait(3)