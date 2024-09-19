import sys
import time
import datetime
import random
#Organização
def menu():
    divisoria()
    print("1.   Consultar saldo")
    print("2.   Consultar extrato")
    print("3.   Depositar")
    print("4.   Sacar")
    print("5.   Comprar criptomoedas")
    print("6.   Vender criptomoedas")
    print("7.   Atualizar cotação")
    print("8.   Sair")
    divisoria()
def divisoria():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
def consultar_saldo_sem_senha():
    #REAIS
    arquivoreais = open("saldo.txt", "r")
    saldoreais = arquivoreais.read()
    if (saldoreais == ""):
        saldoreais = 0
    saldoreais2 = float(saldoreais)
    arquivoreais.close()
    #BTC
    arquivobtc = open("btc.txt", "r")
    saldobtc = arquivobtc.read()
    if (saldobtc == ""):
        saldobtc = 0
    saldobtc2 = float(saldobtc)
    arquivobtc.close()
    #ETH
    arquivoeth = open("eth.txt", "r")
    saldoeth = arquivoeth.read()
    if (saldoeth == ""):
        saldoeth= 0
    saldoeth2 = float(saldoeth)
    arquivoeth.close()
    #XRP
    arquivoxrp = open("xrp.txt", "r")
    saldoxrp = arquivoxrp.read()
    if (saldoxrp == ""):
        saldoxrp = 0
    saldoxrp2 = float(saldoxrp)
    arquivoxrp.close()
    print(f"Nome: {nome}")
    print(f"CPF: {cpf_str}")
    print("")
    print(f"Reais: {saldoreais2:.2f}")
    print(f"Bitcoin: {saldobtc2:.2f}")
    print(f"Ethereum: {saldoeth2:.2f}")
    print(f"Ripple: {saldoxrp2:.2f}")
    divisoria()
def cotacoes():
    #BTC
    arquivocotacaobtc = open("cotacaobtc.txt", "r")
    cotacaobtc = arquivocotacaobtc.read()
    cotacaobtc2 = int(float(cotacaobtc))
    arquivocotacaobtc.close()
    #ETH
    arquivocotacaoeth = open("cotacaoeth.txt", "r")
    cotacaoeth = arquivocotacaoeth.read()
    cotacaoeth2 = int(float(cotacaoeth))
    arquivocotacaoeth.close()
    #XRP
    arquivocotacaoxrp = open("cotacaoxrp.txt", "r")
    cotacaoxrp = arquivocotacaoxrp.read()
    cotacaoxrp2 = int(float(cotacaoxrp))
    arquivocotacaoxrp.close()
    #PRINT
    print("Cotações atuais:")
    print(f"Bitcoin: R${cotacaobtc2:.2f} ")
    print(f"Ethereum: R${cotacaoeth2:.2f} ")
    print(f"Ripple: R${cotacaoxrp2:.2f} ")
def atualizar_cotacao_ajuda():
    #LER COTAÇÃO BTC
    arquivocotacaobtc = open("cotacaobtc.txt", "r")
    cotacaobtc = arquivocotacaobtc.read()
    cotacaobtc2 = int(float(cotacaobtc))
    arquivocotacaobtc.close()
    # LER COTAÇÃO ETH
    arquivocotacaoeth = open("cotacaoeth.txt", "r")
    cotacaoeth = arquivocotacaoeth.read()
    cotacaoeth2 = int(float(cotacaoeth))
    arquivocotacaoeth.close()
    # LER COTAÇÃO XRP
    arquivocotacaoxrp = open("cotacaoxrp.txt", "r")
    cotacaoxrp = arquivocotacaoxrp.read()
    cotacaoxrp2 = int(float(cotacaoxrp))
    arquivocotacaoxrp.close()
    #ALEATÓRIOS 
    num1 = random.randint(950, 1050)
    num1b = num1/1000
    num2 = random.randint(950, 1050)
    num2b = num2/1000
    num3 = random.randint(950, 1050)
    num3b = num3/1000
    #ALTERAR COTAÇÃO
    novacotacaobtc = str(cotacaobtc2 * num1b)
    novacotacaoeth = str(cotacaoeth2 * num2b)
    novacotacaoxrp = str(cotacaoxrp2 * num3b)
    #SALVAR NOVAS COTAÇÕES
    #BTC
    arquivocotacaobtc = open("cotacaobtc.txt", "w")
    arquivocotacaobtc.write(novacotacaobtc)
    arquivocotacaobtc.close()
    #ETH
    arquivocotacaoeth = open("cotacaoeth.txt", "w")
    arquivocotacaoeth.write(novacotacaoeth)
    arquivocotacaoeth.close()
    #XRP
    arquivocotacaoxrp = open("cotacaoxrp.txt", "w")
    arquivocotacaoxrp.write(novacotacaoxrp)
    arquivocotacaoxrp.close()
    #CONFIRMAÇÃO
    print("Cotações atualizadas com sucesso!")
#Funções 1 a 8
def consultar_saldo():
    while True:
        senha_input = int(input("Digite sua senha: "))
        divisoria()
        if (senha_input != senha_certa):
            print("Senha incorreta, tente novamente.")
            divisoria()
            time.sleep(2)
        elif (senha_input == senha_certa):
            #REAIS
            arquivoreais = open("saldo.txt", "r")
            saldoreais = arquivoreais.read()
            if (saldoreais == ""):
                saldoreais = 0
            saldoreais2 = float(saldoreais)
            arquivoreais.close()
            #BTC
            arquivobtc = open("btc.txt", "r")
            saldobtc = arquivobtc.read()
            if (saldobtc == ""):
                saldobtc = 0
            saldobtc2 = float(saldobtc)
            arquivobtc.close()
            #ETH
            arquivoeth = open("eth.txt", "r")
            saldoeth = arquivoeth.read()
            if (saldoeth == ""):
                saldoeth= 0
            saldoeth2 = float(saldoeth)
            arquivoeth.close()
            #XRP
            arquivoxrp = open("xrp.txt", "r")
            saldoxrp = arquivoxrp.read()
            if (saldoxrp == ""):
                saldoxrp = 0
            saldoxrp2 = float(saldoxrp)
            arquivoxrp.close()
            print(f"Nome: {nome}")
            print(f"CPF: {cpf_str}")
            print("")
            print(f"Reais: {saldoreais2:.2f}")
            print(f"Bitcoin: {saldobtc2}")
            print(f"Ethereum: {saldoeth2}")
            print(f"Ripple: {saldoxrp2}")
            divisoria()
            break
def consultar_extrato():
    print(f"Nome: {nome}")
    print(f"CPF: {cpf_str}")
    print("")
    arquivo = open("extrato.txt", "r")
    for linha in arquivo:
        print(linha.strip())
    arquivo.close()
    divisoria()
def depositar():
    #DEPÓSITO
    arquivo = open("saldo.txt", "r")
    saldo_atual = arquivo.read()
    if (saldo_atual == ""):
        saldo_atual = 0
    arquivo.close()
    deposito = int(input("Valor em reais de deposito: "))
    saldo_novo = float(saldo_atual) + deposito
    #SALVAR SALDO NOVO
    arquivo = open("saldo.txt", "w")
    arquivo.write(str(saldo_novo))
    arquivo.close()
    divisoria()
    #SALVAR NO EXTRATO
    agora = datetime.datetime.now()
    data = agora.strftime("%d-%m-%Y %H:%M")
    #SALDOS
    #REAIS
    arquivoreais = open("saldo.txt", "r")
    saldoreais = arquivoreais.read()
    if (saldoreais == ""):
        saldoreais = 0
    saldoreais2 = float(saldoreais)
    arquivoreais.close()
    #BTC
    arquivobtc = open("btc.txt", "r")
    saldobtc = arquivobtc.read()
    if (saldobtc == ""):
        saldobtc = 0
    saldobtc2 = float(saldobtc)
    arquivobtc.close()
    #ETH
    arquivoeth = open("eth.txt", "r")
    saldoeth = arquivoeth.read()
    if (saldoeth == ""):
        saldoeth= 0
    saldoeth2 = float(saldoeth)
    arquivoeth.close()
    #XRP
    arquivoxrp = open("xrp.txt", "r")
    saldoxrp = arquivoxrp.read()
    if (saldoxrp == ""):
        saldoxrp = 0
    saldoxrp2 = float(saldoxrp)
    arquivoxrp.close()
    #COTAÇÕES
    #BTC
    arquivocotacaobtc = open("cotacaobtc.txt", "r")
    cotacaobtc = arquivocotacaobtc.read()
    cotacaobtc2 = int(float(cotacaobtc))
    arquivocotacaobtc.close()
    #ETH
    arquivocotacaoeth = open("cotacaoeth.txt", "r")
    cotacaoeth = arquivocotacaoeth.read()
    cotacaoeth2 = int(float(cotacaoeth))
    arquivocotacaoeth.close()
    #XRP
    arquivocotacaoxrp = open("cotacaoxrp.txt", "r")
    cotacaoxrp = arquivocotacaoxrp.read()
    cotacaoxrp2 = int(float(cotacaoxrp))
    arquivocotacaoxrp.close()
    arquivo = open("extrato.txt", "a")
    arquivo.write(f"{data} + {deposito:.2f} REAL CT: 0.0   TX: 0.00 REAL: {saldoreais2:.2f} BTC: {saldobtc2:.4f} ETH: {saldoeth2:.4f} XRP: {saldoxrp2:.4f}\n")
    arquivo.close()

    time.sleep(1)
    consultar_saldo_sem_senha()
def sacar():
    arquivo = open("saldo.txt", "r")
    saldo_atual = arquivo.read()
    if (saldo_atual == ""):
        saldo_atual = 0
    arquivo.close()
    saque = float(input("Valor em reais de saque: "))
    if (saque > float(saldo_atual)):
        divisoria()
        print("Saque maior que o saldo.")
        divisoria()
    elif (saque <= float(saldo_atual)):
        saldo_novo = float(saldo_atual) - saque

        arquivo = open("saldo.txt", "w")
        arquivo.write(str(saldo_novo))
        arquivo.close()
        #SALVAR NO EXTRATO
        agora = datetime.datetime.now()
        data = agora.strftime("%d-%m-%Y %H:%M")
        #SALDOS
        #REAIS
        arquivoreais = open("saldo.txt", "r")
        saldoreais = arquivoreais.read()
        if (saldoreais == ""):
            saldoreais = 0
        saldoreais2 = float(saldoreais)
        arquivoreais.close()
        #BTC
        arquivobtc = open("btc.txt", "r")
        saldobtc = arquivobtc.read()
        if (saldobtc == ""):
            saldobtc = 0
        saldobtc2 = float(saldobtc)
        arquivobtc.close()
        #ETH
        arquivoeth = open("eth.txt", "r")
        saldoeth = arquivoeth.read()
        if (saldoeth == ""):
            saldoeth= 0
        saldoeth2 = float(saldoeth)
        arquivoeth.close()
        #XRP
        arquivoxrp = open("xrp.txt", "r")
        saldoxrp = arquivoxrp.read()
        if (saldoxrp == ""):
            saldoxrp = 0
        saldoxrp2 = float(saldoxrp)
        arquivoxrp.close()
        #COTAÇÕES
        #BTC
        arquivocotacaobtc = open("cotacaobtc.txt", "r")
        cotacaobtc = arquivocotacaobtc.read()
        cotacaobtc2 = int(float(cotacaobtc))
        arquivocotacaobtc.close()
        #ETH
        arquivocotacaoeth = open("cotacaoeth.txt", "r")
        cotacaoeth = arquivocotacaoeth.read()
        cotacaoeth2 = int(float(cotacaoeth))
        arquivocotacaoeth.close()
        #XRP
        arquivocotacaoxrp = open("cotacaoxrp.txt", "r")
        cotacaoxrp = arquivocotacaoxrp.read()
        cotacaoxrp2 = int(float(cotacaoxrp))
        arquivocotacaoxrp.close()
        arquivo = open("extrato.txt", "a")
        arquivo.write(f"{data} - {saque:.2f} REAL CT: 0.0   TX: 0.00 REAL: {saldoreais2:.2f} BTC: {saldobtc2:.4f} ETH: {saldoeth2:.4f} XRP: {saldoxrp2:.4f}\n")
        arquivo.close()
        divisoria()
        time.sleep(1)
        consultar_saldo_sem_senha()
def comprar_criptomoedas():
    while True:
        senha_input = int(input("Digite sua senha: "))
        divisoria()
        if (senha_input != senha_certa):
            print("Senha incorreta, tente novamente.")
            divisoria()
            time.sleep(2)
        elif (senha_input == senha_certa):
            cotacoes()
            divisoria()
            time.sleep(2)
            #ESCOLHA DE COMPRA E DE VALOR
            print("Qual cripto deseja comprar?")
            print("1.   Bitcoin")
            print("2.   Ethereum")
            print("3.   Ripple")
            divisoria()
            escolhacripto = int(input(""))
            divisoria()
            print("Qual o valor de compra?")
            valorcompra = int(input(""))
            divisoria()

            #ESCOLHA 1 
            if (escolhacripto == 1):
                #SALDO EM R$
                arquivoreais = open("saldo.txt", "r")
                saldoreais = arquivoreais.read()
                if (saldoreais == ""):
                    saldoreais = 0
                saldoreais2 = float(saldoreais)
                arquivoreais.close()
                #COTAÇÃO BTC
                arquivocotacaobtc = open("cotacaobtc.txt", "r")
                cotacaobtc = arquivocotacaobtc.read()
                cotacaobtc2 = int(float(cotacaobtc))
                arquivocotacaobtc.close()
                #CONTAS 
                if (valorcompra > saldoreais2):
                    print("Saldo insuficiente.")
                    divisoria()
                    break
                elif (valorcompra <= saldoreais2):
                    valorcompra_taxa = (valorcompra * (98/100))
                    novosaldoreais = (saldoreais2 - valorcompra)
                    novosaldocripto = (valorcompra_taxa / cotacaobtc2)
                #SALVAR NOVOS SALDO REAIS
                arquivo = open("saldo.txt", "w")
                arquivo.write(str(novosaldoreais))
                arquivo.close()
                #SALVAR NOVO SALDO BTC
                arquivo = open("btc.txt", "w")
                arquivo.write(str(novosaldocripto))
                arquivo.close()
                #SALVAR NO EXTRATO
                agora = datetime.datetime.now()
                data = agora.strftime("%d-%m-%Y %H:%M")
                #SALDOS
                #REAIS
                arquivoreais = open("saldo.txt", "r")
                saldoreais = arquivoreais.read()
                if (saldoreais == ""):
                    saldoreais = 0
                saldoreais2 = float(saldoreais)
                arquivoreais.close()
                #BTC
                arquivobtc = open("btc.txt", "r")
                saldobtc = arquivobtc.read()
                if (saldobtc == ""):
                    saldobtc = 0
                saldobtc2 = float(saldobtc)
                arquivobtc.close()
                #ETH
                arquivoeth = open("eth.txt", "r")
                saldoeth = arquivoeth.read()
                if (saldoeth == ""):
                    saldoeth= 0
                saldoeth2 = float(saldoeth)
                arquivoeth.close()
                #XRP
                arquivoxrp = open("xrp.txt", "r")
                saldoxrp = arquivoxrp.read()
                if (saldoxrp == ""):
                    saldoxrp = 0
                saldoxrp2 = float(saldoxrp)
                arquivoxrp.close()
                #COTAÇÕES
                #BTC
                arquivocotacaobtc = open("cotacaobtc.txt", "r")
                cotacaobtc = arquivocotacaobtc.read()
                cotacaobtc2 = int(float(cotacaobtc))
                arquivocotacaobtc.close()
                #ETH
                arquivocotacaoeth = open("cotacaoeth.txt", "r")
                cotacaoeth = arquivocotacaoeth.read()
                cotacaoeth2 = int(float(cotacaoeth))
                arquivocotacaoeth.close()
                #XRP
                arquivocotacaoxrp = open("cotacaoxrp.txt", "r")
                cotacaoxrp = arquivocotacaoxrp.read()
                cotacaoxrp2 = int(float(cotacaoxrp))
                arquivocotacaoxrp.close()
                #TAXA
                taxa = (valorcompra - valorcompra_taxa)/100
                arquivo = open("extrato.txt", "a")
                arquivo.write(f"{data} + {valorcompra:.2f} BTC CT: {cotacaobtc2:.2f}   TX: {taxa} REAL: {saldoreais2:.2f} BTC: {saldobtc2:.4f} ETH: {saldoeth2:.4f} XRP: {saldoxrp2:.4f}\n")
                arquivo.close()
                #Confirmação
                print("Cripto Comprada, houve uma taxação de 2%.")
                divisoria()
                break
            elif (escolhacripto == 2):
                #SALDO EM R$
                arquivoreais = open("saldo.txt", "r")
                saldoreais = arquivoreais.read()
                if (saldoreais == ""):
                    saldoreais = 0
                saldoreais2 = float(saldoreais)
                arquivoreais.close()
                #ETH
                arquivocotacaoeth = open("cotacaoeth.txt", "r")
                cotacaoeth = arquivocotacaoeth.read()
                cotacaoeth2 = int(float(cotacaoeth))
                arquivocotacaoeth.close()
                #CONTAS 
                if (valorcompra > saldoreais2):
                    print("Saldo insuficiente.")
                    divisoria()
                    break
                elif (valorcompra <= saldoreais2):
                    valorcompra_taxa = (valorcompra * (99/100))
                    novosaldoreais = (saldoreais2 - valorcompra)
                    novosaldocripto = (valorcompra_taxa / cotacaoeth2)
                #SALVAR NOVOS SALDO REAIS
                arquivo = open("saldo.txt", "w")
                arquivo.write(str(novosaldoreais))
                arquivo.close()
                #SALVAR NOVO SALDO ETH
                arquivo = open("eth.txt", "w")
                arquivo.write(str(novosaldocripto))
                arquivo.close()
                #SALVAR NO EXTRATO
                agora = datetime.datetime.now()
                data = agora.strftime("%d-%m-%Y %H:%M")
                #SALDOS
                #REAIS
                arquivoreais = open("saldo.txt", "r")
                saldoreais = arquivoreais.read()
                if (saldoreais == ""):
                    saldoreais = 0
                saldoreais2 = float(saldoreais)
                arquivoreais.close()
                #BTC
                arquivobtc = open("btc.txt", "r")
                saldobtc = arquivobtc.read()
                if (saldobtc == ""):
                    saldobtc = 0
                saldobtc2 = float(saldobtc)
                arquivobtc.close()
                #ETH
                arquivoeth = open("eth.txt", "r")
                saldoeth = arquivoeth.read()
                if (saldoeth == ""):
                    saldoeth= 0
                saldoeth2 = float(saldoeth)
                arquivoeth.close()
                #XRP
                arquivoxrp = open("xrp.txt", "r")
                saldoxrp = arquivoxrp.read()
                if (saldoxrp == ""):
                    saldoxrp = 0
                saldoxrp2 = float(saldoxrp)
                arquivoxrp.close()
                #COTAÇÕES
                #BTC
                arquivocotacaobtc = open("cotacaobtc.txt", "r")
                cotacaobtc = arquivocotacaobtc.read()
                cotacaobtc2 = int(float(cotacaobtc))
                arquivocotacaobtc.close()
                #ETH
                arquivocotacaoeth = open("cotacaoeth.txt", "r")
                cotacaoeth = arquivocotacaoeth.read()
                cotacaoeth2 = int(float(cotacaoeth))
                arquivocotacaoeth.close()
                #XRP
                arquivocotacaoxrp = open("cotacaoxrp.txt", "r")
                cotacaoxrp = arquivocotacaoxrp.read()
                cotacaoxrp2 = int(float(cotacaoxrp))
                arquivocotacaoxrp.close()
                #TAXA
                taxa = (valorcompra - valorcompra_taxa)/100
                arquivo = open("extrato.txt", "a")
                arquivo.write(f"{data} + {valorcompra:.2f} ETH CT: {cotacaoeth2:.2f}   TX: {taxa} REAL: {saldoreais2:.2f} BTC: {saldobtc2:.4f} ETH: {saldoeth2:.4f} XRP: {saldoxrp2:.4f}\n")
                arquivo.close()
                #Confirmação
                print("Cripto Comprada, houve uma taxação de 1%.")
                divisoria()
                break
            elif (escolhacripto == 3):
                #SALDO EM R$
                arquivoreais = open("saldo.txt", "r")
                saldoreais = arquivoreais.read()
                if (saldoreais == ""):
                    saldoreais = 0
                saldoreais2 = float(saldoreais)
                arquivoreais.close()
                #XRP
                arquivocotacaoxrp = open("cotacaoxrp.txt", "r")
                cotacaoxrp = arquivocotacaoxrp.read()
                cotacaoxrp2 = int(float(cotacaoxrp))
                arquivocotacaoxrp.close()
                #CONTAS 
                if (valorcompra > saldoreais2):
                    print("Saldo insuficiente.")
                    divisoria()
                    break
                elif (valorcompra <= saldoreais2):
                    valorcompra_taxa = (valorcompra * (99/100))
                    novosaldoreais = (saldoreais2 - valorcompra)
                    novosaldocripto = (valorcompra_taxa / cotacaoxrp2)
                #SALVAR NOVOS SALDO REAIS
                arquivo = open("saldo.txt", "w")
                arquivo.write(str(novosaldoreais))
                arquivo.close()
                #SALVAR NOVO SALDO XRP
                arquivo = open("xrp.txt", "w")
                arquivo.write(str(novosaldocripto))
                arquivo.close()
                #SALVAR NO EXTRATO
                agora = datetime.datetime.now()
                data = agora.strftime("%d-%m-%Y %H:%M")
                #SALDOS
                #REAIS
                arquivoreais = open("saldo.txt", "r")
                saldoreais = arquivoreais.read()
                if (saldoreais == ""):
                    saldoreais = 0
                saldoreais2 = float(saldoreais)
                arquivoreais.close()
                #BTC
                arquivobtc = open("btc.txt", "r")
                saldobtc = arquivobtc.read()
                if (saldobtc == ""):
                    saldobtc = 0
                saldobtc2 = float(saldobtc)
                arquivobtc.close()
                #ETH
                arquivoeth = open("eth.txt", "r")
                saldoeth = arquivoeth.read()
                if (saldoeth == ""):
                    saldoeth= 0
                saldoeth2 = float(saldoeth)
                arquivoeth.close()
                #XRP
                arquivoxrp = open("xrp.txt", "r")
                saldoxrp = arquivoxrp.read()
                if (saldoxrp == ""):
                    saldoxrp = 0
                saldoxrp2 = float(saldoxrp)
                arquivoxrp.close()
                #COTAÇÕES
                #BTC
                arquivocotacaobtc = open("cotacaobtc.txt", "r")
                cotacaobtc = arquivocotacaobtc.read()
                cotacaobtc2 = int(float(cotacaobtc))
                arquivocotacaobtc.close()
                #ETH
                arquivocotacaoeth = open("cotacaoeth.txt", "r")
                cotacaoeth = arquivocotacaoeth.read()
                cotacaoeth2 = int(float(cotacaoeth))
                arquivocotacaoeth.close()
                #XRP
                arquivocotacaoxrp = open("cotacaoxrp.txt", "r")
                cotacaoxrp = arquivocotacaoxrp.read()
                cotacaoxrp2 = int(float(cotacaoxrp))
                arquivocotacaoxrp.close()
                #TAXA
                taxa = (valorcompra - valorcompra_taxa)/100
                arquivo = open("extrato.txt", "a")
                arquivo.write(f"{data} + {valorcompra:.2f} XRP CT: {cotacaoxrp2:.2f}   TX: {taxa} REAL: {saldoreais2:.2f} BTC: {saldobtc2:.4f} ETH: {saldoeth2:.4f} XRP: {saldoxrp2:.4f}\n")
                arquivo.close()
                #Confirmação
                print("Cripto Comprada, houve uma taxação de 1%.")
                divisoria()
                break
            else:
                print("Resposta não reconhecida, tente novamente.")
                break
def vender_criptomoedas():
    while True:
        senha_input = int(input("Digite sua senha: "))
        divisoria()
        if (senha_input != senha_certa):
            print("Senha incorreta, tente novamente.")
            divisoria()
            time.sleep(2)
        elif (senha_input == senha_certa):
            cotacoes()
            divisoria()
            time.sleep(2)
            #ESCOLHA DE VENDA E DE VALOR
            print("Qual cripto deseja vender?")
            print("1.   Bitcoin")
            print("2.   Ethereum")
            print("3.   Ripple")
            divisoria()
            escolhacripto = int(input(""))
            divisoria()
            print("Qual o valor de venda?")
            valorvendas = float(input(""))
            divisoria()
            
            #ESCOLHA 1
            if (escolhacripto == 1):
                #REAIS
                arquivoreais = open("saldo.txt", "r")
                saldoreais = arquivoreais.read()
                if (saldoreais == ""):
                    saldoreais = 0
                saldoreais2 = float(saldoreais)
                arquivoreais.close()
                #SALDO BTC
                arquivobtc = open("btc.txt", "r")
                saldobtc = arquivobtc.read()
                if (saldobtc == ""):
                    saldobtc = 0
                saldobtc2 = float(saldobtc)
                arquivobtc.close()
                #COTAÇÃO BTC
                arquivocotacaobtc = open("cotacaobtc.txt", "r")
                cotacaobtc = arquivocotacaobtc.read()
                cotacaobtc2 = int(float(cotacaobtc))
                arquivocotacaobtc.close()
                #CONTAS
                if (valorvendas > saldobtc2):
                    print("Saldo insuficiente.")
                    divisoria()
                    break
                elif (valorvendas <= saldobtc2):
                    valorvenda_taxa = (valorvendas * (97/100))
                    novosaldocripto = (saldobtc2 - valorvendas)
                    novosaldoreais = (valorvenda_taxa * cotacaobtc2) + saldoreais2
                #SALVAR NOVO SALDOS REAIS
                arquivo = open("saldo.txt", "w")
                arquivo.write(str(novosaldoreais))
                arquivo.close()
                #SALVAR NOVO SALDO BTC
                arquivo = open("btc.txt", "w")
                arquivo.write(str(novosaldocripto))
                arquivo.close()
                #SALVAR NO EXTRATO
                agora = datetime.datetime.now()
                data = agora.strftime("%d-%m-%Y %H:%M")
                #SALDOS
                #REAIS
                arquivoreais = open("saldo.txt", "r")
                saldoreais = arquivoreais.read()
                if (saldoreais == ""):
                    saldoreais = 0
                saldoreais2 = float(saldoreais)
                arquivoreais.close()
                #BTC
                arquivobtc = open("btc.txt", "r")
                saldobtc = arquivobtc.read()
                if (saldobtc == ""):
                    saldobtc = 0
                saldobtc2 = float(saldobtc)
                arquivobtc.close()
                #ETH
                arquivoeth = open("eth.txt", "r")
                saldoeth = arquivoeth.read()
                if (saldoeth == ""):
                    saldoeth= 0
                saldoeth2 = float(saldoeth)
                arquivoeth.close()
                #XRP
                arquivoxrp = open("xrp.txt", "r")
                saldoxrp = arquivoxrp.read()
                if (saldoxrp == ""):
                    saldoxrp = 0
                saldoxrp2 = float(saldoxrp)
                arquivoxrp.close()
                #COTAÇÕES
                #BTC
                arquivocotacaobtc = open("cotacaobtc.txt", "r")
                cotacaobtc = arquivocotacaobtc.read()
                cotacaobtc2 = int(float(cotacaobtc))
                arquivocotacaobtc.close()
                #ETH
                arquivocotacaoeth = open("cotacaoeth.txt", "r")
                cotacaoeth = arquivocotacaoeth.read()
                cotacaoeth2 = int(float(cotacaoeth))
                arquivocotacaoeth.close()
                #XRP
                arquivocotacaoxrp = open("cotacaoxrp.txt", "r")
                cotacaoxrp = arquivocotacaoxrp.read()
                cotacaoxrp2 = int(float(cotacaoxrp))
                arquivocotacaoxrp.close()
                #TAXA
                taxa = (valorvendas - valorvenda_taxa)/100
                arquivo = open("extrato.txt", "a")
                arquivo.write(f"{data} - {valorvendas:.2f} BTC CT: {cotacaobtc2:.2f}   TX: {taxa} REAL: {saldoreais2:.2f} BTC: {saldobtc2:.4f} ETH: {saldoeth2:.4f} XRP: {saldoxrp2:.4f}\n")
                arquivo.close()
                #Confirmação
                print("Cripto vendida, houve uma taxação de 3%.")
                divisoria()
                break
            if (escolhacripto == 2):
                #REAIS
                arquivoreais = open("saldo.txt", "r")
                saldoreais = arquivoreais.read()
                if (saldoreais == ""):
                    saldoreais = 0
                saldoreais2 = float(saldoreais)
                arquivoreais.close()
                #SALDO ETH
                arquivoeth = open("eth.txt", "r")
                saldoeth = arquivoeth.read()
                if (saldoeth == ""):
                    saldoeth= 0
                saldoeth2 = float(saldoeth)
                arquivoeth.close()
                #COTAÇÃO ETH
                arquivocotacaoeth = open("cotacaoeth.txt", "r")
                cotacaoeth = arquivocotacaoeth.read()
                cotacaoeth2 = int(float(cotacaoeth))
                arquivocotacaoeth.close()
                #CONTAS
                if (valorvendas > saldoeth2):
                    print("Saldo insuficiente.")
                    divisoria()
                    break
                elif (valorvendas <= saldoeth2):
                    valorvenda_taxa = (valorvendas * (98/100))
                    novosaldocripto = (saldoeth2 - valorvendas)
                    novosaldoreais = (valorvenda_taxa * cotacaoeth2) + saldoreais2
                #SALVAR NOVO SALDOS REAIS
                arquivo = open("saldo.txt", "w")
                arquivo.write(str(novosaldoreais))
                arquivo.close()
                #SALVAR NOVO SALDO ETH
                arquivo = open("eth.txt", "w")
                arquivo.write(str(novosaldocripto))
                arquivo.close()
                #SALVAR NO EXTRATO
                agora = datetime.datetime.now()
                data = agora.strftime("%d-%m-%Y %H:%M")
                #SALDOS
                #REAIS
                arquivoreais = open("saldo.txt", "r")
                saldoreais = arquivoreais.read()
                if (saldoreais == ""):
                    saldoreais = 0
                saldoreais2 = float(saldoreais)
                arquivoreais.close()
                #BTC
                arquivobtc = open("btc.txt", "r")
                saldobtc = arquivobtc.read()
                if (saldobtc == ""):
                    saldobtc = 0
                saldobtc2 = float(saldobtc)
                arquivobtc.close()
                #ETH
                arquivoeth = open("eth.txt", "r")
                saldoeth = arquivoeth.read()
                if (saldoeth == ""):
                    saldoeth= 0
                saldoeth2 = float(saldoeth)
                arquivoeth.close()
                #XRP
                arquivoxrp = open("xrp.txt", "r")
                saldoxrp = arquivoxrp.read()
                if (saldoxrp == ""):
                    saldoxrp = 0
                saldoxrp2 = float(saldoxrp)
                arquivoxrp.close()
                #COTAÇÕES
                #BTC
                arquivocotacaobtc = open("cotacaobtc.txt", "r")
                cotacaobtc = arquivocotacaobtc.read()
                cotacaobtc2 = int(float(cotacaobtc))
                arquivocotacaobtc.close()
                #ETH
                arquivocotacaoeth = open("cotacaoeth.txt", "r")
                cotacaoeth = arquivocotacaoeth.read()
                cotacaoeth2 = int(float(cotacaoeth))
                arquivocotacaoeth.close()
                #XRP
                arquivocotacaoxrp = open("cotacaoxrp.txt", "r")
                cotacaoxrp = arquivocotacaoxrp.read()
                cotacaoxrp2 = int(float(cotacaoxrp))
                arquivocotacaoxrp.close()
                #TAXA
                taxa = (valorvendas - valorvenda_taxa)/100
                arquivo = open("extrato.txt", "a")
                arquivo.write(f"{data} - {valorvendas:.2f} eth CT: {cotacaoeth2:.2f}   TX: {taxa} REAL: {saldoreais2:.2f} BTC: {saldobtc2:.4f} ETH: {saldoeth2:.4f} XRP: {saldoxrp2:.4f}\n")
                arquivo.close()
                #Confirmação
                print("Cripto vendida, houve uma taxação de 2%.")
                divisoria()
                break
            if (escolhacripto == 3):
                #REAIS
                arquivoreais = open("saldo.txt", "r")
                saldoreais = arquivoreais.read()
                if (saldoreais == ""):
                    saldoreais = 0
                saldoreais2 = float(saldoreais)
                arquivoreais.close()
                #SALDO XRP
                arquivoxrp = open("xrp.txt", "r")
                saldoxrp = arquivoxrp.read()
                if (saldoxrp == ""):
                    saldoxrp = 0
                saldoxrp2 = float(saldoxrp)
                arquivoxrp.close()
                #COTAÇÃO XRP
                arquivocotacaoxrp = open("cotacaoxrp.txt", "r")
                cotacaoxrp = arquivocotacaoxrp.read()
                cotacaoxrp2 = int(float(cotacaoxrp))
                arquivocotacaoxrp.close()
                #CONTAS
                if (valorvendas > saldoxrp2):
                    print("Saldo insuficiente.")
                    divisoria()
                    break
                elif (valorvendas <= saldoxrp2):
                    valorvenda_taxa = (valorvendas * (99/100))
                    novosaldocripto = (saldoxrp2 - valorvendas)
                    novosaldoreais = (valorvenda_taxa * cotacaoxrp2) + saldoreais2
                #SALVAR NOVO SALDOS REAIS
                arquivo = open("saldo.txt", "w")
                arquivo.write(str(novosaldoreais))
                arquivo.close()
                #SALVAR NOVO SALDO XRP
                arquivo = open("xrp.txt", "w")
                arquivo.write(str(novosaldocripto))
                arquivo.close()
                #SALVAR NO EXTRATO
                agora = datetime.datetime.now()
                data = agora.strftime("%d-%m-%Y %H:%M")
                #SALDOS
                #REAIS
                arquivoreais = open("saldo.txt", "r")
                saldoreais = arquivoreais.read()
                if (saldoreais == ""):
                    saldoreais = 0
                saldoreais2 = float(saldoreais)
                arquivoreais.close()
                #BTC
                arquivobtc = open("btc.txt", "r")
                saldobtc = arquivobtc.read()
                if (saldobtc == ""):
                    saldobtc = 0
                saldobtc2 = float(saldobtc)
                arquivobtc.close()
                #ETH
                arquivoeth = open("eth.txt", "r")
                saldoeth = arquivoeth.read()
                if (saldoeth == ""):
                    saldoeth= 0
                saldoeth2 = float(saldoeth)
                arquivoeth.close()
                #XRP
                arquivoxrp = open("xrp.txt", "r")
                saldoxrp = arquivoxrp.read()
                if (saldoxrp == ""):
                    saldoxrp = 0
                saldoxrp2 = float(saldoxrp)
                arquivoxrp.close()
                #COTAÇÕES
                #BTC
                arquivocotacaobtc = open("cotacaobtc.txt", "r")
                cotacaobtc = arquivocotacaobtc.read()
                cotacaobtc2 = int(float(cotacaobtc))
                arquivocotacaobtc.close()
                #ETH
                arquivocotacaoeth = open("cotacaoeth.txt", "r")
                cotacaoeth = arquivocotacaoeth.read()
                cotacaoeth2 = int(float(cotacaoeth))
                arquivocotacaoeth.close()
                #XRP
                arquivocotacaoxrp = open("cotacaoxrp.txt", "r")
                cotacaoxrp = arquivocotacaoxrp.read()
                cotacaoxrp2 = int(float(cotacaoxrp))
                arquivocotacaoxrp.close()
                #TAXA
                taxa = (valorvendas - valorvenda_taxa)/100
                arquivo = open("extrato.txt", "a")
                arquivo.write(f"{data} - {valorvendas:.2f} XRP CT: {cotacaoxrp2:.2f}   TX: {taxa} REAL: {saldoreais2:.2f} BTC: {saldobtc2:.4f} ETH: {saldoeth2:.4f} XRP: {saldoxrp2:.4f}\n")
                arquivo.close()
                #Confirmação
                print("Cripto vendida, houve uma taxação de 1%.")
                divisoria()
                break
            else:
                print("Resposta não reconhecida, tente novamente.")
                break
def atualizar_cotacao():
    atualizar_cotacao_ajuda()
    divisoria()
def sair():
    print("Saída efetuada com sucesso, até a proxima!")
    divisoria()
    sys.exit()
#Login e Dados
nome = "Bruno Kenez"
cpf_certo = 40184326826
cpf_str = "401.843.268-26"
senha_certa = 123456
#Code
while True:
    cpf = int(input("Digite o CPF: "))
    senha = int(input("Digite sua senha: "))

    if (cpf == cpf_certo) and (senha == senha_certa):
        divisoria()
        print("Login efetuado com sucesso, Bem vindo!")
        break
    elif (cpf == cpf_certo) and (senha != senha_certa):
        divisoria()
        print("Senha incorreta, tente novamente.")
        time.sleep(2)
    elif (cpf != cpf_certo) and (senha == senha_certa):
        divisoria()
        print("CPF incorreto, tente novamente.")
        time.sleep(2)
    else:
        divisoria()
        print("CPF e senha incorretos, tente novamente.")
        time.sleep(2)

while True:
    menu()
    escolha = int(input(""))
    divisoria()
    if (escolha == 1):
        consultar_saldo()
        while True:
            time.sleep(5)
            print("1.   Voltar ao Menu")
            print("2.   Fechar Programa")
            divisoria()
            escolha2 = (input(""))
            if (escolha2 == "1"):
                break
            elif (escolha2 == "2"):
                divisoria()
                sair()
            else:
                divisoria()
                print("Resposta não reconhecida, tente novamente.")
                divisoria()
    elif (escolha == 2):
        consultar_extrato()
        while True:
            time.sleep(5)
            print("1.   Voltar ao Menu")
            print("2.   Fechar Programa")
            divisoria()
            escolha2 = (input(""))
            if (escolha2 == "1"):
                break
            elif (escolha2 == "2"):
                divisoria()
                sair()
            else:
                divisoria()
                print("Resposta não reconhecida, tente novamente.")
                divisoria()
    elif (escolha == 3):
        depositar()
        while True:
            time.sleep(5)
            print("1.   Voltar ao Menu")
            print("2.   Fechar Programa")
            divisoria()
            escolha2 = (input(""))
            if (escolha2 == "1"):
                break
            elif (escolha2 == "2"):
                divisoria()
                sair()
            else:
                divisoria()
                print("Resposta não reconhecida, tente novamente.")
                divisoria()
    elif (escolha == 4):
        sacar()
        while True:
            time.sleep(5)
            print("1.   Voltar ao Menu")
            print("2.   Fechar Programa")
            divisoria()
            escolha2 = (input(""))
            if (escolha2 == "1"):
                break
            elif (escolha2 == "2"):
                divisoria()
                sair()
            else:
                divisoria()
                print("Resposta não reconhecida, tente novamente.")
                divisoria()
    elif (escolha == 5):
        comprar_criptomoedas()
        while True:
            time.sleep(5)
            print("1.   Voltar ao Menu")
            print("2.   Fechar Programa")
            divisoria()
            escolha2 = (input(""))
            if (escolha2 == "1"):
                break
            elif (escolha2 == "2"):
                divisoria()
                sair()
            else:
                divisoria()
                print("Resposta não reconhecida, tente novamente.")
                divisoria()
    elif (escolha == 6):
        vender_criptomoedas()
        while True:
            time.sleep(5)
            print("1.   Voltar ao Menu")
            print("2.   Fechar Programa")
            divisoria()
            escolha2 = (input(""))
            if (escolha2 == "1"):
                break
            elif (escolha2 == "2"):
                divisoria()
                sair()
            else:
                divisoria()
                print("Resposta não reconhecida, tente novamente.")
                divisoria()
    elif (escolha == 7):
        atualizar_cotacao()
        while True:
            time.sleep(5)
            print("1.   Voltar ao Menu")
            print("2.   Fechar Programa")
            divisoria()
            escolha2 = (input(""))
            if (escolha2 == "1"):
                break
            elif (escolha2 == "2"):
                divisoria()
                sair()
            else:
                divisoria()
                print("Resposta não reconhecida, tente novamente")
                divisoria()
    elif (escolha == 8):
        sair()
