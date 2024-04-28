from bson.objectid import ObjectId
from gridfs import GridFS

from mongo_db import client

db=client.school
gfs=GridFS(db,collection="book")
document=gfs.get(ObjectId("5c1f2d50db1df31788fed5f3"))
file=open("D:/data/Linux手册.pdf","wb")
file.write(document.read())
file.close()