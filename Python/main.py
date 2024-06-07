import random

from time import sleep

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import mplcursors
import numpy as np

foto_com_microplastico: str = "Com Microplásticos"
foto_sem_microplastico: str = "Sem Microplástico"


def main():
    coordenadas: list = pegar_coordenadas()
    raio: int = pegar_raio_de_analise()

    coord_para_qtd_microplastico: dict = {}
    for coordenada in coordenadas:
        ir_ate_coordenada(coordenada)
        foto: str = fazer_varredura(raio)

        if foto == foto_com_microplastico:
            print('Microplastico detectado')
            amostra: str = coletar_amostra()
            coord_para_qtd_microplastico[coordenada] = pegar_porcentagem_de_microplastico(amostra)
        else:
            print('Nenhum microplástico encontrado')

    if len(coord_para_qtd_microplastico) > 0:
        print(coord_para_qtd_microplastico)
        criar_grafico(coord_para_qtd_microplastico, raio)


def pegar_coordenadas() -> list:
    coordenadas: list = []

    print('Digite a coordenada desejada: [X,Z]')
    while True:
        coord_x: float = pegar_coordenada('x')
        coord_z: float = pegar_coordenada('z')

        coordenada: tuple = (coord_x, coord_z)

        if coordenadas.__contains__(coordenada):
            print_vermelho('Coordenada já registrada. Por favor insira uma nova.')
            continue
        else:
            coordenadas.append(coordenada)

        print_verde('Coordenada registrada com sucesso!')
        print()

        if pegar_mais_coordenadas():
            continue
        else:
            break

    return coordenadas


def pegar_coordenada(xz: str) -> float:
    while True:
        coord: str = input(f'{xz}: ')

        if coordenada_valida(coord):
            return float(coord)
        else:
            continue


def coordenada_valida(num_str: str) -> bool:
    try:
        f = float(num_str)
        if f >= 1000:
            print_vermelho('Por favor digite uma coordenada menor do que 1000')
            return False

        return True
    except ValueError:
        print_vermelho('Erro, digite novamente sem letras e com ponto (.) ao invés de vírgula (,)...')
        return False


def pegar_mais_coordenadas() -> bool:
    while True:
        resposta: str = input('Deseja registrar mais um ponto de coordenada? [S/N]').strip()

        if resposta == '':
            continue
        elif resposta in 'Ss':
            return True
        elif resposta in 'Nn':
            break
        else:
            print_vermelho('Por favor responda apenas com Ss ou Nn')
            continue

    return False


def pegar_raio_de_analise() -> int:
    while True:
        raio: str = input("Digite o raio de analise do drone em metros: ")

        if numero_inteiro_valido(raio):
            if int(raio) > 100:
                print_vermelho('Por favor digite um raio de analise menor que 100 metros')
                continue
            print()
            return int(raio)
        else:
            continue


def ir_ate_coordenada(coordenada: tuple) -> None:
    print(f'Indo até a coordenada {coordenada}...')
    sleep(5)
    print_verde('Coordenada alcançada com sucesso')
    print()


def fazer_varredura(raio: int) -> str:
    print(f'Fazendo varredura num raio de {raio} metros...')
    foto: str = tirar_fotos(10 * (2 * (raio // 10)) if raio >= 10 else 20)
    print_verde('Varredura completa com sucesso')
    print()
    return foto


def tirar_fotos(qtd: int) -> str:
    print(f'Tirando {qtd} fotos...')
    sleep(5)
    print_verde('Fotos tiradas com sucesso')
    return foto_com_microplastico


def coletar_amostra() -> str:
    print('Coletando amostra')
    sleep(5)
    print_verde("Amostra coletada com sucesso")
    print()
    return foto_com_microplastico


def pegar_porcentagem_de_microplastico(amostra: str) -> float:
    print('Analisando amostra...')
    if amostra == foto_sem_microplastico:
        return 0

    print_verde('Amostra analisada com sucesso')
    print()
    return float(str(f'{random.uniform(5, 95):.2f}'))


def print_verde(arg):
    print(f'\033[32m{arg}\033[m')


def print_vermelho(arg):
    print(f'\033[31m{arg}\033[m')


def numero_inteiro_valido(num_str: str) -> bool:
    try:
        int(num_str)
        return True
    except ValueError:
        print_vermelho('Erro, digite novamente sem letras e um numero inteiro (1, 2, 3)...')
        return False


def criar_grafico(coord_para_qtd_microplastico: dict, raio_de_analise, tamanho_maximo=1000) -> None:
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_facecolor((0, 0, 0.5))

    ax.set_xlim(0, tamanho_maximo)
    ax.set_ylim(0, tamanho_maximo)

    ax.set_xticks(np.arange(0, tamanho_maximo + 1, 100))
    ax.set_yticks(np.arange(0, tamanho_maximo + 1, 100))

    ax.set_aspect('equal')

    colors = [
        (0, 0, 0.5),  # Dark blue
        (0, 0, 1),  # Blue
        (0, 1, 1),  # Cyan
        (0.5, 1, 0.5),  # Light green
        (1, 1, 0),  # Yellow
        (1, 0.5, 0),  # Orange
        (1, 0, 0),  # Red
        (0.5, 0, 0)  # Dark red
    ]
    n_bins = 100
    cmap_name = 'custom_heatmap'
    colormap = mcolors.LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

    norm = mcolors.Normalize(vmin=0, vmax=100)

    raio_circulo = raio_de_analise

    scatter = ax.scatter(
        [coord[0] for coord in coord_para_qtd_microplastico.keys()],
        [coord[1] for coord in coord_para_qtd_microplastico.keys()],
        c=coord_para_qtd_microplastico.values(), cmap=colormap, norm=norm, edgecolor='r'
    )

    for (x, z), porcentagem in coord_para_qtd_microplastico.items():
        cor = colormap(norm(porcentagem))
        ax.plot(x, z, 'ro')
        circle = plt.Circle((x, z), raio_circulo, color=cor, alpha=0.75)
        ax.add_artist(circle)

    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Porcentagem de microplástico')
    cbar.set_ticks(np.arange(0, 101, 10))

    cursor = mplcursors.cursor(scatter, hover=mplcursors.HoverMode.Transient)

    @cursor.connect("add")
    def on_add(sel):
        x, y = sel.target
        percentage = list(coord_para_qtd_microplastico.values())[sel.index]
        sel.annotation.set_text(f'({x:.2f}, {y:.2f}), {percentage:.2f}%')

    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Z')
    plt.title('Mapa de Calor de Microplásticos')
    plt.show()


if __name__ == "__main__":
    main()
