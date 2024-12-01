import os
def list_directory_recursive(directory, depth=0):
    try:
        # Lista o conteúdo do diretório
        items = os.listdir(directory)
        for item in items:
            # Caminho completo do item
            full_path = os.path.join(directory, item)

            # Identifica se é arquivo ou diretório
            if os.path.isdir(full_path):
                print(f"{'  ' * depth}[D] {item}")
                # Chamada recursiva para subdiretórios
                list_directory_recursive(full_path, depth + 1)
            else:
                print(f"{'  ' * depth}[F] {item}")
    except PermissionError:
        print(f"{'  ' * depth}[!] Sem permissão para acessar: {directory}")
    except FileNotFoundError:
        print(f"{'  ' * depth}[!] Diretório não encontrado: {directory}")
    except Exception as e:
        print(f"{'  ' * depth}[!] Erro: {e}")


# Exemplo de uso
if __name__ == "__main__":
    directory_to_scan = input("Digite o caminho do diretório a ser percorrido: ")
    if os.path.exists(directory_to_scan) and os.path.isdir(directory_to_scan):
        print(f"Conteúdo do diretório '{directory_to_scan}':")
        list_directory_recursive(directory_to_scan)
    else:
        print("O caminho especificado não é um diretório válido.")
