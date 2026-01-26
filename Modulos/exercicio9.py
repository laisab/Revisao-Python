"""
Imagine um arquivo chamado cumprimento.py com o seguinte código:

def dar_oi():
    print("Oi!")

print("Módulo carregado com sucesso!")  # Código solto
dar_oi()                                # Chamada solta

Se você criar um outro arquivo programa.py e fizer apenas import cumprimento, o que vai aparecer no terminal?
"""
print("O print com comentário '# Código solto' e a chamada da função.\nIsso ocorre porque todo o arquivo foi importado")
