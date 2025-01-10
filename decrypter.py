#nota pessoal: odeio python, muito ruim, mesmo....
import os
import pyaes
import hashlib

# Definir a senha
senha = "Sua senha aqui"

# Gerar o hash MD5 e pegar os primeiros 16 caracteres
hash_md5 = hashlib.md5(senha.encode()).hexdigest()
chave = hash_md5[:16].encode()

def descriptografar_arquivo(file_name):
    try:
        with open(file_name, "rb") as file:
            file_data = file.read()
        
        # Inicializar AES com a chave gerada
        aes = pyaes.AESModeOfOperationCTR(chave)
        decrypt_data = aes.decrypt(file_data)
        
        # Criar o arquivo descriptografado
        new_file_name = file_name.replace(".troll", "")
        with open(new_file_name, "wb") as new_file:
            new_file.write(decrypt_data)
        
        # Remover o arquivo criptografado
        os.remove(file_name)
        print(f"Arquivo {file_name} descriptografado com sucesso para {new_file_name}.")
    except Exception as e:
        print(f"Erro ao descriptografar {file_name}: {e}")

# Percorrer todos os arquivos no diretório
for arquivo in os.listdir():
    if arquivo.endswith(".troll"):
        descriptografar_arquivo(arquivo)

print("Processo concluído.")
