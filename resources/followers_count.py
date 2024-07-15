from flask_restful import Resource
from models import db, User, Follow


class FollowersCountAPI(Resource):
    def get(self, user_id):
        count = Follow.query.filter_by(followee_id=user_id).count()
        return {'user_id': user_id, 'followers_count': count}, 200
