from cryptography.fernet import Fernet
import os

# 1. carregando a chave
def carregar_chave():
    return open("chave.key", "rb").read()

# 2. descritografar arquivo 
def descriptografar_arquivo (arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    
    try:
        dados_descriptografados = f.decrypt(dados)
        with open(arquivo, "wb") as file:
            file.write(dados_descriptografados)
    except Exception as e:
        print(f"Falha ao descriptografar {arquivo}: {e}")

# 3. encontrar o arquivo 
def encontrar_aquivos(diretorio):
    lista=[]
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            
            # --- CORREÇÃO APLICADA AQUI ---
            # Pula o script, a chave E a nota de resgate
            if nome == "ransonware.py" or nome == "chave.key" or nome == "lEIA isso.txt":
                continue # Pula para o próximo arquivo na pasta
            
            lista.append(caminho)
            
    return lista

def main():
    chave = carregar_chave()
    arquivos = encontrar_aquivos("test_files")

    # ---- ADICIONE ESTA LINHA PARA DEBUGAR ----
    print(f"Arquivos encontrados para descriptografar: {arquivos}")
    # ------------------------------------------

    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
        print(" Arquivos restaurados com sucesso!") # Lembre-se, isso ainda está no lugar errado (dentro do loop)

if __name__== "__main__":
    main()