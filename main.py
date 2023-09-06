from functions import *

def main():
    filename = "todos.txt"
    listaToDos = loadToDosFromFile(filename)
    opcao = menu()
    index = getLatestIndex(listaToDos)

    while(opcao != 0 and opcao <= 4):
        if(opcao == 1):
            criarToDo(listaToDos, index)
            index += 1
        elif(opcao == 2):
            listarToDos(listaToDos)
        elif(opcao == 3):
            busca = int(input("Digite o número do to-do que você deseja editar.\n"))
            editarToDo(listaToDos, busca)
        elif(opcao == 4):
            busca = int(input("Digite o número do to-do que você deseja excluir.\n"))
            excluirToDos(listaToDos, busca)
        saveToDosToFile(listaToDos, filename)
        opcao = menu()

if __name__ == "__main__":
    main()
