from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    followers = db.relationship(
        'Follow', foreign_keys='Follow.followee_id', backref='followee', lazy='dynamic')
    followees = db.relationship(
        'Follow', foreign_keys='Follow.follower_id', backref='follower', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'


class Follow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)
    followee_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    __table_args__ = (
        db.UniqueConstraint('follower_id', 'followee_id',
                            name='_follower_followee_uc'),
    )

    def __repr__(self):
        return f'<Follow {self.follower_id} -> {self.followee_id}>'
