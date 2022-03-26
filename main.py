from math import e, pi, sqrt, tan, cos, sin, log as ln, log10 as log
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Frame, Tk, Entry, Label, Button, messagebox
from tkinter.constants import BOTH, BOTTOM, LEFT
import matplotlib.pyplot as plt


class Function:
    def __init__(self, root):
        self.__expressao = ""
        self.root = root
        self.display = Label(root, font=("Arial", 15), relief="solid")
        self.plotado = None
        self.ponto_1 = Entry()
        self.ponto_2 = Entry()
        self.intermedio = Entry()
        self.botoes = [["x", lambda: self.func_button("x")], ["√", lambda: self.func_button("sqrt(")],
                       ["(", lambda: self.func_button("(")], [")", lambda: self.func_button(")")],
                       ["%", lambda: self.func_button("%")], ["CE", self.BtBackSpace],
                       ["sin", lambda: self.func_button("sin(")], ["cos", lambda: self.func_button("cos(")],
                       ["7", lambda: self.func_button("7")], ["8", lambda: self.func_button("8")],
                       ["9", lambda: self.func_button("9")], ["/", lambda: self.func_button("/")],
                       ["tan", lambda: self.func_button("tan(")], ["x^y", lambda: self.func_button("^")],
                       ["4", lambda: self.func_button("4")], ["5", lambda: self.func_button("5")],
                       ["6", lambda: self.func_button("6")], ["*", lambda: self.func_button("*")],
                       ["log", lambda: self.func_button("log(")], ["ln", lambda: self.func_button("ln(")],
                       ["1", lambda: self.func_button("1")], ["2", lambda: self.func_button("2")],
                       ["3", lambda: self.func_button("3")], ["-", lambda: self.func_button("-")],
                       ["π", lambda: self.func_button("π")], ["e", lambda: self.func_button("e")],
                       ["0", lambda: self.func_button("0")], [".", lambda: self.func_button(".")], ["=", self.BtEqual],
                       ["+", lambda: self.func_button("+")]]

    def func_button(self, texto: str):
        self.__expressao += texto
        self.update_display()

    def graphIntegration(self):
        try:
            figura = plt.Figure(figsize=(7, 5), dpi=90)
            ax = figura.add_subplot(111)
            grafico = FigureCanvasTkAgg(figura, self.root).get_tk_widget()
            if self.plotado:
                self.plotado.destroy()
            grafico.pack()
            self.plotado = grafico
            pontos = int(self.intermedio.get())
            entrada = [float(self.ponto_1.get()), float(self.ponto_2.get())]
            x, xb = min(entrada), max(entrada)
            base = (xb - x) / (1 + pontos)
            area = 0
            while x < xb:
                altura = eval(self.__expressao)
                area += abs(base) * abs(altura)
                x += base
                ax.stem(x, altura, linefmt='red', markerfmt=",")
            return area
        except ValueError:
            self.plotado.destroy()

    def update_display(self) -> None:
        self.display.config(text=self.__expressao)

    def BtBackSpace(self) -> None:
        new_string = ""
        for i in range(len(self.__expressao)):
            if i != len(self.__expressao) - 1:
                new_string += self.__expressao[i]
        self.__expressao = new_string
        self.update_display()

    def format_expression(self) -> str:
        return self.__expressao.replace("^", "**").replace("π", "pi").replace("%", "/100 *")

    def BtEqual(self) -> None:
        try:
            self.__expressao = self.format_expression()
            self.display.config(text=f"AREA APROXIMADA = {self.graphIntegration()}")
            self.__expressao = ""
        except (SyntaxError, NameError):
            messagebox.showerror("Erro", "IMPOSSIVEL FAZER ESSA CONTA")
            self.__expressao = ""
            self.update_display()

    @staticmethod
    def set_buttons(root: Frame, list_button: list) -> None:
        for linha in range(5):
            frame_linha = Frame(root)
            frame_linha.pack()
            for coluna in range(6):
                texto, funcao = list_button[coluna + linha * 6]
                Button(frame_linha, text=texto, command=funcao, background="#FFFFFF", relief="solid", width=2,
                       height=1).pack(
                    side=LEFT, ipadx=12, ipady=6, fill=BOTH)


class Calculadora(Function):
    def __init__(self, root):
        super().__init__(root=root)
        self.display.pack(side="top", fill=BOTH, pady=5, padx=5)
        frame_geral = Frame(root, background="#FFFFFF")
        frame_points = Frame(frame_geral, background="#FFFFFF")
        frame_point_1 = Frame(frame_points, background="#FFFFFF")
        frame_intermedio = Frame(frame_points, background="#FFFFFF")
        frame_point_2 = Frame(frame_points, background="#FFFFFF")
        frame_botao = Frame(frame_geral, background="#FFFFFF")
        frame_geral.pack(side=LEFT, padx=45)
        frame_points.pack(pady=10)
        frame_point_1.pack(side=LEFT, padx=10)
        frame_intermedio.pack(side=LEFT, padx=14)
        frame_point_2.pack(side=LEFT, padx=18)
        frame_botao.pack(side=BOTTOM, ipady=40)
        Label(frame_point_1, text="Xa", bg="#FFFFFF").pack(side=LEFT, padx=5)
        Label(frame_intermedio, text="Xi", bg="#FFFFFF").pack(side=LEFT, padx=5)
        Label(frame_point_2, text="Xb", bg="#FFFFFF").pack(side=LEFT, padx=5)
        self.ponto_1 = Entry(frame_point_1, width=3, bg="#F0F8FF")
        self.intermedio = Entry(frame_intermedio, width=3, bg="#F0F8FF")
        self.ponto_2 = Entry(frame_point_2, width=3, bg="#F0F8FF")
        self.ponto_1.pack(side=LEFT)
        self.intermedio.pack(side=LEFT)
        self.ponto_2.pack(side=LEFT)
        self.set_buttons(frame_botao, list_button=self.botoes)


if __name__ == "__main__":
    app = Tk()
    app.geometry("900x500")
    app.title("Calculadora")
    app.configure(background="#FFFFFF")
    Calculadora(app)
    app.resizable(False, False)
    app.mainloop()
