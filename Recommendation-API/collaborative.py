import pandas as pd
import numpy as np

#Reading the dataframe with ratings>3
new_df = pd.read_csv("data\\collab\\new_df_cf.csv")

#User predictions df
user_predictions_df = pd.read_csv("data\\collab\\user_predictions.csv")

#Item predictions df
item_predictions_df = pd.read_csv("data\\collab\\item_predictions.csv")

#Function to perform User-based collaborative filtering
def recommend_top_n_user_based(user_id, top_n=5):
  item_rated = list(new_df['asin'].loc[new_df['reviewerID'] == user_id])
  temp = user_predictions_df.loc[user_predictions_df['reviewerID'] == user_id].copy()
  temp.drop(user_predictions_df[item_rated], axis=1, inplace=True) #remove already rated products
  final = temp.iloc[:, 1:].sort_values(by=temp.index[0], axis=1, ascending=False) #descending order of similarity
  
  top_recommend = final.iloc[:, :top_n].to_dict(orient='records')
  return item_rated, top_recommend

#Function to perform Item-based collaborative filtering
def recommend_top_n_item_based(user_id, top_n=5):
  item_rated = list(new_df['asin'].loc[new_df['reviewerID'] == user_id])
  temp = item_predictions_df.loc[item_predictions_df['reviewerID'] == user_id].copy()
  temp.drop(item_predictions_df[item_rated], axis=1, inplace=True)
  final = temp.iloc[:, 1:].sort_values(by=temp.index[0], axis=1, ascending=False)
  top_recommend = final.iloc[:, :top_n].to_dict(orient='records')

  return item_rated, top_recommend