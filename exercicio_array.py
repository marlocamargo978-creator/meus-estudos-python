"""
Sistema de Notas - Exercício com Arrays.
Demonstra operações básicas com arrays em Python.
"""
import array
import os
import pyfiglet
TAMANHO_LINHA = 65

# 1. Criação do Array
# 'd' significa que vamos guardar numeros decimais (double/float)
# Se fossem inteiros seria usado o 'i'

notas = array.array('d', [8.5, 9.0, 4.5, 6.0, 10.0])
titulo = pyfiglet.figlet_format("SISTEMA DE NOTAS\n", font="sub-zero")
print(titulo)
print(f"--- Notas iniciais: {notas.tolist()} ---\n") # tolist() visualização mais bonita

# 2. Usando APPEND (quando chega uma nota nova)
notas.append(7.5)
print(">>> ADICIONANDO NOTA...") # Oque está acontecendo.
print(f"Adicionada nota 7.5: {notas.tolist()}")
print("-" * TAMANHO_LINHA) # Separador visual

# 3. Usando INSERT (O aluno da primeira posição refez a prova)
notas.insert(0, 9.5)
print(">>> INSERINDO NO INICÍO...")
print(f"Inserida nota 9.5 no inicio: {notas.tolist()}")
print("-" * TAMANHO_LINHA)

# 4. Usando INDEX e POP (Remove uma nota errada especifica)
# Supondo que a nota 4.5 estava errada e precisa sair

try:
    posicao_ruim = notas.index(4.5) # Aqui acha onde esta o 4.5
    nota_removida = notas.pop(posicao_ruim) # Remove pelo indice
    print(">>> NOTA REMOVIDA...")
    print(f"Nota {nota_removida} removida da posição {posicao_ruim}.")
    print("-" * TAMANHO_LINHA)
except ValueError:
    print("Nota não encontrada.")
    print("-" * TAMANHO_LINHA)

# 5. Usando COUNT (Quantos tiraram nota maxima?)
qtd_dez = notas.count(10.0)
print(">>> QUANTIDADE DE NOTAS 10...")
print(f"Quantidade de notas 10.0: {qtd_dez}")
print("-" * TAMANHO_LINHA)

# 6. Slices (Pegar as 3 primeiras notas para analise)
primeiras_tres = notas[:3]
print(">>> PEGANDO AS 3 PRIMEIRAS NOTAS...")
print(f"As 3 primeiras notas são: {primeiras_tres.tolist()}")
print("-" * TAMANHO_LINHA)

# 7. Usando REVERSE (Inverter a ordem)
notas.reverse()
print(">>> INVERTENDO A ORDEM DAS NOTAS")
print(f"Ordem invertida: {notas.tolist()}")
print("-" * TAMANHO_LINHA)

# 8. Técnico: Gravando em arquivo binario (tofile)
# Isso cria um arquivo que nao da pra ler no bloco de notas, só via código
nome_arquivo = "notas_backup.bin"
with open(nome_arquivo, "wb") as arquivo:
    notas.tofile(arquivo)
    print(">>> ARRAY SALVO DE FORMA BINÁRIA...")
    print(f"Array salvo no arquivo '{nome_arquivo}' de forma binaria.")
    print("-" * TAMANHO_LINHA)

# 9. Lendo do arquivo (fromfile) para um novo array
notas_recuperadas = array.array('d') # Cria vazio
with open(nome_arquivo, "rb") as arquivo:
    # Lê o tamanho do arquivo para saber quantos items puxar
    tamanho_arquivo = len(arquivo.read())
    arquivo.seek(0)
    # Cada double ('d') ocupa 8 bytes. Dividimos para saber quantos itens tem.
    qtd_itens = tamanho_arquivo // 8
    notas_recuperadas.fromfile(arquivo, qtd_itens)
print(">>> NOTAS RECUPERADAS...")
print(f"Notas recuperadas do arquivo: {notas_recuperadas.tolist()}")
print("-" * TAMANHO_LINHA)

print("\n--- FINAL DO SISTEMA ---")

# Limpeza (remove o arquivo criado)
os.remove(nome_arquivo)
