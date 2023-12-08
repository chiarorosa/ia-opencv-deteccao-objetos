import os

def split_file(file_path, MB_per_chunk):
    # Verifica se o arquivo existe
    if not os.path.isfile(file_path):
        print("Arquivo não encontrado!")
        return
    
    # Tamanho do chunk em bytes
    chunk_size = MB_per_chunk * 1024 * 1024
    # Contador de partes
    part_number = 1
    
    with open(file_path, 'rb') as f:
        chunk = f.read(chunk_size)
        # Enquanto houver dados, continue criando novos arquivos
        while chunk:
            # Define o nome da parte, com base no número da parte
            part_name = f"{file_path}.part{part_number}"
            with open(part_name, 'wb') as chunk_file:
                chunk_file.write(chunk)
            print(f"Parte {part_number} – {part_name} criada.")
            # Lê o próximo chunk do arquivo
            chunk = f.read(chunk_size)
            part_number += 1

# Solicita informações ao usuário
file_to_split = input("Por favor, insira o caminho do arquivo que deseja dividir: ")
size_in_MB = float(input("Por favor, insira o tamanho de cada parte em MB: "))

# Chama a função para dividir o arquivo
split_file(file_to_split, size_in_MB)