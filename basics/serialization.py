import pickle

things = {"apple":1,"banana":20,"carrot":50}

serializted = pickle.dumps(things)
print(serializted)

things_v2 = pickle.loads(serializted)
print(things_v2)

with open("pickel.things","wb") as handle:
    pickle.dump(things,handle)
    
with open("pickel.things","rb") as handle:
    things_v3 = pickle.load(handle)
    
print(things_v3)