turmas={}

def consulta():
    aux=int(input("1-turmas,2-nome das turmas,3-aluno"))
  if(aux==1):
    print(turmas)
  if(aux==2):
    turma=str(input("entre com o nome da turma:"))
    print(turmas[turma])
  if(aux==3):
    turma=str(input("entre com o nome da turma:"))
    matricula=str(input("entre com a matricula do aluno"))
    print(turmas[turma][matricula])
consulta()

def addturma ():
    turma= str(input("entre com a turma:"))
    #a turma identificada deve ter o ano (ex:1), uma letra, e a sigla do curso. Ex:1BINF.
    alunos={}
    turmas[turma]=alunos
addturma()

def addalunosnota ():
    turma=str(input("entre com a turma:"))
    alunos= {}
    matriculas= str(input("entre com as matricula:"))
    #os alunos são identificados pelas matriculas

    qtnotas= int(input("entre com quantas notas tem o aluno:"))
    aux=1
    listadenotas= []
    while qtnotas>=aux:
        nota= int(input("entre com a nota:"))
        listadenotas.append(nota)
        aux += 1
    print(listadenotas)
    #turmas[turma]
    [matricula]=listadenotas
addalunos()

def calcmedia(listadenotas):
  soma=0
  for x in listadenotas:
    soma+=x
  return soma/len(listadenotas)
calcmedia()

def mediaturma():
  soma=0
  cont=0
  turma=str(input("entre com a turma:"))
  for x in turmas[turma]:
    soma+=calcmedia(turmas[turma][x])
    cont+=1
  return soma/cont
mediaturma()
