def check_abstract():
    z = collection.find({"abstract":{"$exists": False}})
    for k in z:
       id = k["id"]
       collection.update_one({"id":id}, {"$set": {"abstract": ""}})

def check_references():
    z = collection.find({"references":{"$exists": False}})
    for k in z:
       id = k["id"]
       collection.update_one({"id":id}, {"$set": {"references": []}})
