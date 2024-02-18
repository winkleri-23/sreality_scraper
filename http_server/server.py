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

        strTable = "<html><meta charset=\"UTF-8\"><table><tr><th>Flats</th><th> </th></tr>"
        for row in flat_records:
            strRW = "<tr><td>"+row[1]+ "</td><td><img src=\""+row[2]+"\"></td></tr>"
            strTable = strTable+strRW
        
        strTable = strTable+"</table></html>"
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