import psycopg2
from psycopg2 import sql, OperationalError

def create_user_table():
    try:
        # Configurações de conexão ao banco de dados
        conn = psycopg2.connect(
            dbname="smartmetric",
            user="smartmetric",
            password="12345",
            host="localhost",
            port="5432"
        )
        conn.autocommit = True  # Configura a autocommit para execução de criação de tabela

        # Criação do cursor
        with conn.cursor() as cursor:
            # Criação da tabela
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    senha_hash VARCHAR(255) NOT NULL,
                    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            print("Tabela de usuários criada com sucesso.")

    except OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    finally:
        # Fechando a conexão
        if conn:
            conn.close()

# Executando a função
create_user_table()
