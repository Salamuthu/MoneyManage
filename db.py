import mysql.connector
from datetime import date

def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='moneymanage'
        )
        return connection
    except mysql.connector.Error as e:
        print("Database connection failed:", e)
        return None

def get_total_income(user_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT SUM(amount) FROM income WHERE user_id=%s", (user_id,))
    result = cur.fetchone()[0]
    conn.close()
    return result if result else 0


def get_total_expenses(user_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT SUM(amount) FROM expense WHERE user_id=%s", (user_id,))
    result = cur.fetchone()[0]
    conn.close()
    return result if result else 0


def get_today_total_expenses(user_id):
    today = date.today()
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT SUM(amount) FROM expense WHERE date_entry=%s AND user_id=%s",
        (today, user_id)
    )
    result = cur.fetchone()[0]
    conn.close()
    return result if result else 0


def get_today_total_incomes(user_id):
    today = date.today()
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT SUM(amount) FROM income WHERE date_entry=%s AND user_id=%s",
        (today, user_id)
    )
    result = cur.fetchone()[0]
    conn.close()
    return result if result else 0


def get_recent_transactions(user_id, limit=5):
    conn = connect_db()
    cur = conn.cursor()
    query = """
        SELECT category, amount, date_entry 
        FROM (
            SELECT category, amount, date_entry 
            FROM income WHERE user_id=%s

            UNION ALL

            SELECT category, amount, date_entry 
            FROM expense WHERE user_id=%s
        ) AS all_trans
        ORDER BY date_entry DESC
        LIMIT %s
    """
    cur.execute(query, (user_id, user_id, limit))
    result = cur.fetchall()
    conn.close()
    return result

def update_tables():
    conn = connect_db()
    cur = conn.cursor()

    try:
        cur.execute("ALTER TABLE income ADD COLUMN user_id INT NULL")
    except:
        print("income.user_id already exists")

    try:
        cur.execute("ALTER TABLE expense ADD COLUMN user_id INT NULL")
    except:
        print("expense.user_id already exists")

    try:
        cur.execute("""
            ALTER TABLE income 
            ADD CONSTRAINT fk_income_user 
            FOREIGN KEY (user_id) REFERENCES user(id)
        """)
    except:
        print("income foreign key already exists")

    try:
        cur.execute("""
            ALTER TABLE expense 
            ADD CONSTRAINT fk_expense_user 
            FOREIGN KEY (user_id) REFERENCES user(id)
        """)
    except:
        print("expense foreign key already exists")

    try:
        cur.execute("UPDATE income SET user_id = 1 WHERE user_id IS NULL")
        cur.execute("UPDATE expense SET user_id = 1 WHERE user_id IS NULL")
    except:
        pass

    conn.commit()
    conn.close()
    print("Database updated successfully!")
