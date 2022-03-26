# SE FOR COPIAR, DÁ UMA ESTRELA NO REP
def aproximacao(x: float, xb: float, pontos: int, equacao: str) -> float:
    base = (xb - x) / (1 + pontos)
    area = 0
    while x < xb:
        altura = eval(equacao)
        area += base * altura
        x += base
    return area


print(aproximacao(int(input("Xa:")), int(input("Xb:")), int(input("Xi:")), input("Equação:")))
