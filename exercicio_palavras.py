import os

#Implementar armazenar todas as plavras em uma lista só sem ter que abrir o arquivo mais de uma vez!!!!!!!!!!!!!!!!

pasta = os.getcwd() #dessa forma posso pegar o caminho da pasta atual
arquivos_pasta_atual = os.listdir(pasta)#usado para pegar todos os arquivos da pasta e colocar em um array em forma de str

def uses_only(palavra, lista_arquivo):
    Contagem_palavras_validas = 0
    if contem_letra(palavra, lista_arquivo) == True:
        print(f"\t{palavra}")
        Contagem_palavras_validas+=1
    if(Contagem_palavras_validas == len(palavra)):
        print(f"\t{palavra}")
    return Contagem_palavras_validas
    

def exibir_palavras_all_uses(nome_arquivo_atual, lista_arquivo):
    Total_palavras_validas = 0
    fin = open(f"{nome_arquivo_atual}")
    for palavra in fin:
        pass
    
    return Total_palavras_validas

def exibir_palavras_lista_permitidas(nome_arquivo_atual, lista_permitidas):
    Total_palavras_válidas = 0
    fin = open(f"{nome_arquivo_atual}")
    for palavra in fin:
        palavras_validas = uses_only(palavra, lista_permitidas)
        Total_palavras_válidas += palavras_validas
        
    return Total_palavras_válidas

def uses_only(palavra, lista_permitidas):
    Contagem_palavras_validas = 0
    if contem_letra(palavra, lista_permitidas) == True:
        print(f"\t{palavra}")
        Contagem_palavras_validas+=1
    return Contagem_palavras_validas

def exibir_palavras_lista_proibidas(nome_arquivo_atual, lista_proibidas):
    Total_palavras_válidas = 0
    fin = open(f"{nome_arquivo_atual}")
    for palavra in fin:
        palavras_validas = avoid(lista_proibidas, palavra)
        Total_palavras_válidas += palavras_validas
        
    return Total_palavras_válidas
    
def contem_letra(palavra, lista):
        for i in range(0, len(lista)):
            if lista[i] in palavra:
                return True
        return False

def avoid(lista_proibidas, palavra):
        Contagem_palavras_validas = 0
        if contem_letra(palavra, lista_proibidas) == False:
            print(f"\t{palavra}")
            Contagem_palavras_validas+=1
        return Contagem_palavras_validas

def confirmação_nova_option(option):
    confirmacao = input("\tDeseja fazer uma nova ação?(s/n):")
    if confirmacao == "s" or confirmacao == "S":
        limpar_tela()
        return True
    else:
        return option    
        
def palavras_totais_arquivo(nome_arquivos):
    todas_palavras = open(f"{nome_arquivos}")
    qtd_total_palavras = 0
    for palavra in todas_palavras:
        qtd_total_palavras+=1
    return qtd_total_palavras
    

def palavras_sem_e(nome_arquivos):
    todas_palavras =  open(f"{nome_arquivos}")
    qtd_palavras = 0
    for palavra in todas_palavras:
        if "e" not in palavra:
            print(f"\t{palavra}")
            qtd_palavras += 1
    return qtd_palavras

def exibir_palavras_20_letras(conteudo_arquivos):
    qtd_palavras = 0
    for palavra in conteudo_arquivos:
        if length(palavra) >= 20:
            print(f"\t{palavra}")
            qtd_palavras += 1
    return qtd_palavras
    

def length(palavra):
    letras = 0
    for letra in palavra:
        letras += 1    
    return letras

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    menu = """\t=====================================
\t1 - Ler arquivo
\t2 - Palavras com Até 20 Letras
\t3 - Palavras sem a letra "e"
\t4 - Listar palavras proibidas
\t5 - Palavras com letras selecionadas
\t6 - Palavras com todas as letras selecionadas
\t0 - Sair do Programa
\t====================================="""
    print(menu)

def verificar_estado_arquivo(nome_arquivo):
    nova_tentativa = nome_arquivo
    if nome_arquivo not in arquivos_pasta_atual:
        print(" O arquivo foi digitado incorretamente, tente novamente!")
        nova_tentativa = primeira_option()
        verificar_estado_arquivo(nova_tentativa)
    else:
        return  nova_tentativa

def primeira_option():
    print(f"""
\t======================================
\tOs seguintes arquivos podem ser lidos:""")
    for arquivo in arquivos_pasta_atual:#arquivos pasta atual é uma variável global fora da main!!
        if "txt" in arquivo:
            print(f"""\t{arquivo}""")
    arquivo_selecionado = input("\tInsira o arquivo desejado:")
    arquivo_verificado = verificar_estado_arquivo(arquivo_selecionado)
    return arquivo_verificado
    

def ler_arquivo(arquivo):
    fin = open(f"{arquivo}")
    return fin

def main():

    mostrar_menu()
    option = int(input("\t>>>"))
    
    while(option != 0):
        if(option == 1):
            arquivo_selecionado = primeira_option()
            conteudo_arquivos = ler_arquivo(arquivo_selecionado)
            qtd_palavras_totais = palavras_totais_arquivo(arquivo_selecionado)
            limpar_tela()
            print(f"\tArquivo {arquivo_selecionado} carregado com sucesso!")
            mostrar_menu()
            option = int(input("\t>>>"))
            
        elif (option == 2):
            print("\tAs seguintes palavras contem 20 letras ou mais:")
            palavras_20_letras = exibir_palavras_20_letras(conteudo_arquivos)
            porcentagem_palavras_20_letras = (palavras_20_letras/qtd_palavras_totais)*100
            print(f"\tExistem {palavras_20_letras} palavras com 20 letras no arquivo que equivalem a cerca de {porcentagem_palavras_20_letras}% das palavras totais!")
            cornfirmacao = confirmação_nova_option(option)
            if(cornfirmacao == True):
                mostrar_menu()
                option = int(input("\t>>>"))
            else:
                option = 0
        elif (option == 3):
            qtd_palavras_sem_e = palavras_sem_e(arquivo_selecionado)
            qtd_palavras_totais = palavras_totais_arquivo(arquivo_selecionado)
            porcentagem_palavras_sem_e = (qtd_palavras_sem_e/qtd_palavras_totais)*100
            print(f"\tExistem {qtd_palavras_sem_e} palavras sem a letra \"e\" e elas são cerca de {porcentagem_palavras_sem_e:.2f}% das palavras totais ")
            cornfirmacao = confirmação_nova_option(option)
            if(cornfirmacao == True):
                mostrar_menu()
                option = int(input("\t>>>"))
            else:
                option = 0
        elif (option == 4):
            lista_palavras_proibidas = []
            entrada = 0
            while(entrada != "0"):
                entrada = input("\tInsira a Lista de Letras Proibidas separadas por espaço(0 para encerrar): ")
                for letra in entrada:
                    lista_palavras_proibidas.append(letra)
            qtd_palavras_validas = exibir_palavras_lista_proibidas(arquivo_selecionado, lista_palavras_proibidas)
            porcentagem_palavras_validas = (qtd_palavras_validas/qtd_palavras_totais)*100
            print(f"\tExistem {qtd_palavras_validas} palavras válidas que equivalem a {porcentagem_palavras_validas:.4f}% das palavras totais")
            cornfirmacao = confirmação_nova_option(option)
            if(cornfirmacao == True):
                mostrar_menu()
                option = int(input("\t>>>"))
            else:
                option = 0
        elif(option == 5):
            lista_palavras_permitidas = []
            entrada = 0
            while(entrada != "0"):
                entrada = input("\tInsira a Palavra ou letras que você deseja selecionar na lista:(0 para encerrar)")
                for letra in entrada:
                    lista_palavras_permitidas.append(letra)
            qtd_palavras_validas = exibir_palavras_lista_permitidas(arquivo_selecionado, lista_palavras_permitidas)
            porcentagem_palavras_validas = (qtd_palavras_validas/qtd_palavras_totais)*100
            print(f"\tExistem {qtd_palavras_validas} palavras válidas que equivalem a {porcentagem_palavras_validas:.4f}% das palavras totais")
            cornfirmacao = confirmação_nova_option(option)
            if(cornfirmacao == True):
                mostrar_menu()
                option = int(input("\t>>>"))
            else:
                option = 0
        
        elif(option == 6):
            lista_palavras_permitidas = []
            entrada = 0
            while(entrada != "0"):
                entrada = input("\tInsira a Palavra ou letras que você deseja selecionar na lista:(0 para encerrar)")
                for letra in entrada:
                    lista_palavras_permitidas.append(letra)
            qtd_palavras_validas = exibir_palavras_all_uses(arquivo_selecionado, lista_palavras_permitidas)
            porcentagem_palavras_validas = (qtd_palavras_validas/qtd_palavras_totais)*100
            print(f"\tExistem {qtd_palavras_validas} palavras válidas que equivalem a {porcentagem_palavras_validas:.4f}% das palavras totais")
            cornfirmacao = confirmação_nova_option(option)
            if(cornfirmacao == True):
                mostrar_menu()
                option = int(input("\t>>>"))
            else:
                option = 0
            
main()