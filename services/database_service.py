import psycopg2
from psycopg2 import OperationalError

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="smartmetric",
            user="smarmetric",
            password="12345",
            host="localhost",
            port="5432"
        )
        print("Conexão bem-sucedida!")
        return conn
    except OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
