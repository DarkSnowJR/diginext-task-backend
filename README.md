
# Following System API

این پروژه یک سیستم فالویینگ ساده است که شامل قابلیت‌های دنبال کردن، لغو دنبال کردن، نمایش تعداد دنبال‌کنندگان هر کاربر به صورت روزانه، و نمایش دنبال‌کنندگان مشترک دو کاربر می‌باشد.

## پیش‌نیازها

- Python 3.x
- Flask
- Flask-RESTful
- Flask-SQLAlchemy

## نصب

ابتدا مخزن پروژه را کلون کنید:

```bash
git clone https://github.com/DarkSnowJR/diginext-task-backend
cd diginext-task-backend
```

یک محیط مجازی ایجاد کنید و وابستگی‌ها را نصب کنید:

```bash
python -m venv venv
source venv/bin/activate  # در ویندوز: venv\Scripts\activate
pip install -r requirements.txt
```

## راه‌اندازی دیتابیس و افزودن داده‌های تست

برای راه‌اندازی دیتابیس و افزودن داده‌های تست، اسکریپت `add_test_data.py` را اجرا کنید:

```bash
python add_test_data.py
```

این اسکریپت دیتابیس را پاکسازی کرده و داده‌های جدید را اضافه می‌کند.

## اجرای سرور

برای اجرای سرور، دستور زیر را اجرا کنید:

```bash
export FLASK_APP=app.py  # در ویندوز: set FLASK_APP=app.py
flask run
```

سرور در آدرس `http://127.0.0.1:5000/` اجرا خواهد شد.

## استفاده از API

### دنبال کردن کاربر

```bash
POST /follow
Content-Type: application/json

{
    "follower_id": 1,
    "followee_id": 2
}
```

### لغو دنبال کردن کاربر

```bash
POST /unfollow
Content-Type: application/json

{
    "follower_id": 1,
    "followee_id": 2
}
```

### نمایش تعداد دنبال‌کنندگان یک کاربر

```bash
GET /followers_count/<user_id>
```

### نمایش دنبال‌کنندگان مشترک دو کاربر

```bash
GET /common_followers/<user1_id>/<user2_id>
```

### نمایش لیست کاربران همراه با دنبال‌کنندگان و دنبال‌شوندگان آن‌ها

```bash
GET /users
```

## مستندات API

مستندات API در فایل `swagger.yaml` موجود است. می‌توانید از ابزارهایی مانند [Swagger Editor](https://editor.swagger.io/) برای مشاهده و تست مستندات استفاده کنید.

## نکات مهم

- این پروژه نیازی به احراز هویت (Authentication) ندارد.
- برای بهبود scalability می‌توان از روش‌هایی مانند کش کردن (Caching) و استفاده از دیتابیس‌های توزیع شده (Distributed Databases) استفاده کرد.

## راهنمای توسعه‌دهندگان

برای توسعه و تغییرات در کد، می‌توانید از دستور زیر برای اجرای تست‌ها استفاده کنید:

```bash
pytest
```

این پروژه از استانداردهای کدنویسی PEP 8 پیروی می‌کند. لطفاً قبل از ارسال pull request مطمئن شوید که کد شما با این استانداردها سازگار است.

## لایسنس

این پروژه تحت لایسنس MIT منتشر شده است. برای اطلاعات بیشتر به فایل `LICENSE` مراجعه کنید.
