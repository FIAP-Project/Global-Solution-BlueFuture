import random
from time import sleep

foto_com_microplastico: str = "Com Microplásticos"
foto_sem_microplastico: str = "Sem Microplástico"


def main():
    coordenadas: list = pegar_coordenadas()
    raio: int = pegar_raio_de_analise()

    coord_para_qtd_microplastico: dict = {}
    for coordenada in coordenadas:
        ir_ate_coordenada(coordenada)
        fazer_varredura(raio)
        foto: str = tirar_fotos(10)

        if foto == foto_com_microplastico:
            print('Microplastico detectado')
            amostra: str = coletar_amostra()
            coord_para_qtd_microplastico[coordenada] = pegar_porcentagem_de_microplastico(amostra)
        else:
            print('Nenhum microplástico encontrado')

    print(coord_para_qtd_microplastico)


def pegar_coordenadas() -> list:
    coordenadas: list = []

    print('Digite a coordenada desejada: [X,Z]')
    while True:
        coord_x: float = pegar_coordenada('x')
        coord_z: float = pegar_coordenada('z')

        coordenada: tuple = (coord_x, coord_z)
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
        float(num_str)
        return True
    except ValueError:
        print_vermelho('Erro, digite novamente sem letras e com ponto (.) ao invés de vírgula (,)...')
        return False


def pegar_mais_coordenadas() -> bool:
    while True:
        resposta: str = input('Deseja registrar mais um ponto de coordenada? [S/N]').strip()

        if resposta in 'Ss':
            return True
        elif resposta in 'Nn':
            break
        else:
            print_vermelho('Por favor responda apenas com Ss ou Nn')
            continue

    return False


def pegar_raio_de_analise() -> int:
    while True:
        raio: str = input("Digite o raio de analise do drone: ")

        if numero_inteiro_valido(raio):
            print()
            return int(raio)
        else:
            continue


def ir_ate_coordenada(coordenada: tuple) -> None:
    print(f'Indo até a coordenada {coordenada}...')
    sleep(5)
    print_verde('Coordenada alcançada com sucesso')
    print()


def fazer_varredura(raio: int) -> None:
    print(f'Fazendo varredura num raio de {raio} metros...')
    sleep(5)
    print_verde('Varredura completa com sucesso')
    print()


def tirar_fotos(qtd: int) -> str:
    print(f'Tirando {qtd} fotos...')
    sleep(5)
    print_verde('Fotos tiradas com sucesso')
    print()
    return foto_sem_microplastico if random.randint(0, 1) == 0 else foto_com_microplastico


def coletar_amostra() -> str:
    print('Coletando amostra')
    sleep(5)
    print_verde("Amostra coletada com sucesso")
    print()
    return foto_com_microplastico


def pegar_porcentagem_de_microplastico(amostra: str) -> float:
    if amostra == foto_sem_microplastico:
        return 0

    return float(str(f'{random.uniform(0, 95):.2f}'))


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


if __name__ == "__main__":
    main()
