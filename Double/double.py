from os import remove, unlink
import requests
from bs4 import BeautifulSoup
import pyautogui
from datetime import datetime
from time import sleep
import clipboard
from copy import deepcopy
from queue import Empty
from win10toast import ToastNotifier 

notifica = ToastNotifier() 

dados_extraidos = []
lista_extraida = []
lista_de_numeros = []
lista_de_branco = []
total_de_branco = 0
lista_de_cores = []
lista_id = []
lista_jogadas = []
lista_extraida_cores = []

aposta_branco = 1.80

lista_de_conversoes = [
[1, "red"],
[2, "red"],
[3, "red"],
[4, "red"],
[5, "red"],
[6, "red"],
[7, "red"],
[8, "black"],
[9, "black"],
[10, "black"],
[11, "black"],
[12, "black"],
[13, "black"],
[14, "black"],
]
lista_previsoes = []
cor_prevista = ""

def analise_previsao(lista_conversao, lista_numeros, lista_previsao):
    lista_analisada = []
    if lista_numeros[-1] != "white":
        lista_conversao_ = lista_conversao
        lista_numeros_ = lista_numeros
        lista_previsao_ = lista_previsao

        numero = lista_numeros_[-1]
        cor = ""

        for x in lista_conversao_:
            if x[0] == numero:
                cor = x[1]

        lista = [numero + 1, cor]
        lista_previsao_.append(lista)

        for dados in lista_previsao_:
            dados[0] -= 1
            if dados[0] == 0:
                if dados[1] == "red":
                    lista_analisada.append("red/white")
                if dados[1] == "black":
                   lista_analisada.append("black/white")

        return lista_analisada

sequencias_analisadas = [
]


id = ""
contador = 0
captura = False

hora_inicial = datetime.now()

jogada = ""

cor_apostada = ""
valor_ganho = 0
valor_perdido = 0
valor_apostado = 3.60
saldo = 50

maior_valor_dobrado = 0

vitoria = 0
derrota = 0
clique_red = ""
clique_black = ""
clique_branco = ""
clique_quantia = ""
clique_começar = ""


def cliqueRed(click1):
    click1_ = click1
    print("Posicione o mouse em cima do 'Vermelho'...")
    print("Captura em 3 segundos...")
    sleep(3)
    click1_ = pyautogui.position()
    print(f"OK... {str(click1_)}")
    return click1_


def cliqueBlack(click1):
    click1_ = click1
    print("Posicione o mouse em cima do 'Preto'...")
    print("Captura em 3 segundos...")
    sleep(3)
    click1_ = pyautogui.position()
    print(f"OK... {str(click1_)}")
    return click1_


def cliqueWhite(click1):
    click1_ = click1
    print("Posicione o mouse em cima do 'Branco'...")
    print("Captura em 3 segundos...")
    sleep(3)
    click1_ = pyautogui.position()
    print(f"OK... {str(click1_)}")
    return click1_


def cliqueQuantia(click1):
    click1_ = click1
    print("Posicione o mouse em cima da 'Quantia'...")
    print("Captura em 3 segundos...")
    sleep(3)
    click1_ = pyautogui.position()
    print(f"OK... {str(click1_)}")
    return click1_


def cliqueComecar(click1):
    click1_ = click1
    print("Posicione o mouse em cima do 'Começar'...")
    print("Captura em 3 segundos...")
    sleep(3)
    click1_ = pyautogui.position()
    print(f"OK... {str(click1_)}")
    return click1_


def cliqueCamuflar(click3):
    click3_ = click3

    print("Posicione o mouse em algum lugar para camuflar janela...")
    print("Captura em 3 segundos...")
    sleep(3)
    click2_ = pyautogui.position()
    print(f"OK... {str(click2_)}")
    return click2_


clique_camuflar1 = ""
clique_camuflar2 = ""

if captura == True:
    clique_red = cliqueRed(clique_red)
    clique_black = cliqueBlack(clique_black)
    clique_branco = cliqueWhite(clique_branco)
    clique_quantia = cliqueQuantia(clique_quantia)
    clique_começar = cliqueComecar(clique_começar)

def ler_cores(lista_ext):

    lista_ext_ = lista_ext
    lista_ext_.clear()

    arq = open("double.txt")
    linhas = arq.readlines()

    for linha in linhas[0:]:
        linha_ = linha.split(";")

        if linha_ is not Empty:
            new_list = []
            if "white" not in linha_[0]:
                n1 = int(linha_[0].strip())
            else:
                n1 = linha_[0].strip()

            if "white" not in linha_[1]:
                n2 = int(linha_[1].strip())
            else:
                n2 = linha_[1].strip()

            if "white" not in linha_[2]:
                n3 = int(linha_[2].strip())
            else:
                n3 = linha_[2].strip()

            if "white" not in linha_[3]:
                n4 = int(linha_[3].strip())
            else:
                n4 = linha_[3].strip()

            if "white" not in linha_[4]:
                n5 = int(linha_[4].strip())
            else:
                n5 = linha_[4].strip()

            if "white" not in linha_[5]:
                n6 = int(linha_[5].replace("\n", "").strip())
            else:
                n6 = linha_[5].replace("\n", "").strip()

            new_list.append(n1)
            new_list.append(n2)
            new_list.append(n3)
            new_list.append(n4)
            new_list.append(n5)
            new_list.append(n6)

            list_cor = []

            for x in new_list:
                if "white" not in str(x):
                    if x <= 7:
                        list_cor.append("red")
                    elif x >= 7:
                        list_cor.append("black")
                else:
                    list_cor.append("white") 
                
            lista_ext_.append(deepcopy(list_cor))
            new_list.clear()
            list_cor.clear()

    return lista_ext_

def ler_dados(lista_ext):

    lista_ext_ = lista_ext
    lista_ext_.clear()

    arq = open("double.txt")
    linhas = arq.readlines()

    for linha in linhas[0:]:
        linha_ = linha.split(";")

        if linha_ is not Empty:
            new_list = []
            if "white" not in linha_[0]:
                n1 = int(linha_[0].strip())
            else:
                n1 = linha_[0].strip()

            if "white" not in linha_[1]:
                n2 = int(linha_[1].strip())
            else:
                n2 = linha_[1].strip()

            if "white" not in linha_[2]:
                n3 = int(linha_[2].strip())
            else:
                n3 = linha_[2].strip()

            if "white" not in linha_[3]:
                n4 = int(linha_[3].strip())
            else:
                n4 = linha_[3].strip()

            if "white" not in linha_[4]:
                n5 = int(linha_[4].strip())
            else:
                n5 = linha_[4].strip()

            if "white" not in linha_[5]:
                n6 = int(linha_[5].replace("\n", "").strip())
            else:
                n6 = linha_[5].replace("\n", "").strip()

            new_list.append(n1)
            new_list.append(n2)
            new_list.append(n3)
            new_list.append(n4)
            new_list.append(n5)
            new_list.append(n6)

            lista_ext_.append(deepcopy(new_list))
            new_list.clear()

    return lista_ext_


def aposta_cor(lista, lista_dados, lista_cores, lista_dados_cor):

    lista_ = lista
    lista_dados_ = lista_dados
    lista_dados_cor_ = lista_dados_cor
    lista_cores_ = lista_cores

    red_5 = 0
    black_5 = 0
    white_5 = 0
    melhor_jogada_5 = ""

    red_4 = 0
    black_4 = 0
    white_4 = 0
    melhor_jogada_4 = ""

    red_3 = 0
    black_3 = 0
    white_3 = 0
    melhor_jogada_3 = ""

    red_2 = 0
    black_2 = 0
    white_2 = 0
    melhor_jogada_2 = ""

    red_1 = 0
    black_1 = 0
    white_1 = 0
    melhor_jogada_1 = ""

    red_cor_5 = 0
    black_cor_5 = 0
    white_cor_5 = 0
    melhor_jogada_cor_5 = ""

    red_cor_4 = 0
    black_cor_4 = 0
    white_cor_4 = 0
    melhor_jogada_cor_4 = ""

    red_cor_3 = 0
    black_cor_3 = 0
    white_cor_3 = 0
    melhor_jogada_cor_3 = ""

    red_cor_2 = 0
    black_cor_2 = 0
    white_cor_2 = 0
    melhor_jogada_cor_2 = ""

    red_cor_1 = 0
    black_cor_1 = 0
    white_cor_1 = 0
    melhor_jogada_cor_1 = ""

    if len(lista_) >= 5:
        probabilidade_5 = []

        for lista in lista_dados_:
            if lista[0] == lista_[-5]:
                if lista[1] == lista_[-4]:
                    if lista[2] == lista_[-3]:
                        if lista[3] == lista_[-2]:
                            if lista[4] == lista_[-1]:
                                if lista[5] == "white":
                                    probabilidade_5.append("white")
                                elif lista[5] <= 7:
                                    probabilidade_5.append("red")
                                elif lista[5] > 7:
                                    probabilidade_5.append("black")

        for x in probabilidade_5[-2:]:
            if x == "red":
                red_5 += 1
            elif x == "white":
                white_5 += 1
            elif x == "black":
                black_5 += 1

        if red_5 > black_5:
            melhor_jogada_5 = "red"
        elif black_5 > red_5:
            melhor_jogada_5 = "black"
        elif white_5 > red_5:
            melhor_jogada_5 = "white"
        else:
            melhor_jogada_5 = "Não jogar"

        print(
            f"Probabilidade com 05 Casas: Red: {red_5} | Black: {black_5} | White: {white_5} - Jogar no : {melhor_jogada_5}")

    if len(lista_) >= 4:
        probabilidade_4 = []

        for lista in lista_dados_:
            if lista[0] == lista_[-4]:
                if lista[1] == lista_[-3]:
                    if lista[2] == lista_[-2]:
                        if lista[3] == lista_[-1]:
                            if lista[4] == "white":
                                probabilidade_4.append("white")
                            elif lista[4] <= 7:
                                probabilidade_4.append("red")
                            elif lista[4] > 7:
                                probabilidade_4.append("black")

        for x in probabilidade_4[-2:]:
            if x == "red":
                red_4 += 1
            elif x == "white":
                white_4 += 1
            elif x == "black":
                black_4 += 1

        if red_4 > black_4:
            melhor_jogada_4 = "red"
        elif black_4 > red_4:
            melhor_jogada_4 = "black"
        elif white_4 > red_4:
            melhor_jogada_4 = "white"
        else:
            melhor_jogada_4 = "Não jogar"

        print(
            f"Probabilidade com 04 Casas: Red: {red_4} | Black: {black_4} | White: {white_4} - Jogar no : {melhor_jogada_4}")

    if len(lista_) >= 3:
        probabilidade_3 = []

        for lista in lista_dados_:
            if lista[0] == lista_[-3]:
                if lista[1] == lista_[-2]:
                    if lista[2] == lista_[-1]:
                        if lista[3] == "white":
                            probabilidade_3.append("white")
                        elif lista[3] <= 7:
                            probabilidade_3.append("red")
                        elif lista[3] > 7:
                            probabilidade_3.append("black")

        for x in probabilidade_3[-3:]:
            if x == "red":
                red_3 += 1
            elif x == "white":
                white_3 += 1
            elif x == "black":
                black_3 += 1

        if red_3 > black_3:
            melhor_jogada_3 = "red"
        elif black_3 > red_3:
            melhor_jogada_3 = "black"
        elif white_3 > red_3:
            melhor_jogada_3 = "white"
        else:
            melhor_jogada_3 = "Não jogar"

        print(
            f"Probabilidade com 03 Casas: Red: {red_3} | Black: {black_3} | White: {white_3} - Jogar no : {melhor_jogada_3}")

    if len(lista_) >= 2:
        probabilidade_2 = []

        for lista in lista_dados_:
            if lista[0] == lista_[-2]:
                if lista[1] == lista_[-1]:
                    if lista[2] == "white":
                        probabilidade_2.append("white")
                    elif lista[2] <= 7:
                        probabilidade_2.append("red")
                    elif lista[2] > 7:
                        probabilidade_2.append("black")

        for x in probabilidade_2[-5:]:
            if x == "red":
                red_2 += 1
            elif x == "white":
                white_2 += 1
            elif x == "black":
                black_2 += 1

        if red_2 > black_2:
            melhor_jogada_2 = "red"
        elif black_2 > red_2:
            melhor_jogada_2 = "black"
        elif white_2 > red_2:
            melhor_jogada_2 = "white"
        else:
            melhor_jogada_2 = "Não jogar"

        print(
            f"Probabilidade com 02 Casas: Red: {red_2} | Black: {black_2} | White: {white_2} - Jogar no : {melhor_jogada_2}")

    if len(lista_) >= 1:
        probabilidade_1 = []

        for lista in lista_dados_:
            if lista[0] == lista_[-1]:
                if lista[1] == "white":
                    probabilidade_1.append("white")
                elif lista[1] <= 7:
                    probabilidade_1.append("red")
                elif lista[1] > 7:
                    probabilidade_1.append("black")

        for x in probabilidade_1[-5:]:
            if x == "red":
                red_1 += 1
            elif x == "white":
                white_1 += 1
            elif x == "black":
                black_1 += 1

        if red_1 > black_1:
            melhor_jogada_1 = "red"
        elif black_1 > red_1:
            melhor_jogada_1 = "black"
        elif white_1 > red_1:
            melhor_jogada_1 = "white"
        else:
            melhor_jogada_1 = "Não jogar"

        print(
                f"Probabilidade com 01 Casas: Red: {red_1} | Black: {black_1} | White: {white_1} - Jogar no : {melhor_jogada_1}\n")

    """
        try:
            notifica.show_toast("ANALISE", f"04 Casas: Red: {red_4} | Black: {black_4} | White: {white_4}\n03 Casas: Red: {red_3} | Black: {black_3} | White: {white_3}\n02 Casas: Red: {red_2} | Black: {black_2} | White: {white_2}\n01 Casas: Red: {red_1} | Black: {black_1} | White: {white_1}", duration = 4)
        except:
            pass
    """

    if len(lista_) >= 5:
        probabilidade_cor_5 = []

        for lista in lista_dados_cor_:
            if lista[0] == lista_cores_[-5]:
                if lista[1] == lista_cores_[-4]:
                    if lista[2] == lista_cores_[-3]:
                        if lista[3] == lista_cores_[-2]:
                            if lista[4] == lista_cores_[-1]:
                                if lista[5] == "white":
                                    probabilidade_cor_5.append("white")
                                elif lista[5] == "red":
                                    probabilidade_cor_5.append("red")
                                elif lista[5] == "black":
                                    probabilidade_cor_5.append("black")

        for x in probabilidade_cor_5[-2:]:
            if x == "red":
                red_cor_5 += 1
            elif x == "white":
                white_cor_5 += 1
            elif x == "black":
                black_cor_5 += 1

        if red_cor_5 > black_cor_5:
            melhor_jogada_cor_5 = "red"
        elif black_cor_5 > red_cor_5:
            melhor_jogada_cor_5 = "black"
        elif white_cor_5 > red_cor_5:
            melhor_jogada_cor_5 = "white"
        else:
            melhor_jogada_cor_5 = "Não jogar"

        print(
            f"Probabilidade Cor 05 Casas: Red: {red_cor_5} | Black: {black_cor_5} | White: {white_cor_5} - Jogar no : {melhor_jogada_cor_5}")


    if len(lista_) >= 4:
        probabilidade_cor_4 = []

        for lista in lista_dados_cor_:
            if lista[0] == lista_cores_[-4]:
                if lista[1] == lista_cores_[-3]:
                    if lista[2] == lista_cores_[-2]:
                        if lista[3] == lista_cores_[-1]:
                            if lista[4] == "white":
                                probabilidade_cor_4.append("white")
                            elif lista[4] == "red":
                                probabilidade_cor_4.append("red")
                            elif lista[4] == "black":
                                probabilidade_cor_4.append("black")

        for x in probabilidade_cor_4[-2:]:
            if x == "red":
                red_cor_4 += 1
            elif x == "white":
                white_cor_4 += 1
            elif x == "black":
                black_cor_4 += 1

        if red_cor_4 > black_cor_4:
            melhor_jogada_cor_4 = "red"
        elif black_cor_4 > red_cor_4:
            melhor_jogada_cor_4 = "black"
        elif white_cor_4 > red_cor_4:
            melhor_jogada_cor_4 = "white"
        else:
            melhor_jogada_cor_4 = "Não jogar"

        print(
            f"Probabilidade Cor 04 Casas: Red: {red_cor_4} | Black: {black_cor_4} | White: {white_cor_4} - Jogar no : {melhor_jogada_cor_4}")


    if len(lista_) >= 3:
        probabilidade_cor_3 = []

        for lista in lista_dados_cor_:
            if lista[0] == lista_cores_[-3]:
                if lista[1] == lista_cores_[-2]:
                    if lista[2] == lista_cores_[-1]:
                        if lista[3] == "white":
                            probabilidade_cor_3.append("white")
                        elif lista[3] == "red":
                            probabilidade_cor_3.append("red")
                        elif lista[3] == "black":
                            probabilidade_cor_3.append("black")

        for x in probabilidade_cor_3[-3:]:
            if x == "red":
                red_cor_3 += 1
            elif x == "white":
                white_cor_3 += 1
            elif x == "black":
                black_cor_3 += 1

        if red_cor_3 > black_cor_3:
            melhor_jogada_cor_3 = "red"
        elif black_cor_3 > red_cor_3:
            melhor_jogada_cor_3 = "black"
        elif white_cor_3 > red_cor_3:
            melhor_jogada_cor_3 = "white"
        else:
            melhor_jogada_cor_3 = "Não jogar"

        print(f"Probabilidade Cor 03 Casas: Red: {red_cor_3} | Black: {black_cor_3} | White: {white_cor_3} - Jogar no : {melhor_jogada_cor_3}")

    
    if len(lista_) >= 2:
        probabilidade_cor_2 = []

        for lista in lista_dados_cor_:
            if lista[0] == lista_cores_[-2]:
                if lista[1] == lista_cores_[-1]:
                    if lista[2] == "white":
                        probabilidade_cor_2.append("white")
                    elif lista[2] == "red":
                        probabilidade_cor_2.append("red")
                    elif lista[2] == "black":
                        probabilidade_cor_2.append("black")

        for x in probabilidade_cor_2[-5:]:
            if x == "red":
                red_cor_2 += 1
            elif x == "white":
                white_cor_2 += 1
            elif x == "black":
                black_cor_2 += 1

        if red_cor_2 > black_cor_2:
            melhor_jogada_cor_2 = "red"
        elif black_cor_2 > red_cor_2:
            melhor_jogada_cor_2 = "black"
        elif white_cor_2 > red_cor_2:
            melhor_jogada_cor_2 = "white"
        else:
            melhor_jogada_cor_2 = "Não jogar"

        print(
            f"Probabilidade Cor 02 Casas: Red: {red_cor_2} | Black: {black_cor_2} | White: {white_cor_2} - Jogar no : {melhor_jogada_cor_2}")

    if len(lista_) >= 1:
        probabilidade_cor_1 = []

        for lista in lista_dados_cor_:
            if lista[0] == lista_cores_[-1]:
                if lista[1] == "white":
                    probabilidade_cor_1.append("white")
                elif lista[1] == "red":
                    probabilidade_cor_1.append("red")
                elif lista[1] == "black":
                    probabilidade_cor_1.append("black")

        for x in probabilidade_cor_1[-5:]:
            if x == "red":
                red_cor_1 += 1
            elif x == "white":
                white_cor_1 += 1
            elif x == "black":
                black_cor_1 += 1

        if red_cor_1 > black_cor_1:
            melhor_jogada_cor_1 = "red"
        elif black_cor_1 > red_cor_1:
            melhor_jogada_cor_1 = "black"
        elif white_cor_1 > red_cor_1:
            melhor_jogada_cor_1 = "white"
        else:
            melhor_jogada_cor_1 = "Não jogar"

        print(
                f"Probabilidade Cor 01 Casas: Red: {red_cor_1} | Black: {black_cor_1} | White: {white_cor_1} - Jogar no : {melhor_jogada_cor_1}")


        if melhor_jogada_3 == "red" and red_2 - black_2 >= 3 and red_1 - black_1 >= 3:
                notifica.show_toast("ATENÇÂO", "RED/WHITE")
                return "red/white"
      
        if melhor_jogada_3 == "black" and black_2 - red_2 >= 3 and black_1 - red_1 >= 3:
                notifica.show_toast("ATENÇÂO", "BLACK/WHITE")
                return "black/white"

    return ""


while True:
    try:
        # URL de onde vai ser extraido os dados
        url_base = 'https://kitblaze.com/double/'
        response = requests.get(f'{url_base}')
        site = BeautifulSoup(response.text, 'html.parser')
        double = site.find('div', attrs={'pdi'})

        if id != str(double.get_attribute_list("data-id")[0]):
            try:
                cor = str(double.find('img')).split("/")[8].split("-")[0]
                numero = int(double.find("span", attrs={
                             "numero-span"}).get_text())
                tempo = str(double.find('div', attrs={"div-hora"}).get_text())
            except:
                pass

            id = str(double.get_attribute_list("data-id")[0])

            cor = str(double.find('img')).split("/")[8].split("-")[0]
            try:
                numero = int(double.find("span", attrs={
                             "numero-span"}).get_text())
            except:
                pass

            if "white" in cor:
                cor = "white"
                numero = "white"
            try:
                notifica.show_toast(f"Cor do Blaze", f"{cor}", duration = 2)
            except:
                pass

            lista_de_numeros.append(numero)
            dados_extraidos.append(numero)
            lista_de_cores.append(cor)

            if cor == "white":
                list = [cor, tempo]
                lista_de_branco.append(list)

            if cor_apostada != "":
                if cor in cor_apostada:

                    if 'white' in cor:
                        total_de_branco += 1
                        valor_ganho += (1.80 * 14) - valor_apostado
                        print(
                        f"Você ganhou: {(1.80 * 14) - valor_apostado:.2f}\n")
                        saldo += (1.80 * 14) - valor_apostado
                    else:
                        valor_ganho += valor_apostado - 1.80
                        print(
                        f"Você ganhou: {valor_apostado - 1.80:.2f}\n")
                        saldo += valor_apostado - 1.80

                    valor_apostado = 3.6
                    vitoria += 1
                else:
                    print(f"\nVocê perdeu: {valor_apostado:.2f}\n")
                    valor_perdido += valor_apostado + 1.80
                    saldo -= valor_apostado + 1.80

                    derrota += 1
                    valor_apostado = valor_apostado * 2


            try:
                notifica.show_toast("STATUS", f"Vitorias: {vitoria} || Derrotas: {derrota}\n Saldo: {saldo:.2f}\n Maior Valor Dobrado: {maior_valor_dobrado}", duration = 2)
            except:
                pass

            # escreve as informações no arquivo txt
            with open("double.txt", "a+") as file:
                if len(dados_extraidos) >= 6:
                    print("Dados escritos !")
                    file.write(
                        f"{dados_extraidos[-6]}; {dados_extraidos[-5]}; {dados_extraidos[-4]}; {dados_extraidos[-3]}; {dados_extraidos[-2]}; {dados_extraidos[-1]}\n")

            # Faz a leitura do arquivo txt
            lista_extraida = ler_dados(lista_extraida)
            lista_extraida_cores = ler_cores(lista_extraida_cores)

            # Verifica as informações das sequencias e retorna a aposta.
            

            cores_prevista = analise_previsao(lista_de_conversoes, lista_de_numeros, lista_previsoes)

            cor_apostada = aposta_cor(
                lista_de_numeros, lista_extraida, lista_de_cores, lista_extraida_cores)

            if len(lista_de_numeros) >= 3:
                contador = 0
                for x in sequencias_analisadas:
                    if x[0] == lista_de_numeros[-3] and x[1] == lista_de_numeros[-2] and x[2] == lista_de_numeros[-3]:
                        cor_apostada = ""
            
            print(f"\nLista: {dados_extraidos}")
            print(f"Lista: {lista_de_cores}")
            print(f"A Cor é: {cor} - {tempo}")

            if cor_apostada == "red/white":
                print(f"\033[1;31mCor apostada: {cor_apostada}\033[0;0m")
            elif cor_apostada == "black/white":
                print(f"\033[1;33mCor apostada: {cor_apostada}\033[0;0m")
            else:
                print(f"\033[1;34mCor apostada: {cor_apostada}\033[0;0m")

            print(f"Lista de Branco: {lista_de_branco}")
                
            print(f"Cor prevista: {cores_prevista}")
            print(f"Valor atual da aposta: {valor_apostado}")
            print(f"Saldo Atual: {saldo:.2f}")
            print(f"O maior valor dobrado é: R$ {maior_valor_dobrado:.2f}")
            print(f"Valor Ganho: {valor_ganho:.2f} || Valor Perdido: {valor_perdido:.2f}")
            print(f"\033[1;97mTotal de Brancos: {total_de_branco}	\033[0;0m")
            print(f"\033[1;32mVitorias: {vitoria} \033[0;0m|| \033[1;31mDerrotas: {derrota}\n\033[0;0m")

            aposta_branco = 1.8

            if valor_apostado > 9:
                aposta_branco = 3.6

            # verifica qual a maior aposta
            if valor_apostado > maior_valor_dobrado:
                maior_valor_dobrado = valor_apostado

            # Não deixa as listas passar de 10 itens
            if len(lista_de_numeros) >= 15:
                lista_de_numeros = lista_de_numeros[-15:]
                dados_extraidos = dados_extraidos[-15:]
                lista_de_cores = lista_de_cores[-15:]


            if captura == True:
                if cor_apostada != "":
                    if cor_apostada == 'red/white':
                        pyautogui.click(clique_quantia)
                        pyautogui.hotkey("ctrl", "a")
                        pyautogui.hotkey("del")
                        sleep(0.3)
                        if valor_apostado == 1.80:
                            valor_apostado *= 2
                        clipboard.copy(valor_apostado)
                        pyautogui.hotkey("Ctrl", "V")
                        sleep(0.3)
                        pyautogui.click(clique_red)
                        sleep(3.5)
                        pyautogui.click(clique_começar)
                        sleep(0.3)
                        pyautogui.click(clique_quantia)
                        pyautogui.hotkey("ctrl", "a")
                        pyautogui.hotkey("del")
                        sleep(0.3)
                        clipboard.copy(aposta_branco)
                        pyautogui.hotkey("Ctrl", "V")
                        sleep(0.3)
                        pyautogui.click(clique_branco)
                        sleep(0.3)
                        pyautogui.click(clique_começar)

                    if cor_apostada == 'black/white':
                        pyautogui.click(clique_quantia)
                        pyautogui.hotkey("ctrl", "a")
                        pyautogui.hotkey("del")
                        sleep(0.3)
                        if valor_apostado == 1.80:
                            valor_apostado *= 2
                        clipboard.copy(valor_apostado)
                        pyautogui.hotkey("Ctrl", "V")
                        sleep(0.3)
                        pyautogui.click(clique_black)
                        sleep(3.5)
                        pyautogui.click(clique_começar)
                        sleep(0.3)
                        pyautogui.click(clique_quantia)
                        pyautogui.hotkey("ctrl", "a")
                        pyautogui.hotkey("del")
                        sleep(0.3)
                        clipboard.copy(aposta_branco)
                        pyautogui.hotkey("Ctrl", "V")
                        sleep(0.3)
                        pyautogui.click(clique_branco)
                        sleep(0.3)
                        pyautogui.click(clique_começar)

                    if cor_apostada == 'white':
                        pyautogui.click(clique_quantia)
                        pyautogui.hotkey("ctrl", "a")
                        pyautogui.hotkey("del")
                        sleep(0.3)
                        clipboard.copy(aposta_branco)
                        pyautogui.hotkey("Ctrl", "V")
                        sleep(0.3)
                        pyautogui.click(clique_branco)
                        sleep(2)
                        pyautogui.click(clique_começar)
    except:
        print("Falha, por gentileza verifique o site !")
