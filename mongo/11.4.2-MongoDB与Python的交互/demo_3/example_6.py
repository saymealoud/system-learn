from gridfs import GridFS

from mongo_db import client

db=client.school
gfs=GridFS(db,collection="book")

file=open("D:/data/Linux就该这么学.pdf","rb")
args={"type":"PDF","keyword":"linux"}
gfs.put(file,filename="Linux就该这么学.pdf",**args)
file.close()