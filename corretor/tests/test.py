from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')
e1 = model.encode("dono")
e2 = model.encode("tutor")
print(util.cos_sim(e1, e2))
