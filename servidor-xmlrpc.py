from xmlrpc.server import SimpleXMLRPCServer
import datetime
import xmlrpc.client

def today():
    today = datetime.datetime.today()
    return xmlrpc.client.DateTime(today)

server = SimpleXMLRPCServer(("localhost", 8000))


try:
    print("Escuchando el puerto 8000...")
    print ('presiones ctrl+c para salir')
    server.register_function(today, "today")
    server.serve_forever()
except KeyboardInterrupt:
    print('saliendo')