from manim import *

class NandGate(VGroup):
    def __init__(self, name: str, in1_label: str = "", in2_label: str = "", out_label: str = "", **kwargs):
        super().__init__(**kwargs)

        body = RoundedRectangle(
            width=1.5, height=1.2, corner_radius=0.3, color=BLACK
        )
        bubble = Circle(
            radius=0.08, color=BLACK
        ).next_to(body, RIGHT, buff=0)
        label = Text(name, font_size=14, color=BLACK).move_to(body)

        in1 = Line(body.get_left()+UP*0.3, body.get_left()+UP*0.3+LEFT*0.6,
                   color=BLACK)
        in2 = Line(body.get_left()+DOWN*0.3, body.get_left()+DOWN*0.3+LEFT*0.6,
                   color=BLACK)

        out = Line(bubble.get_right(), bubble.get_right()+RIGHT*0.6,
                   color=BLACK)

        self.add(body, bubble, in1, in2, out, label)
        self.body, self.in1, self.in2, self.out, self.bubble = body, in1, in2, out, bubble

        # pin name labels, placed above each input line's start point
        if in1_label:
            in1_name = Text(in1_label, font_size=12, color=BLACK).next_to(in1.get_end(), UP, buff=0.1)
            self.add(in1_name)
            self.in1_name = in1_name

        if in2_label:
            in2_name = Text(in2_label, font_size=12, color=BLACK).next_to(in2.get_end(), UP, buff=0.1)
            self.add(in2_name)
            self.in2_name = in2_name

        # output label, placed above the output line's far end
        if out_label:
            out_name = Text(out_label, font_size=12, color=BLACK).next_to(out.get_end(), UP, buff=0.1)
            self.add(out_name)
            self.out_name = out_name

class NotGate(VGroup):
    """Standard NOT symbol: triangle + inversion bubble."""
    def __init__(self, name: str = "", in_label: str = "", out_label: str = "", **kwargs):
        super().__init__(**kwargs)

        body = Polygon(
            LEFT*0.75+UP*0.6, LEFT*0.75+DOWN*0.6, RIGHT*0.75,
            color=BLACK
        )
        bubble = Circle(radius=0.08, color=BLACK).next_to(body, RIGHT, buff=0)
        label = Text(name, font_size=12, color=BLACK).move_to(body).shift(LEFT*0.15) if name else None

        in1 = Line(body.get_left(), body.get_left()+LEFT*0.6, color=BLACK)
        out = Line(bubble.get_right(), bubble.get_right()+RIGHT*0.6, color=BLACK)

        self.add(body, bubble, in1, out)
        if label:
            self.add(label)
        self.body, self.in1, self.out, self.bubble = body, in1, out, bubble

        if in_label:
            in1_name = Text(in_label, font_size=12, color=BLACK).next_to(in1.get_end(), UP, buff=0.1)
            self.add(in1_name)
            self.in1_name = in1_name

        if out_label:
            out_name = Text(out_label, font_size=12, color=BLACK).next_to(out.get_end(), UP, buff=0.1)
            self.add(out_name)
            self.out_name = out_name

class AndGate(VGroup):
    def __init__(self, name: str = "", in1_label: str = "", in2_label: str = "", out_label: str = "", **kwargs):
        super().__init__(**kwargs)

        top = Line(LEFT*0.75+UP*0.6, RIGHT*0+UP*0.6, color=BLACK)
        bottom = Line(LEFT*0.75+DOWN*0.6, RIGHT*0+DOWN*0.6, color=BLACK)
        straight = Line(LEFT*0.75+UP*0.6, LEFT*0.75+DOWN*0.6, color=BLACK)
        arc = Arc(radius=0.6, start_angle=-PI/2, angle=PI, arc_center=ORIGIN, color=BLACK)
        body = VGroup(straight, top, bottom, arc)
        label = Text(name, font_size=12, color=BLACK).move_to(LEFT*0.25) if name else None

        in1 = Line(LEFT*0.75+UP*0.3, LEFT*0.75+UP*0.3+LEFT*0.6, color=BLACK)
        in2 = Line(LEFT*0.75+DOWN*0.3, LEFT*0.75+DOWN*0.3+LEFT*0.6, color=BLACK)
        out = Line(RIGHT*0.6, RIGHT*0.6+RIGHT*0.6, color=BLACK)  # starts exactly at arc's rightmost point (0.6, 0)

        self.add(body, in1, in2, out)
        if label:
            self.add(label)
        self.body, self.in1, self.in2, self.out = body, in1, in2, out

        if in1_label:
            in1_name = Text(in1_label, font_size=12, color=BLACK).next_to(in1.get_end(), UP, buff=0.1)
            self.add(in1_name); self.in1_name = in1_name
        if in2_label:
            in2_name = Text(in2_label, font_size=12, color=BLACK).next_to(in2.get_end(), UP, buff=0.1)
            self.add(in2_name); self.in2_name = in2_name
        if out_label:
            out_name = Text(out_label, font_size=12, color=BLACK).next_to(out.get_end(), UP, buff=0.1)
            self.add(out_name); self.out_name = out_name

class OrGate(VGroup):
    def __init__(self, name: str = "", in1_label: str = "", in2_label: str = "", out_label: str = "", **kwargs):
        super().__init__(**kwargs)

        top_back = LEFT*0.7 + UP*0.6
        bottom_back = LEFT*0.7 + DOWN*0.6
        tip = RIGHT*0.75

        top_curve = ArcBetweenPoints(top_back, tip, angle=-PI/4, color=BLACK)
        bottom_curve = ArcBetweenPoints(bottom_back, tip, angle=PI/4, color=BLACK)
        back_curve = ArcBetweenPoints(top_back, bottom_back, angle=-PI/3, color=BLACK)

        body = VGroup(top_curve, bottom_curve, back_curve)
        label = Text(name, font_size=12, color=BLACK).move_to(LEFT*0.15) if name else None

        in1 = Line(LEFT*0.55+UP*0.3, LEFT*0.55+UP*0.3+LEFT*0.6, color=BLACK)
        in2 = Line(LEFT*0.55+DOWN*0.3, LEFT*0.55+DOWN*0.3+LEFT*0.6, color=BLACK)
        out = Line(tip, tip+RIGHT*0.6, color=BLACK)

        self.add(body, in1, in2, out)
        if label:
            self.add(label)
        self.body, self.in1, self.in2, self.out = body, in1, in2, out

        if in1_label:
            in1_name = Text(in1_label, font_size=12, color=BLACK).next_to(in1.get_end(), UP, buff=0.1)
            self.add(in1_name); self.in1_name = in1_name
        if in2_label:
            in2_name = Text(in2_label, font_size=12, color=BLACK).next_to(in2.get_end(), UP, buff=0.1)
            self.add(in2_name); self.in2_name = in2_name
        if out_label:
            out_name = Text(out_label, font_size=12, color=BLACK).next_to(out.get_end(), UP, buff=0.1)
            self.add(out_name); self.out_name = out_name

class XorGate(VGroup):
    def __init__(self, name: str = "", in1_label: str = "", in2_label: str = "", out_label: str = "", **kwargs):
        super().__init__(**kwargs)

        top_back = LEFT*0.7 + UP*0.6
        bottom_back = LEFT*0.7 + DOWN*0.6
        tip = RIGHT*0.75

        top_curve = ArcBetweenPoints(top_back, tip, angle=-PI/4, color=BLACK)
        bottom_curve = ArcBetweenPoints(bottom_back, tip, angle=PI/4, color=BLACK)
        back_curve = ArcBetweenPoints(top_back, bottom_back, angle=-PI/3, color=BLACK)

        extra_top_back = LEFT*0.85 + UP*0.6
        extra_bottom_back = LEFT*0.85 + DOWN*0.6
        extra_curve = ArcBetweenPoints(extra_top_back, extra_bottom_back, angle=-PI/3, color=BLACK)

        body = VGroup(top_curve, bottom_curve, back_curve, extra_curve)
        label = Text(name, font_size=12, color=BLACK).move_to(LEFT*0.15) if name else None

        in1 = Line(LEFT*0.55+UP*0.3, LEFT*0.85+UP*0.3+LEFT*0.4, color=BLACK)
        in2 = Line(LEFT*0.55+DOWN*0.3, LEFT*0.85+DOWN*0.3+LEFT*0.4, color=BLACK)
        out = Line(tip, tip+RIGHT*0.6, color=BLACK)

        self.add(body, in1, in2, out)
        if label:
            self.add(label)
        self.body, self.in1, self.in2, self.out = body, in1, in2, out

        if in1_label:
            in1_name = Text(in1_label, font_size=12, color=BLACK).next_to(in1.get_end(), UP, buff=0.1)
            self.add(in1_name); self.in1_name = in1_name
        if in2_label:
            in2_name = Text(in2_label, font_size=12, color=BLACK).next_to(in2.get_end(), UP, buff=0.1)
            self.add(in2_name); self.in2_name = in2_name
        if out_label:
            out_name = Text(out_label, font_size=12, color=BLACK).next_to(out.get_end(), UP, buff=0.1)
            self.add(out_name); self.out_name = out_name

class MuxGate(VGroup):
    """Trapezoid box labeled MUX, with 2 data inputs, 1 select (bottom), 1 output."""
    def __init__(self, name: str = "MUX", in1_label: str = "", in2_label: str = "",
                 sel_label: str = "", out_label: str = "", **kwargs):
        super().__init__(**kwargs)

        body = Polygon(
            LEFT*0.6+UP*0.9, RIGHT*0.6+UP*0.5, RIGHT*0.6+DOWN*0.5, LEFT*0.6+DOWN*0.9,
            color=BLACK
        )
        label = Text(name, font_size=12, color=BLACK).move_to(body)

        in1 = Line(LEFT*0.6+UP*0.6, LEFT*0.6+UP*0.6+LEFT*0.6, color=BLACK)
        in2 = Line(LEFT*0.6+DOWN*0.6, LEFT*0.6+DOWN*0.6+LEFT*0.6, color=BLACK)
        sel = Line(DOWN*0.7, DOWN*0.7+DOWN*0.6, color=BLACK)  # midpoint of the slanted bottom edge, not (0,-0.9)
        out = Line(RIGHT*0.6, RIGHT*0.6+RIGHT*0.6, color=BLACK)

        self.add(body, label, in1, in2, sel, out)
        self.body, self.in1, self.in2, self.sel, self.out = body, in1, in2, sel, out

        if in1_label:
            in1_name = Text(in1_label, font_size=12, color=BLACK).next_to(in1.get_end(), UP, buff=0.1)
            self.add(in1_name); self.in1_name = in1_name
        if in2_label:
            in2_name = Text(in2_label, font_size=12, color=BLACK).next_to(in2.get_end(), DOWN, buff=0.1)
            self.add(in2_name); self.in2_name = in2_name
        if sel_label:
            sel_name = Text(sel_label, font_size=12, color=BLACK).next_to(sel.get_end(), DOWN, buff=0.1)
            self.add(sel_name); self.sel_name = sel_name
        if out_label:
            out_name = Text(out_label, font_size=12, color=BLACK).next_to(out.get_end(), UP, buff=0.1)
            self.add(out_name); self.out_name = out_name

class DemuxGate(VGroup):
    """Inverse trapezoid: 1 input, 1 select (bottom), 2 outputs."""
    def __init__(self, name: str = "DEMUX", in_label: str = "", sel_label: str = "",
                 out1_label: str = "", out2_label: str = "", **kwargs):
        super().__init__(**kwargs)

        body = Polygon(
            LEFT*0.6+UP*0.5, RIGHT*0.6+UP*0.9, RIGHT*0.6+DOWN*0.9, LEFT*0.6+DOWN*0.5,
            color=BLACK
        )
        label = Text(name, font_size=12, color=BLACK).move_to(body)

        in1 = Line(LEFT*0.6, LEFT*0.6+LEFT*0.6, color=BLACK)
        sel = Line(DOWN*0.7, DOWN*0.7+DOWN*0.6, color=BLACK)
        out1 = Line(RIGHT*0.6+UP*0.6, RIGHT*0.6+UP*0.6+RIGHT*0.6, color=BLACK)
        out2 = Line(RIGHT*0.6+DOWN*0.6, RIGHT*0.6+DOWN*0.6+RIGHT*0.6, color=BLACK)

        self.add(body, label, in1, sel, out1, out2)
        self.body, self.in1, self.sel, self.out1, self.out2 = body, in1, sel, out1, out2

        if in_label:
            in1_name = Text(in_label, font_size=12, color=BLACK).next_to(in1.get_end(), UP, buff=0.1)
            self.add(in1_name); self.in1_name = in1_name
        if sel_label:
            sel_name = Text(sel_label, font_size=12, color=BLACK).next_to(sel.get_end(), DOWN, buff=0.1)
            self.add(sel_name); self.sel_name = sel_name
        if out1_label:
            out1_name = Text(out1_label, font_size=12, color=BLACK).next_to(out1.get_end(), UP, buff=0.1)
            self.add(out1_name); self.out1_name = out1_name
        if out2_label:
            out2_name = Text(out2_label, font_size=12, color=BLACK).next_to(out2.get_end(), DOWN, buff=0.1)
            self.add(out2_name); self.out2_name = out2_name


def Nand(a, b):
    return not (a and b)

def Not(a):
    return not a

def And(a, b):
    return a and b

def Or(a, b):
    return a or b

def Xor(a, b):
    return a != b

def OR_from_NAND(a, b):
    return Nand(Nand(a, a), Nand(b, b))


def right_angle_wire(start, end, color=BLACK):
    mid_x = (start[0] + end[0]) / 2
    mid1 = np.array([mid_x, start[1], 0])
    mid2 = np.array([mid_x, end[1], 0])
    seg1 = Line(start, mid1, color=color)
    seg2 = Line(mid1, mid2, color=color)
    seg3 = Line(mid2, end, color=color)
    return VGroup(seg1, seg2, seg3)