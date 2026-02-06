import sqlite3
import mysql.connector
import os


def sincronizar():
    sqlite_path = 'db.sqlite3'
    if not os.path.exists(sqlite_path):
        return

    sqlite_db = None
    mysql_db = None

    try:
        # 1. Conexão SQLite (apenas leitura dos dados)
        sqlite_db = sqlite3.connect(sqlite_path)
        cursor_sqlite = sqlite_db.cursor()

        cursor_sqlite.execute(
            "SELECT nome, cpf, email, celular, data_cadastro, situacao_defeso FROM cadastros_pescadores"
        )
        rows = cursor_sqlite.fetchall()

        if not rows:
            print("ℹ️ SQLite sem registros para processar.")
            return

        # 2. Tentativa de conexão com MySQL
        try:
            mysql_db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="pescadores",
                connect_timeout=5
            )
            cursor_mysql = mysql_db.cursor()
        except mysql.connector.Error:
            print("⚠️ MySQL offline. Os dados continuam seguros no SQLite.")
            return

        # 3. Sincronização usando INSERT IGNORE
        # O 'IGNORE' faz com que, se o CPF já existir no MySQL, ele pule para o próximo sem dar erro
        print(f"🔄 Verificando sincronia de {len(rows)} registros...")

        sql = """INSERT IGNORE INTO cadastros_pescadores 
                 (nome, cpf, email, celular, data_cadastro, situacao_defeso) 
                 VALUES (%s, %s, %s, %s, %s, %s)"""

        cursor_mysql.executemany(sql, rows)
        mysql_db.commit()

        print(f"✅ Processo concluído. Registros novos foram salvos e duplicados foram ignorados.")
        print("📌 Nota: O banco SQLite permaneceu intacto.")

    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

    finally:
        if sqlite_db:
            sqlite_db.close()
        if mysql_db:
            mysql_db.close()


if __name__ == "__main__":
    sincronizar()