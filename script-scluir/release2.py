import os
import shutil

IGNORE = [
    "dev", 
    "excluir", 
    "scripts", 
    ".git", 
    "Makefile", 
    "bootstrap.css", 
    ".gitkeep"
]

# Nome da nova pasta
nova_pasta = "release"

# Caminho da pasta atual (onde o script está)
pasta_atual = os.path.dirname(os.path.abspath(__file__))
destino = os.path.join(pasta_atual, nova_pasta)

# Cria a nova pasta, se necessário
os.makedirs(destino, exist_ok=True)

# Nome do próprio script, para evitar copiar ele
nome_script = os.path.basename(__file__)

ignore_pastas = ["dev", "excluir", "scripts", ".git", "Makefile", "bootstrap.css", ".gitkeep"]

# Itera por tudo que está na pasta atual
for item in os.listdir(pasta_atual):
    if item == nova_pasta or item == nome_script:
        continue  # Pula a nova pasta e o próprio script
    
    if item in ignore_pastas:
        continue

    caminho_origem = os.path.join(pasta_atual, item)
    caminho_destino = os.path.join(destino, item)

    if os.path.isfile(caminho_origem):
        shutil.copy2(caminho_origem, caminho_destino)
        print(f"Arquivo copiado: {item}")
    elif os.path.isdir(caminho_origem):
        shutil.copytree(caminho_origem, caminho_destino, dirs_exist_ok=True)
        print(f"Pasta copiada: {item}")

print("\n✅ Cópia concluída!")
