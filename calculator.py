# Copyright (C) 2026 Berkem Toprak Elmacı
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout,
    QPushButton, QLineEdit, QTextEdit, QLabel
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from math import *
import sys

# Variables
π = pi
Φ = 1.618033988749895
fi = Φ
ans = 0
constant1 = constant2 = constant3 = constant4 = constant5 = constant6 = constant7 = 0


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(1000, 480)
        self.setStyleSheet("background-color: #888888;")

        self.ans = 0
        self.constant1 = self.constant2 = self.constant3 = 0
        self.constant4 = self.constant5 = self.constant6 = self.constant7 = 0

        central = QWidget()
        self.setCentralWidget(central)
        self.grid = QGridLayout(central)
        self.grid.setSpacing(1)
        self.grid.setContentsMargins(2, 2, 2, 2)

        self._build_ui()

    # ── helpers ──────────────────────────────────────────────────────────────

    def btn(self, text, bg, fg="#000000", colspan=1, rowspan=1, small=False):
        b = QPushButton(text)
        font_size = 8 if small else 9
        b.setFont(QFont("Helvetica", font_size))
        b.setStyleSheet(
            f"QPushButton {{ background-color:{bg}; color:{fg}; padding:1px 1px; }}"
            f"QPushButton:hover {{ background-color: #DDDDDD; }}"
        )
        b.setMinimumHeight(28)
        return b

    def place(self, widget, row, col, rowspan=1, colspan=1):
        self.grid.addWidget(widget, row, col, rowspan, colspan)

    # ── actions ───────────────────────────────────────────────────────────────

    def h(self, x):
        self.entry1.insert(str(x))

    def f(self, x):
        self.text1.insertPlainText(str(x))

    def g(self):
        try:
            a = self.entry1.text()
            result = eval(a, {"__builtins__": {}}, {
                "sin": sin, "cos": cos, "tan": tan, "sinh": sinh,
                "cosh": cosh, "tanh": tanh, "asin": asin, "acos": acos,
                "atan": atan, "log": log, "log10": log10, "log2": log2,
                "sqrt": sqrt, "exp": exp, "fabs": fabs, "fmod": fmod,
                "factorial": factorial, "ceil": ceil, "floor": floor,
                "radians": radians, "degrees": degrees,
                "pi": pi, "e": e,
                "π": π, "Φ": Φ, "fi": fi,
                "ans": self.ans,
            })
            self.text1.append(f"{a} = {result}\n")
            self.entry1.clear()
            self.entry2.clear()
            self.entry2.insert(str(result))
            self.ans = result
        except Exception:
            self.entry1.clear()
            self.entry2.clear()
            self.entry2.insert("invalid input")

    def m(self, func):
        y = self.entry1.text()
        self.entry1.clear()
        self.entry1.insert(f"{func}({y})")

    def n(self, func):
        y = self.entry1.text()
        self.entry1.clear()
        text = f"{func}({y},)"
        self.entry1.insert(text)
        self.entry1.setCursorPosition(len(text) - 1)

    def assign(self, x):
        if x == 1:   self.constant1 = self.ans
        elif x == 2: self.constant2 = self.ans
        elif x == 3: self.constant3 = self.ans
        elif x == 4: self.constant4 = self.ans
        elif x == 5: self.constant5 = self.ans
        elif x == 6: self.constant6 = self.ans
        elif x == 7: self.constant7 = self.ans
        elif x == 11: self.h(self.constant1)
        elif x == 22: self.h(self.constant2)
        elif x == 33: self.h(self.constant3)
        elif x == 44: self.h(self.constant4)
        elif x == 55: self.h(self.constant5)
        elif x == 66: self.h(self.constant6)
        elif x == 77: self.h(self.constant7)

    # ── UI build ──────────────────────────────────────────────────────────────

    def _build_ui(self):
        # ── text / entry widgets ──────────────────────────────────────────────
        self.entry1 = QLineEdit()
        self.entry1.setFont(QFont("Helvetica", 11))
        self.entry1.returnPressed.connect(self.g)
        self.place(self.entry1, 0, 14, 1, 7)

        self.entry2 = QLineEdit()
        self.entry2.setFont(QFont("Helvetica", 11))
        self.place(self.entry2, 0, 21, 1, 7)

        self.text1 = QTextEdit()
        self.text1.setFont(QFont("Helvetica", 9))
        self.text1.setStyleSheet("background-color:#555555; color:#FFFFFF;")
        self.place(self.text1, 1, 21, 9, 7)

        # ── number buttons ────────────────────────────────────────────────────
        nums = [
            (0, 4, 14, 1, 2), (1, 3, 14), (2, 3, 15), (3, 3, 16),
            (4, 2, 14), (5, 2, 15), (6, 2, 16),
            (7, 1, 14), (8, 1, 15), (9, 1, 16),
        ]
        for item in nums:
            n_val = item[0]; row = item[1]; col = item[2]
            cs = item[4] if len(item) > 4 else 1
            b = self.btn(str(n_val), "#B4B4FF")
            b.clicked.connect(lambda _, v=n_val: self.h(v))
            self.place(b, row, col, 1, cs)

        # ── operator buttons ──────────────────────────────────────────────────
        ops = [
            ("+", 1, 17), ("-", 2, 17), ("*", 3, 17), ("/", 4, 17),
        ]
        for txt, r, c in ops:
            b = self.btn(txt, "#FFA0A0")
            b.clicked.connect(lambda _, v=txt: self.h(v))
            self.place(b, r, c)

        dot_b = self.btn(".", "#96C8C8")
        dot_b.clicked.connect(lambda: self.h("."))
        self.place(dot_b, 4, 16)

        lpar = self.btn("(", "#FFFF80")
        lpar.clicked.connect(lambda: self.h("("))
        self.place(lpar, 6, 20)

        rpar = self.btn(")", "#FFFF80")
        rpar.clicked.connect(lambda: self.h(")"))
        self.place(rpar, 7, 20)

        equal_b = self.btn("=", "#C8C8C8")
        equal_b.clicked.connect(self.g)
        self.place(equal_b, 5, 16, 1, 2)

        del_b = self.btn("C", "#C8C8C8")
        del_b.clicked.connect(lambda: self.entry1.clear())
        self.place(del_b, 5, 18)

        bs_b = self.btn("<--", "#C8C8C8")
        bs_b.clicked.connect(lambda: self.entry1.backspace())
        self.place(bs_b, 4, 18)

        deltext_b = self.btn("del>", "#C8C8C8")
        deltext_b.clicked.connect(lambda: self.text1.clear())
        self.place(deltext_b, 8, 20)

        exp_btn = self.btn("exp", "#B1FF64")
        exp_btn.clicked.connect(lambda: self.h("e"))
        self.place(exp_btn, 3, 19)

        ans_b = self.btn("ans", "#C8C8C8")
        ans_b.clicked.connect(lambda: self.h(self.ans))
        self.place(ans_b, 5, 14, 1, 2)

        # ── math buttons ──────────────────────────────────────────────────────
        pow_b = self.btn("^", "#B1FF64")
        pow_b.clicked.connect(lambda: self.h("**"))
        self.place(pow_b, 2, 18)

        sqrt_b = self.btn("√", "#B1FF64")
        sqrt_b.clicked.connect(lambda: self.m("sqrt"))
        self.place(sqrt_b, 3, 18)

        math_btns = [
            ("lnx",     6, 18, 1, 2, "#AFC982", lambda: self.m("log")),
            ("log(x)",  7, 18, 1, 2, "#AFC982", lambda: self.m("log10")),
            ("log(a,b)",8, 18, 1, 2, "#AFC982", lambda: self.n("log")),
            ("(a)mod(b)",9,18,1, 2, "#AA7ACC", lambda: self.n("fmod")),
            ("sin",  6, 14, 1, 1, "#A0FFA0", lambda: self.m("sin")),
            ("cos",  7, 14, 1, 1, "#A0FFA0", lambda: self.m("cos")),
            ("tan",  8, 14, 1, 1, "#A0FFA0", lambda: self.m("tan")),
            ("cot",  9, 14, 1, 1, "#A0FFA0", lambda: self.h("1/tan(")),
            ("sinh", 6, 15, 1, 1, "#A0FFA0", lambda: self.m("sinh")),
            ("cosh", 7, 15, 1, 1, "#A0FFA0", lambda: self.m("cosh")),
            ("tanh", 8, 15, 1, 1, "#A0FFA0", lambda: self.m("tanh")),
            ("coth", 9, 15, 1, 1, "#A0FFA0", lambda: self.h("1/tanh(")),
            ("arcsin", 6, 16, 1, 2, "#A0FFA0", lambda: self.m("asin")),
            ("arccos", 7, 16, 1, 2, "#A0FFA0", lambda: self.m("acos")),
            ("arctan", 8, 16, 1, 2, "#A0FFA0", lambda: self.m("atan")),
            ("arccot", 9, 16, 1, 2, "#A0FFA0", lambda: self.h("atan(1/")),
            ("x!",    2, 20, 1, 1, "#B1FF64", lambda: self.m("factorial")),
            ("ceil",  5, 19, 1, 1, "#DDDDDD", lambda: self.m("ceil")),
            ("floor", 5, 20, 1, 1, "#DDDDDD", lambda: self.m("floor")),
            ("|x|",   3, 20, 1, 1, "#B1FF64", lambda: self.m("fabs")),
            ("rad",   4, 19, 1, 1, "#DDDDDD", lambda: self.m("radians")),
            ("deg",   4, 20, 1, 1, "#DDDDDD", lambda: self.m("degrees")),
            ("e^x",   2, 19, 1, 1, "#B1FF64", lambda: self.m("exp")),
        ]
        for item in math_btns:
            txt, r, c, rs, cs, bg, cmd = item
            b = self.btn(txt, bg)
            b.clicked.connect(cmd)
            self.place(b, r, c, rs, cs)

        # ── constant buttons ──────────────────────────────────────────────────
        pi_b = self.btn("π", "#FFFFB4")
        pi_b.clicked.connect(lambda: self.h("π"))
        self.place(pi_b, 1, 18)

        e_b = self.btn("e", "#FFFFB4")
        e_b.clicked.connect(lambda: self.h("e"))
        self.place(e_b, 1, 19)

        fi_b = self.btn("Φ", "#FFFFB4")
        fi_b.clicked.connect(lambda: self.h("Φ"))
        self.place(fi_b, 1, 20)

        # ── memory (constant) buttons ────────────────────────────────────────────
        constant_set = [("x=",1),("y=",2),("z=",3),("t=",4),("a=",5),("b=",6),("c=",7)]
        constant_get = [("x",11),("y",22),("z",33),("t",44),("a",55),("b",66),("c",77)]
        for i, (txt, code) in enumerate(constant_set):
            b = self.btn(txt, "#DDDDDD")
            b.clicked.connect(lambda _, c=code: self.assign(c))
            self.place(b, 10+i, 27)
        for i, (txt, code) in enumerate(constant_get):
            b = self.btn(txt, "#DDDDDD")
            b.clicked.connect(lambda _, c=code: self.assign(c))
            self.place(b, 10+i, 25, 1, 2)

        # ── physical constants ────────────────────────────────────────────────
        phys = [
            # Planck
            ("h: planck\n(J·sn)",    1, 6, "#84EDFF", 6.62606957e-34),
            ("h (eV·sn)",            2, 6, "#84EDFF", 4.135667516e-15),
            ("h (erg·sn)",           3, 6, "#84EDFF", 6.62606957e-27),
            # Boltzmann
            ("k:boltzman\n(Joule/K)",4, 6, "#6FEAFF", 1.38065e-23),
            ("k\n(eV/K)",            5, 6, "#6FEAFF", 8.617343e-5),
            ("k\n(erg/K)",           6, 6, "#6FEAFF", 1.38065e-16),
            # Rydberg
            ("R: Rydberg\n(m^-1)",   7, 6, "#3CACFF", 10973548.229),
            ("R\n(eV)",              8, 6, "#3CACFF", 13.60569),
            ("R\n(Joule)",           9, 6, "#3CACFF", 2.18e-18),
            ("R\n[atm*L/(mol*K)]",  10, 6, "#3CACFF", 0.082051282051282),
            ("R\n[J/(K·mol)]",      11, 6, "#3CACFF", 8.314),
            # Avogadro etc
            ("Na: avogadro\n(1/mol)",1, 8, "#80FF80", 6.022136736e23),
            ("u (akb)\n(kg)",        2, 8, "#80FF80", 1.660540210e-27),
            ("electronmass\n(kg)",   3, 8, "#80FF80", 9.10938e-31),
            ("electronmass\n(MeV/c²)",4,8,"#80FF80", 0.5109989461),
            ("electronmass\n(akb)",  5, 8, "#80FF80", 5.48579909070e-4),
            ("electron\n(Coulomb)",  6, 8, "#80FF80", -1.60217e-19),
            ("proton mass\n(kg)",    7, 8, "#80FF80", 1.67262e-27),
            ("proton mass\n(MeV/c²)",8,8,"#80FF80", 938.272029),
            ("proton\n(Coulomb)",    9, 8, "#80FF80", 1.60217e-19),
            ("neutron\nmass (kg)",  10, 8, "#80FF80", 1.674928610e-27),
            ("doteron mass\n(kg)",  11, 8, "#80FF80", 3.343586020e-27),
            # Electromagnetic
            ("c (m/s)\nspeed of light",1,10,"#004080",299792458.01),
            ("G (universal)\nN·m²/kg²",2,10,"#202020",6.6725985e-11),
            ("g (earth)\n(m/s²)",   3,10,"#552B00", 9.860665),
            ("μ0\n(N/A²)",          4,10,"#808000", 1.2566370614359173e-06),
            ("ε0\n[c²/(N·m²)]",     5,10,"#808000", 8.854187817e-12),
            ("k (electric)\n(N·m²/c²)",6,10,"#808000",8987551787.96),
            ("K (magnetic)\n(N/A²)",7,10,"#808000", 1e-7),
            # Quantum
            ("mB bohr (J/T)\nmagneton",1,2,"#561855",9.274015431e-24),
            ("a0 bohr\nradius(m)",   2, 2, "#561855", 0.52917724924e-10),
            ("e- compton\nλ (m)",    3, 2, "#561855", 2.4263105822e-12),
            ("h/e² hall\nresist.(Ω)",4, 2, "#561855", 25812.805612),
            ("nuclear\nmagneton(kg)",5, 2, "#561855", 5.050786617e-27),
            ("magnetic\nflux q.(Wb)",6, 2, "#561855", 2.0678346161e-15),
            # Astronomical
            ("Hubble (s⁻¹)\nparameter",1,4,"#FFC90D",2.5e-18),
            ("earth ect.\nradius(m)", 2, 4, "#FFC90D", 6.374e6),
            ("earth\nmass (kg)",     3, 4, "#FFC90D", 5.976e24),
            ("moon\nmass (kg)",      4, 4, "#FFC90D", 7.35e22),
            ("moon orbit\nradius (m)",5,4,"#FFC90D", 3.844e8),
            ("sun\nmass(kg)",        6, 4, "#FFC90D", 1.989e30),
            ("sun\nradius (m)",      7, 4, "#FFC90D", 6.96e8),
            ("earth orbit\nradius (m)",8,4,"#FFC90D",1.496e11),
            ("year\n(sn)",           9, 4, "#FFC90D", 31557600),
            ("milkyway\nradius (m)", 10,4, "#FFC90D", 7.5e20),
            ("milkyway\nmass (kg)",  11,4, "#FFC90D", 2.7e41),
        ]
        for item in phys:
            txt, r, c, bg, val = item
            fg = "#FFFFFF" if bg in ("#004080","#202020","#552B00","#808000","#561855") else "#000000"
            b = self.btn(txt, bg, fg, small=True)
            b.clicked.connect(lambda _, v=val: self.h(v))
            self.place(b, r, c, 1, 2)

        self.grid.setSpacing(0)

        for i in range(20):
            self.grid.setRowStretch(i, 1)

def main():
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
