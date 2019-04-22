import falcon
import json
from models import User
import connection


class UsersApi:

    def on_get(self, req, resp):
        users = []
        ss = connection.get_session()
        for user in ss.query(User).all():
            users.append(user.to_dict())
        resp.body = json.dumps(users)

    def on_post(self, req, resp):

        if "name" in req.media and "address" in req.media:
            ss = connection.get_session()
            ss.add(User(name=req.media["name"], address=req.media["address"]))
            ss.commit()

            resp.body = "User added!\n"

        else:
            resp.body = "Valid json is { name: USER_NAME, address: USER_ADDRESS }\n"


api = falcon.API()
api.add_route('/api/users', UsersApi())
