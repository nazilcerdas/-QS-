try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="nazil-280103"
        )
    
except Exception as e:
        print(e)

curs = conn.cursor()
query = f"select * from siswi"
curs.execute(query)
data = curs.fetchall()

for d in data:
    print("nama:", d[0], "umur:", d[1])