from flask import Flask
from flask_restful import Api
from models import db
from resources.follow import FollowAPI
from resources.unfollow import UnfollowAPI
from resources.followers_count import FollowersCountAPI
from resources.common_followers import CommonFollowersAPI
from resources.user_list import UserListAPI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///followers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()

api.add_resource(FollowAPI, '/follow')
api.add_resource(UnfollowAPI, '/unfollow')
api.add_resource(FollowersCountAPI, '/followers_count/<int:user_id>')
api.add_resource(CommonFollowersAPI,
                 '/common_followers/<int:user1_id>/<int:user2_id>')
api.add_resource(UserListAPI, '/users')

if __name__ == '__main__':
    app.run(debug=True)
