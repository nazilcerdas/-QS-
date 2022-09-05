try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="nazil-280103")

    curs = conn.cursor()

    nama = "nazil"
    umur = 20
    query = f"insert into siswi(nama, umur) values('{nama}', {umur})"

    curs.execute(query)
    conn.commit()
    print("data masuk")
except Exception as e:
    print(e)