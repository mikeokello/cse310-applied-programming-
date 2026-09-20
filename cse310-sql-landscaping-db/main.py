import sqlite3
from datetime import date
DB_NAME = "landscape.db"
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
def create_tables():
    conn = get_connection(); cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS customers (customer_id INTEGER PRIMARY KEY, name TEXT NOT NULL, phone TEXT UNIQUE, email TEXT UNIQUE)")
    cur.execute("CREATE TABLE IF NOT EXISTS properties (property_id INTEGER PRIMARY KEY, customer_id INTEGER NOT NULL, address TEXT NOT NULL, total_area INTEGER NOT NULL, FOREIGN KEY (customer_id) REFERENCES customers(customer_id))")
    cur.execute("CREATE TABLE IF NOT EXISTS jobs (job_id INTEGER PRIMARY KEY, property_id INTEGER NOT NULL, bags_needed INTEGER NOT NULL, total_cost REAL NOT NULL, job_date TEXT NOT NULL, FOREIGN KEY (property_id) REFERENCES properties(property_id))")
    conn.commit(); conn.close(); print("Tables created!")
def add_customer(name, phone, email):
    conn=get_connection(); conn.execute("INSERT INTO customers (name,phone,email) VALUES (?,?,?)",(name,phone,email)); conn.commit(); conn.close()
def add_property(customer_id, address, total_area):
    conn=get_connection(); conn.execute("INSERT INTO properties (customer_id,address,total_area) VALUES (?,?,?)",(customer_id,address,total_area)); conn.commit(); conn.close()
def add_job(property_id, bags_needed, total_cost):
    conn=get_connection(); conn.execute("INSERT INTO jobs (property_id,bags_needed,total_cost,job_date) VALUES (?,?,?,?)",(property_id,bags_needed,total_cost,str(date.today()))); conn.commit(); conn.close()
def view_all_jobs():
    conn=get_connection(); cur=conn.cursor()
    cur.execute("SELECT c.name, p.address, j.bags_needed, j.total_cost, j.job_date FROM jobs j JOIN properties p ON j.property_id=p.property_id JOIN customers c ON p.customer_id=c.customer_id")
    for r in cur.fetchall(): print(r)
    conn.close()
def total_profit():
    conn=get_connection(); cur=conn.cursor()
    cur.execute("SELECT c.name, SUM(j.total_cost), COUNT(j.job_id) FROM customers c JOIN properties p ON c.customer_id=p.customer_id JOIN jobs j ON p.property_id=j.property_id GROUP BY c.name")
    for r in cur.fetchall(): print(f"Customer: {r[0]}, Total: ${r[1]}, Jobs: {r[2]}")
    conn.close()
def main():
    create_tables()
    conn=get_connection(); count=conn.execute("SELECT COUNT(*) FROM customers").fetchone()[0]; conn.close()
    if count==0:
        add_customer("John Doe","0701000001","john@example.com")
        add_customer("Jane Smith","0701000002","jane@example.com")
        add_property(1,"123 Jinja Road",3600); add_property(2,"45 Kampala Ave",5000)
        add_job(1,2,94.00); add_job(2,3,141.00)
    print("\n--- All Jobs (JOIN) ---"); view_all_jobs()
    print("\n--- Profit (GROUP BY + SUM) ---"); total_profit()
if __name__=="__main__": main()
