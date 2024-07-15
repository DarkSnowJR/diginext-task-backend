from flask import request
from flask_restful import Resource
from models import db, User, Follow


class FollowAPI(Resource):
    def post(self):
        data = request.get_json()
        follower_id = data.get('follower_id')
        followee_id = data.get('followee_id')

        if follower_id == followee_id:
            return {'message': 'You cannot follow yourself'}, 400

        follow = Follow(follower_id=follower_id, followee_id=followee_id)
        db.session.add(follow)
        db.session.commit()

        return {'message': 'Followed successfully'}, 201
