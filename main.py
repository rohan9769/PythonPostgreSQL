import psycopg2

#Making connection to postgresql
conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="YOUR_POSTGRES_PASSWORD",
    port=5432
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS mlmodels(
            id INT PRIMARY KEY,
            model_name VARCHAR(255),
            model_version VARCHAR(255),
            age INT
    );
""")

cur.execute("""
    INSERT INTO mlmodels (id,model_name,model_version,age) VALUES
    (1,'BERT','v1',44),
    (2,'NER','v1',45),
    (3,'SC','v2',46),
    (4,'CQ','v2',47)
""")

cur.execute(""" SELECT * FROM mlmodels WHERE model_name='BERT' """)
print(cur.fetchone())

cur.execute(""" SELECT * FROM mlmodels WHERE age < 46 """)
for row in cur.fetchall():
    print(row)

conn.commit()
cur.close()
conn.close()