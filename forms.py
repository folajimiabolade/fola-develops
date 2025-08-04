# Import necessary libraries and modules
# flask-wtforms are used to render forms with cross-site-request-forgery protection on the front-end(web page)
# https://flask-wtf.readthedocs.io/en/0.15.x/quickstart/
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, BooleanField, URLField, TextAreaField, FileField, IntegerField
from wtforms.validators import DataRequired, Length, Email, InputRequired, URL


class SignupForm(FlaskForm):
    first_name = StringField(
        label="First Name",
        validators=[DataRequired(), Length(max=1000)],
        render_kw={"class": "field signup-field", "placeholder": "Your First Name"}
    )
    last_name = StringField(
        label="Last Name",
        validators=[DataRequired(), Length(max=1000)],
        render_kw={"class": "field signup-field", "placeholder": "Your Last Name"}
    )
    email = EmailField(
        label="Email",
        validators=[DataRequired(), Email()],
        render_kw={"class": "field signup-field", "placeholder": "e.g. name@email.com"}
    )
    password = PasswordField(
        label="Password",
        validators=[DataRequired(), Length(min=8)],
        render_kw={"class": "field signup-field", "placeholder": "8 characters or more"}
    )
    second_password = PasswordField(
        label="Re-enter password",
        validators=[DataRequired(), Length(min=8)],
        render_kw={"class": "field signup-field", "placeholder": "8 characters or more"}
    )
    privacy = BooleanField(label="", validators=[DataRequired(), InputRequired()])
    button = SubmitField(label="Sign Up", render_kw={"class": "text button signup-button signup-field"})
    submit = SubmitField(label="Submit", render_kw={"class": "text button signup-button signup-field"})


class LoginForm(FlaskForm):
    email = EmailField(
        validators=[DataRequired()],
        render_kw={"class": "field", "placeholder": "", "autocomplete": "email"}
    )
    password = PasswordField(
        validators=[DataRequired()],
        render_kw={"class": "field", "placeholder": ""}
    )
    button = SubmitField(label="Login", render_kw={"class": "text button login-button"})


class TestimonyForm(FlaskForm):
    website = URLField(
        label="URL of website built (Optional)",
        # validators=[DataRequired(), URL()],
        render_kw={"class": "field add-field website", "placeholder": "https://website.com"}
    )
    testimony = TextAreaField(
        label="Testimony",
        validators=[DataRequired()],
        render_kw={"class": "field add-field", "placeholder": "Your Testimony"}
    )
    button = SubmitField(label="Submit", render_kw={"class": "text button add-button"})


class PictureForm(FlaskForm):
    picture = FileField(render_kw={"class": "text upload-picture"})
    button = SubmitField(label="Upload", render_kw={"class": "button upload-button"})


class SettingsForm(FlaskForm):
    first_name = StringField(
        label="First Name",
        validators=[DataRequired(), Length(max=1000)],
        render_kw={"class": "field signup-field", "placeholder": "Your First Name"}
    )
    last_name = StringField(
        label="Last Name",
        validators=[DataRequired(), Length(max=1000)],
        render_kw={"class": "field signup-field", "placeholder": "Your Last Name"}
    )
    email = EmailField(
        label="Email",
        validators=[DataRequired(), Email()],
        render_kw={"class": "field signup-field", "placeholder": "e.g. name@email.com"}
    )
    submit = SubmitField(label="Submit", render_kw={"class": "text button signup-button signup-field"})


class VerifyForm(FlaskForm):
    input = IntegerField(
        label="Type code here",
        validators=[DataRequired()],
        render_kw={"class": "field verify-input", "placeholder": "Code"}
    )
    submit = SubmitField(label="Submit", render_kw={"class": "text button signup-button signup-field verify-button"})


class PasswordForm(FlaskForm):
    password = PasswordField(
        label="Your password",

    )
    second_password = PasswordField(
        label="Re-enter password"

    )
    submit = SubmitField(
        label="Change password",
        render_kw={"class": "text button signup-button signup-field"}
    )


class EmailForm(FlaskForm):
    email = EmailField(
        validators=[DataRequired()],
        render_kw={"class": "field your-email", "placeholder": "Your email", "autocomplete": "email"}
    )
    button = SubmitField(label="Verify", render_kw={"class": "text button signup-button"})


class NewPasswordForm(FlaskForm):
    code = IntegerField(
        validators=[DataRequired()],
        render_kw={"class": "field verify-input signup-field new-password", "placeholder": "Verification code"}
    )
    password = PasswordField(
        validators=[DataRequired(), Length(min=8)],
        render_kw={"class": "field signup-field new-password", "placeholder": "New password"}
    )
    second_password = PasswordField(
        validators=[DataRequired(), Length(min=8)],
        render_kw={"class": "field signup-field new-password", "placeholder": "Re-enter password"}
    )
    submit = SubmitField(
        label="Change password",
        render_kw={"class": "text button signup-button signup-field"}
    )
