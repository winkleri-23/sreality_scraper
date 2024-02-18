import http.server
import socketserver
from http import HTTPStatus
import psycopg2

cnt = 0

def getDataFromDB():
    global cnt 
    try:
        conn = psycopg2.connect(
            host="database",
            port="5432",
            database="sreality",
            user="test",
            password="test"
        )
        dbHandle = conn.cursor()
        
        dbHandle.execute("""
        SELECT * FROM flat
        """)

        flat_records = dbHandle.fetchall()
        strTable = "<html><head><meta charset=\"UTF-8\"><style>table {font-family: Arial, sans-serif; border-collapse: collapse; width: 100%;} th, td {border: 1px solid #ddd; padding: 8px; text-align: center; vertical-align: middle;} th {background-color: #f2f2f2;} tr:nth-child(even) {background-color: #f9f9f9;} tr:hover {background-color: #f5f5f5;}</style></head><body><table><tr><th>#</th><th>Flats</th><th>Image</th></tr>"
        for i, row in enumerate(flat_records, start=1):
            strRW = "<tr><td>" + str(i) + "</td><td>" + str(row[1]) + "</td><td><img src=\"" + str(row[2]) + "\" style=\"max-width: 200px; display: block; margin-left: auto; margin-right: auto;\"></td></tr>"
            strTable = strTable + strRW

        strTable = strTable + "</table></body></html>"
        hs = open("./srealityFlats.html", 'w')
        hs.write(strTable)
        hs.close()

    except Exception as e:
        cnt += 1
        hs = open("./srealityFlats.html", 'w')
        hs.write("No data available! + "+str(cnt))
        hs.close()
        print(e)
          

class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        getDataFromDB()
        self.path = 'srealityFlats.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


with socketserver.TCPServer(('', 8080), HttpRequestHandler) as server:
    print('Server started on port 8080...')
    cnt = 0
    server.serve_forever()