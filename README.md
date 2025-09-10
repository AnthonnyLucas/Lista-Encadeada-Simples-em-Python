# Lista Encadeada Simples em Python

Este projeto consiste na implementação de uma estrutura de dados de Lista Encadeada Simples em Python, desenvolvida para ser uma ferramenta didática e funcional para manipulação de coleções de dados numéricos (inteiros e de ponto flutuante). A aplicação permite que o usuário realize as operações fundamentais de uma lista, como adicionar e remover elementos em posições específicas, além de visualizar o estado atual da lista a qualquer momento. O código é estruturado de forma clara em duas classes principais: Node, que representa cada elemento individual da lista, e LinkedList, que gerencia o conjunto de nós e encapsula toda a lógica das operações. O programa é interativo e executado via linha de comando (CLI), oferecendo um menu simples onde o usuário pode inicializar a lista com valores pré-definidos e, em seguida, manipular a lista dinamicamente através de comandos intuitivos. Além da funcionalidade básica, o projeto inclui um tratamento robusto de erros para entradas inválidas, como posições fora do alcance ou formatos de comando incorretos, garantindo uma experiência de usuário estável e informativa. É uma excelente demonstração prática dos conceitos de ponteiros, alocação dinâmica de memória e manipulação de estruturas de dados fundamentais da ciência da computação.

## Descrição

A aplicação foi desenvolvida com o objetivo de demonstrar de forma prática o funcionamento e a manipulação de uma lista encadeada. Ela permite que o usuário inicie a lista com uma sequência de números e, em seguida, utilize comandos simples para adicionar novos valores em posições específicas ou remover valores existentes. O código é estruturado de maneira clara e inclui tratamento de erros para garantir uma interação robusta com o usuário.

## Funcionalidades

* **Inicialização Dinâmica:** Permite que o usuário insira os valores iniciais da lista ao iniciar o programa.
* **Adicionar Elemento:** Adiciona um número em qualquer posição válida da lista (`A [numero] [posição]`).
* **Remover Elemento:** Remove a primeira ocorrência de um número específico da lista (`R [numero]`).
* **Imprimir Lista:** Exibe todos os elementos da lista em sua ordem atual (`P`).
* **Interface Interativa:** Menu simples e claro para interação via terminal.
* **Tratamento de Erros:** Valida as entradas do usuário para evitar que o programa quebre com comandos ou valores inválidos.

## Requisitos

Para executar este projeto, você precisará ter o **Python 3** instalado em sua máquina. Nenhuma outra dependência ou biblioteca externa é necessária.

### Verificando a Instalação do Python

Abra seu terminal ou prompt de comando e execute um dos seguintes comandos. Se o Python estiver instalado, ele retornará a versão.

```bash
python --version
```
ou
```bash
python3 --version
```

Se você não tiver o Python instalado, pode baixá-lo gratuitamente no site oficial: [python.org](https://www.python.org/downloads/).

## Como Executar o Projeto

Siga os passos abaixo para baixar e rodar a aplicação em sua máquina local.

**1. Clone o Repositório**

Abra seu terminal, navegue até o diretório onde deseja salvar o projeto e use o comando `git` para clonar o repositório:

```bash
git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
```
*Substitua `seu-usuario/nome-do-repositorio` pela URL do seu repositório no GitHub.*

**2. Acesse a Pasta do Projeto**

Após o download, entre na pasta do projeto com o comando `cd`:

```bash
cd nome-do-repositorio
```

**3. Execute o Script**

Com o Python 3 instalado e dentro da pasta correta, execute o seguinte comando para iniciar o programa:

```bash
python3 nome_do_arquivo.py
```
*Caso o comando `python3` não funcione, tente usar `python`.*
*Substitua `nome_do_arquivo.py` pelo nome real do seu arquivo Python.*

## Como Usar a Aplicação

Ao iniciar o programa, ele primeiro solicitará os valores iniciais para a lista.

1.  **Inicialização:**
    Digite os números que desejar (inteiros ou decimais, como `5.5`), separados por espaço, e pressione `Enter`.
    ```
    Digite os valores numéricos iniciais da lista (inteiros ou decimais), separados por espaço:
    10 20 30.5 40
    ```

2.  **Menu de Ações:**
    Após a inicialização, um menu será exibido com as ações disponíveis:

    ```
    --- Menu de Ações ---
    Adicionar: A [numero] [posição]
    Remover:   R [numero]
    Imprimir:  P
    Fechar:    X
    -----------------------
    ```

3.  **Exemplos de Comandos:**

    * **Para Adicionar** o número `25` na posição `2`:
        ```
        Digite a ação: A 25 2
        ```

    * **Para Remover** a primeira ocorrência do número `20`:
        ```
        Digite a ação: R 20
        ```

    * **Para Imprimir** (visualizar) o estado atual da lista:
        ```
        Digite a ação: P
        ```

    * **Para Encerrar** o programa:
        ```
        Digite a ação: X
        ```
