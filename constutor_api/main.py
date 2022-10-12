import requests
import json
import tarefa

def buscar_dados():
    request = requests.get("http://localhost:3002/api/todo")
    todos = json.loads(request.content)
    print(todos)
    print(todos[0]['titulo'])

def cadastrar_dados(tarefa):
    requests.post("http://localhost:3002/api/todo",
                  data=json.dumps(tarefa.__dict__))

if __name__ == '__main__':
    cadastrar_dados(tarefa.Tarefa("Escrever o artigo de Python", "Segunda parte"))
    buscar_dados()

