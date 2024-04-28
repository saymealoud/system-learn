from bson.objectid import ObjectId
from gridfs import GridFS

from mongo_db import client

db=client.school
gfs=GridFS(db,collection="book")
gfs.delete(ObjectId("5c1f2d50db1df31788fed5f3"))