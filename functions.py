def loadToDosFromFile(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            listaToDos = {}
            for line in lines:
                index, title, content = line.strip().split("|")
                listaToDos[int(index)] = [title, content]
            return listaToDos
    except FileNotFoundError:
        return {}

def saveToDosToFile(lista, filename):
    with open(filename, "w") as file:
        for index, todo in lista.items():
            file.write(f"{index}|{todo[0]}|{todo[1]}\n")

def criarToDo(lista, index):
    title = input("Digite o título.\n")
    content = input("Digite a descrição.\n")
    lista[index] = [title, content]
    print("To-do criado com sucesso.")

def editarToDo(lista, busca):
    if busca in lista:
        novoTitulo = input("Digite o novo título.\n")
        novoConteudo = input("Digite o novo conteúdo.\n")
        lista[busca] = [novoTitulo, novoConteudo]
        print("To-do editado com sucesso.")
    else:
        print("To-do não encontrado.")

def listarToDos(lista):
    print("Lista de To-dos:")
    for index, todo in lista.items():
        print(f"{index} - Título: {todo[0]} - Descrição: {todo[1]}")

def excluirToDos(lista, busca):
    if busca in lista:
        del lista[busca]
        print("To-do excluído com sucesso.")
    else:
        print("To-do não encontrado.")

def menu():
    return int(input("O que deseja fazer?\n" +
                 "1 para inserir to-do\n" +
                 "2 para listar to-dos\n" +
                 "3 para editar to-do\n" +
                 "4 para excluir to-do\n" +
                 "0 para sair\n"))

def getLatestIndex(lista):
    if not lista:
        return 1
    return max(lista.keys()) + 1

