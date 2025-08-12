# Import necessary libraries and modules
# flask creates the server that communicates with users
# https://flask.palletsprojects.com/en/stable/quickstart/
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify, abort
# os is where the secrets are saved, like developer passwords and api keys
import os
# Import forms from the forms.py file
from forms import LoginForm, SignupForm, TestimonyForm, PictureForm, SettingsForm, VerifyForm, EmailForm, NewPasswordForm, ItemForm
# CSRFProtect protects from cross-site-request-forgery https://flask-wtf.readthedocs.io/en/0.15.x/csrf/
from flask_wtf.csrf import CSRFProtect
# Import database tables from the entities.py file
from entities import db, UnverifiedUser, User, PasswordChanger, Testimony, Item
# werkzeug.security hashes passwords
# https://werkzeug.palletsprojects.com/en/stable/utils/#werkzeug.security.generate_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
# flask_login logs users in and out https://flask-login.readthedocs.io/en/latest/
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
# The python datetime module is used for getting the time that testimonies were made
from datetime import datetime, timezone, timedelta
# API requests are made through the requests module
import requests
# load_dotenv loads data stored as environment variables(e.g. secrets like the developer passwords or api keys)
from dotenv import load_dotenv
# cloudinary stores pictures uploaded by users
# https://cloudinary.com/documentation/dev_kickstart
import cloudinary
from cloudinary import CloudinaryImage
import cloudinary.uploader
import cloudinary.api
# The random module is used to generate a random number
import random
# The simple-mail-transfer-protocol library(smtplib) is used send emails
import smtplib
from functools import wraps
from items_data import things


load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("FLASK-SECRET-KEY")
csrf = CSRFProtect(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE-URI")
db.init_app(app)

app.config["UPLOAD_FOLDER"] = "static/images/uploads"
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp", "jfif"}
# app.config["MAX_CONTENT_LENGTH"] = 8 * 1000 * 1000

url = os.environ.get("API-URL")
i_d_ = os.environ.get("ID-INSTANCE")
key = os.environ.get("API-TOKEN-INSTANCE")
number = os.environ.get("NUMBER")

email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")

video_url = os.environ.get("VIDEO-URL")

config = cloudinary.config(secure=True)  # Signed up with the Google account

login_manager = LoginManager()
login_manager.init_app(app)

admin_email = os.environ.get("ADMIN-EMAIL")

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If the current user is not the admin then return abort with a 403 error
        if current_user.email != admin_email:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function


@app.route("/")
def home():
    posts = db.session.execute(db.select(Testimony).order_by(Testimony.id)).scalars().all()[:3]
    return render_template("index.html", testimonies=posts, video_url=video_url)


@app.route("/about")
def about():
    return render_template("about.html")


# @app.route("/flow")
# @login_required
# def flow():
#     return render_template("flow.html")
#
#
# @app.route("/flow/api")
# @login_required
# def flow_api():
#     return jsonify({
#         "first name": current_user.first_name,
#         "last name": current_user.last_name,
#         "email": current_user.email,
#         "picture url": current_user.picture_url,
#     })


@app.route("/projects")
def designs():
    return render_template("designs.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/testimonies")
def testimonies():
    # Display all the testimonies in the database on the web page, starting with the most recent
    posts = db.session.execute(db.select(Testimony).order_by(Testimony.id.desc())).scalars().all()
    return render_template("testimonies.html", testimonies=posts)


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    signup_form = SignupForm()
    if request.method == "POST":
        if signup_form.validate_on_submit():
            data = request.form
            db_emails = db.session.query(User.email).all()
            for email in db_emails:
                if data["email"] == email[0]:
                    flash("This Account Already Exists Here.")
                    return redirect(url_for("sign_up"))
            if data["password"] == data["second_password"]:
                hashed_password = generate_password_hash(
                    password=data["second_password"],
                    method="pbkdf2",
                    salt_length=8
                )
                unvalidated_user = db.session.execute(db.select(UnverifiedUser).where(UnverifiedUser.email == data["email"])).scalar()
                if unvalidated_user:
                    db.session.delete(unvalidated_user)
                    db.session.commit()
                unverified_user = UnverifiedUser(
                    first_name=data["first_name"].title(),
                    last_name=data["last_name"].title(),
                    email=data["email"],
                    password=hashed_password,
                    verification_code=random.randint(1000, 9999),
                    sent_at = datetime.now()
                )
                db.session.add(unverified_user)
                db.session.commit()
                return redirect(url_for("verify_email", e_mail=data["email"]))
            else:
                flash("Passwords do not match, please try again.")
                return redirect(url_for("sign_up"))
    return render_template("sign-up.html", form=signup_form)


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if request.method == "POST":
        if login_form.validate_on_submit():
            data = request.form
            user = db.session.execute(db.select(User).where(User.email == data["email"])).scalar()
            if user:
                if check_password_hash(user.password, data["password"]):
                    login_user(user)
                    return redirect(url_for("account"))
                flash("Invalid Password, Please Try Again.")
                return redirect(url_for("login"))
            flash("Account Not Found.")
            return redirect(url_for("login"))
    return render_template("login.html", form=login_form)


@app.route("/privacy-policy")
def privacy_policy():
    return render_template("privacy-policy.html")


@app.route("/account")
@login_required
def account():
    return render_template("account.html", admin_email=admin_email)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    user = db.session.execute(db.select(User).where(User.id == current_user.id)).scalar()
    settings_form = SettingsForm(
        first_name=user.first_name,
        last_name=user.last_name
    )
    if request.method == "POST":
        if settings_form.validate_on_submit():
            data = request.form
            with app.app_context():
                user = db.session.execute(db.select(User).where(User.id == current_user.id)).scalar()
                user.first_name = data["first_name"].title()
                user.last_name = data["last_name"].title()
                db.session.commit()
            return redirect(url_for("account"))
    return render_template("settings.html", form=settings_form, email=user.email, admin_email=admin_email)


@app.route("/add-testimony", methods=["GET", "POST"])
@login_required
def add_testimony():
    testimony_form = TestimonyForm()
    if request.method == "POST":
        if testimony_form.validate_on_submit():
            data = request.form
            with app.app_context():
                testimony = Testimony(
                    datetime=datetime.now(timezone.utc),
                    testimony=data["testimony"],
                    website=data["website"],
                    user_id = current_user.id
                )
                db.session.add(testimony)
                db.session.commit()
                requests.post(
                    f"{url}/waInstance{i_d_}/sendMessage/{key}",
                    json={
                        "chatId": f"{number}@c.us",
                        "message": f"{current_user.first_name} {current_user.last_name} added a testimony to FolaDevelops: "
                                   f"{data['testimony']}\nfor: {data['website']}"
                    },
                    headers={'Content-Type': 'application/json'}
                )
            flash("Thanks for adding a testimony, your testimony will be reviewed.")
            return redirect(url_for("account"))
    return render_template("add-testimony.html", form=testimony_form, admin_email=admin_email)


@app.route("/edit-testimony/<int:i_d>", methods=["GET", "POST"])
@login_required
def edit_testimony(i_d):
    testimony = db.session.execute(db.select(Testimony).where(Testimony.id == i_d)).scalar()
    testimony_form = TestimonyForm(testimony=testimony.testimony, website=testimony.website)
    if request.method == "POST":
        if testimony_form.validate_on_submit():
            data = request.form
            with app.app_context():
                testimony = db.session.execute(db.select(Testimony).where(Testimony.id == i_d)).scalar()
                testimony.testimony = data["testimony"]
                testimony.website = data["website"]
                db.session.commit()
                requests.post(
                    f"{url}/waInstance{i_d_}/sendMessage/{key}",
                    json={
                        "chatId": f"{number}@c.us",
                        "message": f"{current_user.first_name} {current_user.last_name} edited a testimony in FolaDevelops: "
                                   f"{data['testimony']}\nfor: {data['website']}"
                    },
                    headers={'Content-Type': 'application/json'}
                )
            flash("Thanks for editing a testimony, your testimony will be reviewed.")
            return redirect(url_for("account"))
    return render_template("edit-testimony.html", i_d=i_d, form=testimony_form)


@app.route("/confirm-delete/<int:i_d>")
@login_required
def confirm_delete(i_d):
    pending_testimony = db.session.execute(db.select(Testimony).where(Testimony.id == i_d)).scalar()
    return render_template("confirm-delete.html", testimony=pending_testimony)


@app.route("/delete/<int:i_d>")
@login_required
def delete(i_d):
    testimony = db.session.execute(db.select(Testimony).where(Testimony.id == i_d)).scalar()
    db.session.delete(testimony)
    db.session.commit()
    return redirect(url_for("account"))


@app.route("/profile-picture")
@login_required
def profile_picture():
    return render_template("profile-picture.html")


def valid_picture(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload-picture", methods=["GET", "POST"])
@login_required
def upload_picture():
    picture_form = PictureForm()
    if request.method == "POST":
        if "picture" not in request.files:
            flash("No file part")
            return redirect(url_for("upload_picture"))
        profile_pic = request.files["picture"]
        pic_name = profile_pic.filename
        if pic_name == "":
            flash("No file selected")
            return redirect(url_for("upload_picture"))
        if profile_pic and valid_picture(pic_name):
            if current_user.picture_url:
                cloudinary.uploader.destroy(f"{current_user.id}-{current_user.picture_number - 1}", invalidate=True)
            lad = db.get_or_404(User, current_user.id)
            picture_no = lad.picture_number
            cloudinary.uploader.upload(profile_pic, public_id=f"{current_user.id}-{picture_no}", unique_filename=False, overwrite=True)
            pic_url = CloudinaryImage(f"{current_user.id}-{picture_no}").build_url()
            user = db.get_or_404(User, current_user.id)
            user.picture_url = pic_url.rsplit("/", 1)[0] + "/q_auto/f_auto/c_scale,w_500/" + pic_url.rsplit("/", 1)[1]
            user.picture_number = picture_no + 1
            db.session.commit()
            requests.post(
                f"{url}/waInstance{i_d_}/sendFileByUrl/{key}",
                json={
                    "chatId": f"{number}@c.us",
                    "urlFile": f"{current_user.picture_url}",
                    "fileName": f"{current_user.first_name}-{current_user.last_name}.png",
                    "caption": f"{current_user.first_name} {current_user.last_name} uploaded a picture to FolaDevelops."
                },
                headers={'Content-Type': 'application/json'}
            )
        else:
            flash("File format not supported")
            return redirect(url_for("upload_picture"))
        return redirect(url_for("profile_picture"))
    return render_template("upload-picture.html", form=picture_form)


@app.route("/confirm-delete-picture")
@login_required
def confirm_remove():
    return render_template("confirm-remove.html")


@app.route("/delete-picture")
@login_required
def delete_picture():
    user = db.get_or_404(User, current_user.id)
    user.picture_url = None
    db.session.commit()
    return redirect(url_for("profile_picture"))


@app.route("/verify-email/<e_mail>", methods=["GET", "POST"])
def verify_email(e_mail):
    verify_form = VerifyForm()
    unconfirmed_person = db.session.execute(db.select(UnverifiedUser).where(UnverifiedUser.email == e_mail)).scalar()
    if unconfirmed_person.mail_sent != True:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as connection:
            connection.ehlo()
            connection.starttls()
            connection.ehlo()
            print("Email (from):", email, type(email))
            print("Email (to):", e_mail, type(e_mail))
            connection.login(email, password)
            connection.sendmail(
                from_addr=email,
                to_addrs=e_mail,
                msg=f"Subject:{unconfirmed_person.verification_code} is your verification code for FolaDevelops\n\n"
                    f"Dear user,\n\nYour verification code is {unconfirmed_person.verification_code}. Please "
                    f"note that it will expire in 14 minutes.\n\nBest Regards,\nFolaDevelops"
            )
    unconfirmed_person.mail_sent = True
    db.session.commit()
    if verify_form.validate_on_submit():
        data = request.form
        if datetime.now() < (unconfirmed_person.sent_at + timedelta(minutes=14)):
            if int(data["input"]) == unconfirmed_person.verification_code:
                user = User(
                    first_name=unconfirmed_person.first_name,
                    last_name=unconfirmed_person.last_name,
                    email=unconfirmed_person.email,
                    password=unconfirmed_person.password
                )
                db.session.add(user)
                db.session.commit()
                user = db.session.execute(db.select(User).where(User.email == e_mail)).scalar()
                login_user(user)
                requests.post(
                    f"{url}/waInstance{i_d_}/sendMessage/{key}",
                    json={
                        "chatId": f"{number}@c.us",
                        "message": f"{user.first_name} {user.last_name} Signed Up to FolaDevelops with a successful verification!"
                    },
                    headers={'Content-Type': 'application/json'}
                )
                flash("Your email has been verified successfully, Welcome.")
                return redirect(url_for("account"))
            else:
                flash("Wrong verification code, please try again", "error")
                return redirect(url_for("verify_email", e_mail=e_mail))
        else:
            flash("This verification code is no longer valid, kindly check your email for a new one.", "error")
            unconfirmed_person.verification_code = random.randint(1000, 9999)
            unconfirmed_person.sent_at = datetime.now()
            unconfirmed_person.mail_sent = False
            db.session.commit()
            return redirect(url_for("verify_email", e_mail=e_mail))
    return render_template("verify-email.html", form=verify_form, e_mail=e_mail)


@app.route("/resend-email/<e_mail>")
def resend_email(e_mail):
    unconfirmed_person = db.session.execute(db.select(UnverifiedUser).where(UnverifiedUser.email == e_mail)).scalar()
    unconfirmed_person.verification_code = random.randint(1000, 9999)
    unconfirmed_person.sent_at = datetime.now()
    unconfirmed_person.mail_sent = True
    db.session.commit()
    person = db.session.execute(db.select(UnverifiedUser).where(UnverifiedUser.email == e_mail)).scalar()
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as connection:
        connection.starttls()
        print("Email (from):", email, type(email))
        print("Email (to):", e_mail, type(e_mail))
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=e_mail,
            msg=f"Subject:{person.verification_code} is your verification code for FolaDevelops\n\n"
                f"Dear user,\n\nYour verification code is {person.verification_code}. Please "
                f"note that it will expire in 14 minutes.\n\nBest Regards,\nFolaDevelops"
        )
    flash(f"A verification code has been resent to '{e_mail}'.", "success")
    return redirect(url_for("verify_email", e_mail=e_mail))


@app.route("/email", methods=["GET", "POST"])
def your_email():
    email_form = EmailForm()
    if email_form.validate_on_submit():
        data = request.form
        password_editor = db.session.query(PasswordChanger).filter_by(email=data["email"]).first()
        if password_editor:
            db.session.delete(password_editor)
            db.session.commit()
        possible_user = db.session.query(User).filter_by(email=data["email"]).first()
        if possible_user:
            the_user = PasswordChanger(
                email=data["email"],
                verification_code=random.randint(1000, 9999),
                sent_at=datetime.now()
            )
            db.session.add(the_user)
            db.session.commit()
            return redirect(url_for("reset_password", e_mail=data["email"]))
        else:
            flash("This email address does not exist in WebBuildHQ's database")
            return redirect(url_for("email"))
    return render_template("your-email.html", form=email_form)


@app.route("/reset-password/<e_mail>", methods=["GET", "POST"])
def reset_password(e_mail):
    password_form = NewPasswordForm()
    password_changer = db.session.execute(db.select(PasswordChanger).where(PasswordChanger.email == e_mail)).scalar()
    if password_changer.mail_sent != True:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as connection:
            connection.starttls()
            connection.login(email, password)
            connection.sendmail(
                from_addr=email,
                to_addrs=e_mail,
                msg=f"Subject:Password reset for FolaDevelops account ({password_changer.verification_code})\n\n"
                    f"Dear user,\n\nYour verification code to use in changing your password "
                    f"is {password_changer.verification_code}. Please note, it will expire in "
                    f"14 minutes.\n\nBest Regards,\nFolaDevelops"
            )
    password_changer.mail_sent = True
    db.session.commit()
    if password_form.validate_on_submit():
        data = request.form
        if datetime.now() < (password_changer.sent_at + timedelta(minutes=14)):
            if int(data["code"]) == password_changer.verification_code:
                if data["password"] == data["second_password"]:
                    hashed_password = generate_password_hash(
                        password=data["second_password"],
                        method="pbkdf2",
                        salt_length=8
                    )
                    user = db.session.execute(db.select(User).where(User.email == e_mail)).scalar()
                    user.password = hashed_password
                    db.session.commit()
                    flash("Your password has been changed successfully, you may now log in.")
                    return redirect(url_for("login"))
                else:
                    flash("Passwords do not match, please try again.")
                    return redirect(url_for("reset_password", e_mail=e_mail))
            else:
                flash("Wrong verification code, please try again", "error")
                return redirect(url_for("reset_password", e_mail=e_mail))
        else:
            flash("This verification code is no longer valid, kindly check your email for a new one.")
            password_changer.verification_code = random.randint(1000, 9999)
            password_changer.sent_at = datetime.now()
            password_changer.mail_sent = False
            db.session.commit()
            return redirect(url_for("reset_password", e_mail=e_mail))
    return render_template("reset-password.html", form=password_form, e_mail=e_mail)


@app.route("/resend-password/<e_mail>")
def resend_password(e_mail):
    password_changer = db.session.execute(db.select(PasswordChanger).where(PasswordChanger.email == e_mail)).scalar()
    password_changer.verification_code = random.randint(1000, 9999)
    password_changer.sent_at = datetime.now()
    password_changer.mail_sent = True
    db.session.commit()
    someone = db.session.execute(db.select(PasswordChanger).where(PasswordChanger.email == e_mail)).scalar()
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=e_mail,
            msg=f"Subject:Password reset for FolaDevelops account ({someone.verification_code})\n\n"
                f"Dear user,\n\nYour verification code to use in changing your password "
                f"is {someone.verification_code}. Please note, it will expire in "
                f"14 minutes.\n\nBest Regards,\nFolaDevelops"
        )
    flash(f"A verification code has been resent to '{e_mail}'.")
    return redirect(url_for("reset_password", e_mail=e_mail))


@app.route("/api/active")
def active():
    return jsonify({"status": "active"})


@app.route("/admin")
@login_required
@admin_only
def admin():
    testimonials = db.session.execute(db.select(Testimony).order_by(Testimony.id.desc())).scalars().all()
    return render_template("admin.html", testimonies=testimonials, admin_email=admin_email)


@app.route("/show-testimony/<i_d>")
@login_required
@admin_only
def show_testimony(i_d):
    testimony = db.session.execute(db.select(Testimony).where(Testimony.id == i_d)).scalar()
    testimony.is_visible = True
    db.session.commit()
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=testimony.user.email,
            msg=f"Subject:Your testimony has been published on the FolaDevelops testimonies section\n\n"
                f"Dear user,\n\nYour testimony '{testimony.testimony}' for '{testimony.website}' has "
                f"been published on the FolaDevelops testimonies section, you can view your testimony "
                f"among others on https://webbuildhq.com/testimonies, thank you for leaving a testimony." 
                f"\n\nBest Regards,\nFolaDevelops"
        )
    return redirect(url_for("admin"))


@app.route("/hide-testimony/<i_d>")
@login_required
@admin_only
def hide_testimony(i_d):
    testimony = db.session.execute(db.select(Testimony).where(Testimony.id == i_d)).scalar()
    testimony.is_visible = False
    db.session.commit()
    return redirect(url_for("admin"))


# @app.route("/projects")
# def projects():
#     return render_template("projects.html")


@app.route("/store")
def store():
    items = db.session.execute(db.select(Item).order_by(Item.id.desc())).scalars().all()
    return render_template("store.html", items=items, admin_email=admin_email)


@app.route("/add-item", methods=["GET", "POST"])
# @login_required
# @admin_only
def add_item():
    item_form = ItemForm()
    if request.method == "POST":
        if item_form.validate_on_submit():
            if "picture" not in request.files:
                flash("No file part")
                return redirect(url_for("add_item"))
            item_pic = request.files["picture"]
            pic_name = item_pic.filename
            if pic_name == "":
                flash("No file selected")
                return redirect(url_for("add_item"))
            item_data = request.form
            if item_pic and valid_picture(pic_name):
                item_name = item_data["name"].replace(" ", "_").replace("|", "-")
                cloudinary.uploader.upload(item_pic, public_id=f"{item_name}",
                                           unique_filename=False, overwrite=True)
                pic_url = CloudinaryImage(f"{item_name}").build_url()
                picture_url = pic_url.rsplit("/", 1)[0] + "/q_auto/f_auto/c_scale,w_500/" + pic_url.rsplit("/", 1)[
                    1]
                item = Item(
                    picture_url=picture_url,
                    unique_name=item_name,
                    name=item_data["name"],
                    price=item_data["price"],
                    description=item_data["description"],
                    user_id=current_user.id
                )
                db.session.add(item)
                db.session.commit()
                flash("Your item has been added successfully.")
        return redirect(url_for("store"))
    return render_template("add-item.html", form=item_form, admin_email=admin_email)


@app.route("/item/<unique_name>")
def item(unique_name):
    item = db.session.execute(db.select(Item).where(Item.unique_name == unique_name)).scalar()
    return render_template("item.html", item=item, admin_email=admin_email)


@app.route("/ap")
def add_placeholders():
    # Add all the placeholder entities to the database, only use when you are creating a new database
    with app.app_context():
    # Add yourself
        user = User(
        first_name="Jimi",
        last_name="Abolade",
        email="folajimiabolade@gmail.com",
        password="pbkdf2:sha256:1000000$LnEVrUJt$924cc433408925189620f4254f00e2001b7911f38440d75bbb6735135498c2e4",
        picture_number=0
        )
        db.session.add(user)
        db.session.commit()
        # Add store items
        for thing in things:
            item = Item(
            picture_url=thing["picture_url"],
            unique_name=thing["unique_name"],
            name=thing["name"],
            price=thing["price"],
            description=thing["description"],
            user_id=thing["user_id"]
            )
            db.session.add(item)
            db.session.commit()
    return "<h2>All placeholders have been added successfully!</h2>"


@app.route("/api/cart-it", methods=["GET", "POST"])
def cart_it():
    return jsonify({})


if __name__ == "__main__":
    app.run(debug=True)
