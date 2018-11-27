from flask import Flask, request, Response, url_for, jsonify
import datetime
import json

app = Flask(__name__, template_folder='/UI/', static_folder='/UI/assets/')

@app.route("/api/v1/red-flags", methods=['POST'])
def post_red_flag():

    try:
        data = request.get_json()
        title = data.get("title")
        comment = data.get("comment")

        local_id = 0

        if len(all_flags) > 0:
            local_id = flag_exists(title, comment)

        if local_id != 0:
            res = {
                "status": 200,
                "data": [
                    {
                        "id": local_id,
                        "message": "Flag Already reported!"
                    }
                ]
            }
            return (jsonify(res), 200)
        else:
            add_new_flag(data)
            res = {
                "status": 201,
                "data": [
                    {
                        "id": data.get("id"),
                        "message":"Created a red-flag record"
                    }
                ]
            }
            return (jsonify(res), 201)
    except:
        res = {
            "status": 400,
            "error": "json object error"
        }
        return (jsonify(res), 400)
    
def flag_exists(title, comment):
    for flag in all_flags:
        if flag["title"] == title and flag["comment"] == comment:
            return flag["id"]

    return 0

def add_new_flag(data):
    all_flags.append(data)

all_flags = []

all_users = []

@app.route("/api/v1/red-flags", methods=["GET"])
def get_all_flags():
    try:
        json_data = request.get_json()
        user_id = json_data.get("userId")
        data = get_flags(user_id)
        res = {
            "status": 200,
            "data": data
        }

        return (jsonify(res), 200)
    except:
        res = {
            "status": 400,
            "error": "json object error"
        }

        return (jsonify(res), 400)

def get_flags(user_id):
    if user_is_admin(user_id):
        return all_flags
    else:

        flags = []
        for flag in all_flags:
            if flag["createdBy"] == user_id:
                flags.append(flag)

        return flags

def user_is_admin(user_id):
    for user in all_users:
        if user["id"] == user_id:
            if user["isAdmin"]:
                return True
    return False

@app.route("/api/v1/users", methods=["POST"])
def add_new_user():
    try:
        json_data = request.get_json()
        uname = json_data['username']
        email = json_data['email']

        if user_exists(uname, email):
            res = {
                "status": 200,
                "data": [{
                    "id": json_data["id"],
                    "message": "User Already Exists"
                }]
            }
            return (jsonify(res), 200)
        
        add_user(json_data)

        msg = "New User Added!"
        if json_data["isAdmin"]:
            msg = "New Admin Added!"
        res = {
            "status": 201,
            "data": [{
                "id": json_data['id'],
                "message": msg
            }]
        }

        return (jsonify(res), 201)
    except:
        res = {
            "status": 400,
            "error": "json object error"
        }

        return (jsonify(res), 400)

def user_exists(username, email):
    if len(all_users) == 0:
        return False

    for user in all_users:
        if user['username'] == username:
            return True
        elif user['email'] == email:
            return True
    
    return False

def add_user(json_data):
    all_users.append(json_data)

if __name__ == '__main__':
    app.run()