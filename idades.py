import mysql.connector
import os
import bcrypt
import requests

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ordep1205",
    database="atv"
)

cursos = conexao.cursor()

def buscar_fato_historico(ano_nascimento):
    try:
        url = f"http://numbersapi.com/{ano_nascimento}/year"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return "Fato histórico não encontrado"
    except:
        return "Erro ao consultar API"

nomes = []
idades = []
pesos = []

usuario = []
senha = [] 

os.system('cls' if os.name == 'nt' else 'clear')
print("| Login")
print("|=================")
usuario = input("| Usuário: ")
senha = input("| Senha: ")

# Vai la no banco, na table usuarios e confere se os dados batem
sql_buscar = "SELECT senha FROM usuarios WHERE usuario = %s"
cursos.execute(sql_buscar, (usuario,))
resultado_senha = cursos.fetchone()

if resultado_senha:
    senha_hash_banco = resultado_senha[0].encode('utf-8')
    
    #confere se o código gerado pelo bcrypt confere com a senha do banco
    #exemplo:
    #senha: 123 - código: $2b$12$3B4lgTShJ/tg7a8SbYOXGOem2iLKu6/9FcO.gjQQhRcxKvVNWPz5G
    
    if bcrypt.checkpw(senha.encode('utf-8'), senha_hash_banco):
        print("Login realizado com sucesso!")

    nomes = []
    idades = []
    pesos = []

    for i in range(3):
        print("                  ")
        print("+-----------------+")
        print("| Cadastro        |")
        print("|=================|")
        nome = input("| Nome: ")
        idade = int(input("| Idade: "))
        peso = float(input("| Peso: ")) 
        
        nomes.append(nome)
        idades.append(idade)
        pesos.append(peso)
        
        # Busca fato histórico do ano de nascimento
        ano_nascimento = 2024 - idade
        fato = buscar_fato_historico(ano_nascimento)
        
        sql = "INSERT INTO pessoas (nome, idade, peso) VALUES (%s, %s, %s)"
        valores = (nome, idade, peso)
        cursos.execute(sql, valores)
        conexao.commit() 
        print("|=================|")
        print("Nome : ", nome,"|", "Idade: ", idade,"|", "Peso: ", peso,"kg")
        print("| Curiosidade do ano", ano_nascimento, ":", fato)

    mediaIdade = sum(idades) / len(idades)
    mediaPeso = sum(pesos) / len(pesos)

    print("+==================================================+")
    print("| Cadastrados:                                     |")
    print("+--------------------------------------------------+")
    for i in range(3):
        print("| Nome : ", nomes[i],"|", "Idade: ", idades[i],"|", "Peso: ", pesos[i],"kg")
    
    print("+--------------------------------------------------+")    
    print("| Média Idade:", mediaIdade)
    print("| Média Peso:", mediaPeso)
    print("+==================================================+")

else:
    print("Usuário ou senha incorretos!")

cursos.close()
conexao.close()
