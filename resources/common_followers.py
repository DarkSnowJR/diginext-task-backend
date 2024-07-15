from flask_restful import Resource
from models import db, Follow


class CommonFollowersAPI(Resource):
    def get(self, user1_id, user2_id):
        followers_user1 = db.session.query(Follow.follower_id).filter_by(
            followee_id=user1_id).subquery()
        followers_user2 = db.session.query(Follow.follower_id).filter_by(
            followee_id=user2_id).subquery()

        common_followers = db.session.query(Follow.follower_id).filter(Follow.follower_id.in_(
            followers_user1)).filter(Follow.follower_id.in_(followers_user2)).all()

        common_followers_list = [
            follower.follower_id for follower in common_followers]

        return {'common_followers': common_followers_list}, 200
