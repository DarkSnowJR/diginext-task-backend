from app import app
from models import db, User, Follow

with app.app_context():
    # پاک کردن داده‌های قدیمی
    db.drop_all()
    db.create_all()

    # افزودن کاربران
    user1 = User(username='user1')
    user2 = User(username='user2')
    user3 = User(username='user3')

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()

    # افزودن روابط دنبال کردن
    follow1 = Follow(follower_id=user1.id, followee_id=user2.id)
    follow2 = Follow(follower_id=user2.id, followee_id=user3.id)
    follow3 = Follow(follower_id=user1.id, followee_id=user3.id)

    db.session.add(follow1)
    db.session.add(follow2)
    db.session.add(follow3)
    db.session.commit()
