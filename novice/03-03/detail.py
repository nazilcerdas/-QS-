# try:
import psycopg2
conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="nazil-280103")

# except Exception as e:
#     print(e)

curs = conn.cursor()
query = f"select * from siswi where umur=19"
curs.execute(query)
data = curs.fetchall()
if not data:
    print("gak ada")
else:
    print("nama:", data[0], "umur:", data[1])