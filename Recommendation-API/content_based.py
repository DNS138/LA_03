import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


user = pd.read_pickle('data\\content\\user.pickle')
user = user.set_index('reviewerID')
item = pd.read_pickle('data\\content\\item.pickle')

user_embs = pd.read_pickle('data\\content\\user_emb.pickle')
item_embs = pd.read_pickle('data\\content\\item_emb.pickle')

sim_matrix = cosine_similarity(user_embs.emb.tolist(), item_embs.emb.tolist())
sim_df = pd.DataFrame(columns=item.asin.tolist(), data = sim_matrix, index = user.index)

# sim_df = pd.read_csv("data\\similarity_df.csv")
# sim_df.set_index('reviewerID', inplace=True)

def find_item_name(asin):
  return item[item['asin'] == asin]['title'].values[0]

def find_prev_purchases(userID):
   prev = user.loc[userID]['asin']
   prev_item = [find_item_name(i) for i in prev]
   return prev_item

def get_top_n_recommendations(userID, n=10, sim_df = sim_df,user = user):
  temp = sim_df.loc[userID]
  A = temp.sort_values(ascending = False).index
  B = user.loc[userID]['asin']
  return [i for i in A if not i in B or B.remove(i)][:n]



