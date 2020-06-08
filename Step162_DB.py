import sqlite3

conn = sqlite3.connect('Step162.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT, col_fileName VARCHAR(55))")
    conn.commit()

fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

for file in fileList:
    if file.endswith('.txt'):
        conn = sqlite3.connect('Step162.db')
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files(col_fileName) VALUES (?)",(file,))
            conn.commit()
            print("\nText File Found: ")
            print(file)

conn.close()
