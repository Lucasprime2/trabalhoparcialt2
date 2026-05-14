from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456", 
        database="primeiro_teste"
    )

@app.post("/tarefas")
def criar_tarefa(item: dict):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (descricao) VALUES (%s)", (item['descricao'],))
    conn.commit()
    cursor.close()
    conn.close()
    return {"status": "Sucesso"}

@app.get("/tarefas")
def listar_tarefas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tarefas")
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados