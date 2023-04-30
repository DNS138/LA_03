from flask import Flask, request, jsonify
from flask_cors import CORS
from content_based import get_top_n_recommendations, find_prev_purchases, find_item_name
from collaborative import recommend_top_n_item_based, recommend_top_n_user_based

app = Flask(__name__)
CORS(app)

@app.route('/')
def enter():
    welcome_msg = "<h1> Welcome to our application </h1> <br/>"
    return welcome_msg

@app.route('/user', methods=['GET'])
def get_user():
    return "<h1> Hello User! Ready to get some recommendations?</h1>"

@app.route('/user/recommend')
def recommend():
    #query parameter for content-based or collaborative
    filtering = request.args.get('filter')  #accepted values - cb-contentbased or cf-collaborative
    user_id = request.args.get('user_id')
    
    if filtering == 'cb':
        prev_purchases = find_prev_purchases(user_id)
        recommendations = get_top_n_recommendations(user_id)
        recommendation_lst = [find_item_name(i) for i in recommendations]
        recommendations_dict = {"userId": user_id, "pastPurchases": prev_purchases, "recommendations": recommendation_lst, "type": "content"}
        return jsonify(recommendations_dict)
    elif filtering == 'cf':
        f_type = request.args.get('type') #type of collaborative - user or item
        if f_type == 'user':
            prev, top_n = recommend_top_n_user_based(user_id)
        elif f_type == 'item':
            prev, top_n = recommend_top_n_item_based(user_id)
        rec = list(top_n[0].keys())
        recommendations_dict = {"userId": user_id, "pastPurchases": prev, "recommendations": rec, "type": "collaborative"}
        return jsonify(recommendations_dict)

if __name__=='__main__':
    app.run(port = 5000, debug = True)
