import Programa

def menu():
    cont="a"
    while (cont=="a"):
        aux= int(input("escolha:0-consulta, 1=adicionar turma,2-adicionar alunos e notas,3-calcular media de um aluno,4-calcular media de uma turma,5-sair:"))
        if(aux==1):
            addturma()
        if (aux==2):
            addalunosnotas()
        if (aux==3):
            turma=str(input("entre com a turma:"))
            matricula=str(input("entre com a matricula:"))
            print(calcmedia(turmas[turma][matricula]))
        if (aux==4):
            print(mediaturma())
        if (aux==5):
            cont="saiu"
        else:
            print("Erro-opção invalida")
menu()
