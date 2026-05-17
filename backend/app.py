from flask_cors import CORS
from flask import Flask
import os
import psycopg2

app = Flask(__name__)
CORS(App)
DB_HOST = os.getenv("DB_HOST", "postgres-service")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD")

APP_ENV = os.getenv("APP_ENV", "development")


def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn


@app.route('/')
def home():
    return f"Backend Running | ENV={APP_ENV}"


@app.route('/health')
def health():
    return {"status": "healthy"}


@app.route('/db-check')
def db_check():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id SERIAL PRIMARY KEY,
                content TEXT
            );
            """
        )

        conn.commit()

        cur.close()
        conn.close()

        return {"database": "connected"}

    except Exception as e:
        return {"error": str(e)}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)