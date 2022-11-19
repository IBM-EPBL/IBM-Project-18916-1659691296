import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=2d46b6b4-cbf6-40eb-bbce-6251e6ba0300.bs2io90108kqb10d8icg.databases.appdomain.cloud;PORT=32328;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=cmm81287;PWD=Os47OPOfg4C4Yird",'','')
print(conn)
print("connection successful")

sql="SELECT * FROM USERS"
stmt = ibm_db.exec_immediate(conn,sql)
dictionary = ibm_db.fetch_assoc(stmt)
while dictionary!=False:
    print("FUll ROW: ",dictionary)
    dictionary=ibm_db.fetch_assoc(stmt)