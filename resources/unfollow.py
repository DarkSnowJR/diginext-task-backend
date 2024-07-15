from flask import request
from flask_restful import Resource
from models import db, Follow


class UnfollowAPI(Resource):
    def post(self):
        data = request.get_json()
        follower_id = data.get('follower_id')
        followee_id = data.get('followee_id')

        follow = Follow.query.filter_by(
            follower_id=follower_id, followee_id=followee_id).first()

        if not follow:
            return {'message': 'Follow relationship does not exist'}, 404

        db.session.delete(follow)
        db.session.commit()

        return {'message': 'Unfollowed successfully'}, 200
