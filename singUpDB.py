from flask import Flask, jsonify, request
from flaskServer.jsonEncoder import CustomJSONEncoder

app = Flask(__name__)
app.users = {}
app.id_count = 1
app.tweets = []


@app.route("/ping", methods=['GET'])
def ping():
    return "pong"


@app.route("/sign-up", methods=['POST'])
def sign_up():
    new_user = request.json
    new_user_id = app.database.execute(
        text(""" 
        INSERT INTO users (
            name,
            email,
            profile,
            hashed_password
        ) VALUES (
            :name,
            :email,
            :profile,
            :password
        )
        """), new_user
    ).lastrowid

    row = current_app.database.execute(text("""
    SELECT 
    id,
    name,
    email,
    profile
    FROM users
    WHERE id = :user_id
    """), {'user_id': new_user_id}
    ).fetchone()

    created_user = {
        'id': row['id'],
        'name': row['name'],
        'email': row['email'],
        'profile': row['profile'],
    } if row else None

    return jsonify(created_user)


# @app.route('/tweet', methods=['POST'])
# def tweet():
#     payload = request.json
#     user_id = int(payload['id'])
#     tweet = payload['tweet']

#     if user_id not in app.users:
#         return 'User not found', 400

#     if len(tweet) > 300:
#         return 'The length of tweets is over 300', 400
#     user_id = int(payload['id'])
#     app.tweets.append({
#         'user_id': user_id,
#         'tweet': tweet
#     })

#     return '', 200


# @app.route('/follow', methods=['POST'])
# def follow():
#     payload = request.json
#     user_id = int(payload['id'])
#     user_id_to_follow = int(payload['follow'])

#     if user_id not in app.users or user_id_to_follow not in app.users:
#         return 'Users not found', 400

#     user = app.users[user_id]
#     user.setdefault('follw', set()).add(user_id_to_follow)

#     return jsonify(user)


# @app.route('/unfollow', methods=['POST'])
# def unfollow():
#     payload = request.json
#     user_id = int(payload['id'])
#     user_id_to_follow = int(payload['unfollow'])

#     if user_id not in app.users or user_id_to_follow not in app.users:
#         return 'Not found', 400
#     user = app.users[user_id]
#     user.setdefault('follow', set()).discard(user_id_to_follow)

#     return jsonify(user)


# @app.route('/timeline/<int:user_id>', methods=['GET'])
# def timeline(user_id):
#     if user_id not in app.users:
#         return 'Not found??', 400

#     follow_list = app.users[user_id].get('follow', set())
#     follow_list.add(user_id)
#     timeline = [tweet for tweet in app.tweets if tweet['user_id'] in follow_list]

#     return jsonify(
#         {
#             'user_id': user_id,
#             'timeline': timeline
#         }
#     )
