"""Confere o tamanho dos títulos (30) e descrições (90) de um arquivo de campanha.

Uso: python3 ferramentas/checar_anuncios.py caminho/da/campanha.md
Lê as listas numeradas abaixo de "Títulos" e "Descrições".
"""
import re
import sys

LIMITES = {"Títulos": 30, "Descrições": 90}


def checar(caminho):
    secao, erros = None, 0
    for linha in open(caminho, encoding="utf-8"):
        for nome in LIMITES:
            if linha.startswith(nome):
                secao = nome
        m = re.match(r"\s*\d+\.\s*(.+)", linha)
        if secao and m:
            texto = m.group(1).strip()
            n, limite = len(texto), LIMITES[secao]
            marca = "OK " if n <= limite else "ERRO"
            erros += n > limite
            print(f"[{marca}] {n:>2}/{limite}  {texto}")
        elif secao and linha.startswith("#"):
            secao = None
    print("Tudo dentro do limite." if not erros else f"{erros} texto(s) acima do limite.")
    return erros


if __name__ == "__main__":
    sys.exit(1 if checar(sys.argv[1]) else 0)
