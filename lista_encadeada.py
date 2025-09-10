class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def adicionar(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            print(f"INFO: Valor {data} adicionado na posição {position}.")
            return

        current_node = self.head
        current_position = 0

        while current_node is not None and current_position < position - 1:
            current_node = current_node.next
            current_position += 1

        if current_node is None:
            print(f"ERRO: Posição {position} é inválida ou fora do alcance da lista.")
        else:
            new_node.next = current_node.next
            current_node.next = new_node
            print(f"INFO: Valor {data} adicionado na posição {position}.")

    def remover(self, data):
        current_node = self.head
        previous_node = None

        if current_node is None:
            print(f"ERRO: Não é possível remover o valor {data}, pois a lista está vazia.")
            return

        if current_node.data == data:
            self.head = current_node.next
            print(f"INFO: Valor {data} removido da lista.")
            return

        while current_node is not None and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            print(f"ERRO: Valor {data} não encontrado na lista.")
        else:
            previous_node.next = current_node.next
            print(f"INFO: Valor {data} removido da lista.")

    def imprimir_lista(self):
        current_node = self.head
        nodes = []
        while current_node is not None:
            nodes.append(str(current_node.data))
            current_node = current_node.next
        
        if nodes:
            print("Lista atual: " + " ".join(nodes))
        else:
            print("Lista atual: (vazia)")


def main():
    lista = LinkedList()

    print("Digite os valores numéricos iniciais da lista (inteiros ou decimais), separados por espaço:")
    try:
        valores_iniciais = list(map(float, input().split()))
        
        for i, valor in enumerate(valores_iniciais):
            lista.adicionar(valor, i)
        print("\nLista inicializada com sucesso!")
        lista.imprimir_lista()

    except ValueError:
        print("Entrada inicial inválida. A lista começará vazia.")

    print("\n--- Menu de Ações ---")
    print("Adicionar: A [numero] [posição]")
    print("Remover:   R [numero]")
    print("Imprimir:  P")
    print("Fechar:    X")
    print("-----------------------\n")

    while True:
        try:
            entrada = input("Digite a ação: ").strip().split()
            acao = entrada[0].upper()

            if acao == 'A':
                if len(entrada) == 3:
                    numero = float(entrada[1])
                    posicao = int(entrada[2])
                    lista.adicionar(numero, posicao)
                else:
                    print("ERRO: Para adicionar, use o formato: A [numero] [posição]")
            
            elif acao == 'R':
                if len(entrada) == 2:
                    numero = float(entrada[1])
                    lista.remover(numero)
                else:
                    print("ERRO: Para remover, use o formato: R [numero]")

            elif acao == 'P':
                lista.imprimir_lista()

            elif acao == 'X':
                print("Programa encerrado.")
                break
            
            else:
                print("ERRO: Ação inválida. Use A, R, P ou X.")

        except (ValueError, IndexError):
            print("ERRO: Entrada inválida. Verifique os números e o formato do comando.")

if __name__ == "__main__":
    main()