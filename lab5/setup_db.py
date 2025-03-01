import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
conn.autocommit = True
cur = conn.cursor()
cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'rct_todo'")
exists = cur.fetchone()
if not exists:
    cur.execute('CREATE DATABASE rct_todo')

conn.close()

conn = psycopg2.connect("host=localhost dbname=rct_todo user=postgres password=postgres")
cur = conn.cursor()

cur.execute("CREATE TABLE tasks (id SERIAL PRIMARY KEY, title VARCHAR(256), description TEXT, completed BOOLEAN, deadline TIMESTAMP)")

conn.commit()

conn.close()
