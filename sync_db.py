import sqlite3
import mysql.connector
import os


def sincronizar():
    sqlite_path = 'db.sqlite3'
    if not os.path.exists(sqlite_path):
        return

    try:
        # Conexão MySQL
        mysql_db = mysql.connector.connect(
            host="localhost", user="root", password="1234", database="pescadores"
        )
        cursor_mysql = mysql_db.cursor()

        # Conexão SQLite
        sqlite_db = sqlite3.connect(sqlite_path)
        cursor_sqlite = sqlite_db.cursor()

        # Pega os dados do SQLite
        # Nota: O Django costuma nomear a tabela como 'cadastros_pescadores'
        cursor_sqlite.execute(
            "SELECT nome, cpf, email, celular, data_cadastro, situacao_defeso FROM cadastros_pescadores")
        rows = cursor_sqlite.fetchall()

        if rows:
            print(f"🔄 Movendo {len(rows)} registros para o MySQL...")
            sql = """INSERT \
            IGNORE INTO cadastros_pescadores 
                     (nome, cpf, email, celular, data_cadastro, situacao_defeso) 
                     VALUES ( \
            %s, \
            %s, \
            %s, \
            %s, \
            %s, \
            %s \
            )"""
            cursor_mysql.executemany(sql, rows)
            mysql_db.commit()

            # Limpa o SQLite para evitar duplicatas no futuro
            cursor_sqlite.execute("DELETE FROM cadastros_pescadores")
            sqlite_db.commit()
            print("✅ Dados sincronizados com sucesso!")

        sqlite_db.close()
        mysql_db.close()
    except Exception as e:
        print(f"ℹ️ MySQL offline ou sem dados novos para sincronizar.")


if __name__ == "__main__":
    sincronizar()