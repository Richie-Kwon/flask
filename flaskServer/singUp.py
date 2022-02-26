from flask import Flask, jsonify, request

app = Flask(__name__)
app.users = {}
app.id_count = 1
app.tweets = []

@app.route("/ping", methods=['GET'])
def ping():
    return "pong"

@app.route("/sign-up", methods = ['POST'])
def sign_up():
    new_user = request.json
    new_user["id"] = app.id_count
    app.users[app.id_count]=new_user
    app.id_count = app.id_count + 1

    return jsonify(new_user)

@app.route('/tweet', methods = ['POST'])
def tweet():
    payload=request.json
    user_id = int (payload['id'])
    tweet = payload['tweet']

    if user_id not in app.users:
        return 'User not found', 400

    if len(tweet) > 300:
        return 'The length of tweets is over 300', 400
    user_id = int(payload['id'])
    app.tweets.append({
        'user_id': user_id,
        'tweet': tweet
    })

    return '', 
    
@app.route('/follow', methods=['POST'])
def follow():
    payload = request.json
    user_id = int(payload['id'])
    user_id_to_follow = int (payload['follow'])

    if user_id not in app.users or user_id_to_follow not in app.users:
        return 'Users not found', 400
    
    user = app.users[user_id]
    user.setdefault('follw', set()).add(user_id_to_follow)

    return jsonify(user)