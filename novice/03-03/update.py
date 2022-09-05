try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="nazil-280103")

    curs = conn.cursor()

    namaLama = "nazila"
    namaBaru = "zilaaaa"
    umurBaru = 20
    query = f"update siswi set nama='{namaBaru}', umur='{umurBaru}' where nama='{namaLama}' "
    curs.execute(query)
    conn.commit()
    print("data telah diupdate")
except Exception as e:
    print(e)