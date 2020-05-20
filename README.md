# Cadastro de Tarefas

### Requisitos

> Mongo 
> Docker (caso não tenha o mongo instalado)


## Criar Mongodb

```
cd docker && docker-compose up -d --build
```

### Objetivo 

 1. importar o arquivo CSV para o mongo e trabalhar os dados antes da   
    importação para o sistema final. 
 2. Fornecer funcionalidade de crataca"    
 3. Base para posterior emissão de relatório

## Ambiente Python 3.X

É possível implementar via docker ou subir via venv.
Nesse roteiro vamos seguir o ambiente venv.

uma opção interessante seria utilizar o pychar CE.

Criando virtualenv : [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)

Após criada a venv, fazer a ativação:
> source/venv/bin/activate

Executar a instacao das dependências:
> pip install -r requirements.txt  

## Executando o Sistema

Com o ambiente venv ativado:

> python3 run.py

obs: a depender da configuração de cada ambiente deverá definir a PYTHONPATH
> export PYTHONPATH="${PYTHONPATH}:./src"   



