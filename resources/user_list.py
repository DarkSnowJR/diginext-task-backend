from flask_restful import Resource
from models import db, User, Follow


class UserListAPI(Resource):
    def get(self):
        print("Getting user list")
        users = User.query.all()
        print(f"Retrieved {len(users)} users")
        result = []
        for user in users:
            print(f"Processing user {user.id}")
            followers = [f.follower_id for f in user.followers]
            print(f"Retrieved {len(followers)} followers for user {user.id}")
            followees = [f.followee_id for f in user.followees]
            print(f"Retrieved {len(followees)} followees for user {user.id}")
            user_info = {
                'id': user.id,
                'username': user.username,
                'followers': followers,
                'followees': followees
            }
            result.append(user_info)
            print(f"Added user {user.id} to result")
        print(f"Total number of users: {len(result)}")
        return result, 200
