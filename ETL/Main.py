import pysftp

#Datos de Conexión

myHostName = "hostname"
myUserName = "username"
myPassword = "password"

def conexionFTP (hostname,username,password):
    conexion = pysftp.Connection(host = hostname, username = username, password = password)
    return conexion

conexion = conexionFTP(myHostName,myUserName,myPassword)
with conexion as sftp:
    # Si la conexión no es exitosa se mostrará un error.
    print ("Conexión exitosa")

    #Directorio
    sftp.cwd('/home/vinkOS/archivosVisitas')

    sftp.get_d('/home/vinkOS/archivosVisitas','/home/etl/visitas/bckp/fecha.zip')

    #Borrar directorio
    sftp.rmdir('./report_*.txt')
