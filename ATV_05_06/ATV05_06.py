import csv
import os

def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    agenda[nome] = telefone
    print("Contato adicionado com sucesso!")

def exibir_contatos(agenda):
    if agenda:
        print("Lista de contatos:")
        for nome, telefone in agenda.items():
            print(f"Nome: {nome}, Telefone: {telefone}")
    else:
        print("A agenda está vazia!")

def buscar_contato(agenda):
    nome = input("Me fale, qual contato quer buscar: ")
    if nome in agenda:
        print(f"Telefone de {nome}: {agenda[nome]}")
    else:
        print("Não encontrei esse contato, tente novamente.")

def salvar_agenda(agenda, arquivo):
    with open(arquivo, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Nome', 'Telefone'])
        for nome, telefone in agenda.items():
            writer.writerow([nome, telefone])
    print("Agenda salva com sucesso!")

def carregar_agenda(arquivo):
    agenda = {}
    try:
        with open(arquivo, 'r') as f:
            reader = csv.reader(f)
            next(reader)  
            for linha in reader:
                nome, telefone = linha
                agenda[nome] = telefone
    except FileNotFoundError:
        print("Arquivo de agenda não encontrado. Criando nova agenda...")
    return agenda

def mostrar_menu():
    print("\n------__Menu de Opções__------")
    print("Digite 1 para Adicionar Contato")
    print("Digite 2 para Exibir Contatos")
    print("Digite 3 para Buscar Contato")
    print("Digite 4 para Salvar Agenda")
    print("Digite 5 para Excluir Agenda")
    print("Digite 6 para Sair do Algoritmo")

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def limpar_agenda(agenda, arquivo):
    confirmacao = input("Tem certeza que deseja limpar a agenda? (sim/não): ").lower()
    if confirmacao == "sim":
        agenda.clear()
        if os.path.exists(arquivo):
            os.remove(arquivo)
            print("Agenda excluída com sucesso!")
        else:
            print("O arquivo da agenda não existe.")
    else:
        print("Operação cancelada.")

def main():
    arquivo = "agenda.csv"
    agenda = carregar_agenda(arquivo)
    
    while True:
        limpar_tela()
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_contato(agenda)
        elif opcao == '2':
            exibir_contatos(agenda)
        elif opcao == '3':
            buscar_contato(agenda)
        elif opcao == '4':
            salvar_agenda(agenda, arquivo)
        elif opcao == '5':
            limpar_agenda(agenda, arquivo)
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
