# # Search test
# from flask import Flask, render_template
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import String, Integer, DateTime, ForeignKey, text, Boolean
#
#
# class Base(DeclarativeBase):
#     pass
#
#
# db = SQLAlchemy(model_class=Base)
#
#
# class Person(db.Model):
#     __tablename__ = "people"
#     id: Mapped[int] = mapped_column(Integer(), primary_key=True)
#     name: Mapped[str] = mapped_column(String())
#     number: Mapped[int] = mapped_column(Integer())
#
#
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pegasus"
# db.init_app(app)
#
#
# with app.app_context():
#     db.create_all()
#
#
# @app.route("/")
# def index():
#     query = Person.query.filter(Person.name.ilike(f'%chloe%')).all()
#     return render_template("test.html", query=query)
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
#
# # End of search test


# # Pagination test
# from flask import Flask, render_template
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import String, Integer, DateTime, ForeignKey, text, Boolean
#
#
# class Base(DeclarativeBase):
#     pass
#
#
# db = SQLAlchemy(model_class=Base)
#
#
# class Person(db.Model):
#     __tablename__ = "people"
#     id: Mapped[int] = mapped_column(Integer(), primary_key=True)
#     name: Mapped[str] = mapped_column(String())
#     number: Mapped[int] = mapped_column(Integer())
#
#
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pegasus"
# db.init_app(app)
#
#
# with app.app_context():
#     db.create_all()
#
#
# @app.route("/<int:page_number>")
# def index(page_number):
#     people = db.select(Person).order_by(Person.id)
#     book = db.paginate(select=people, page=page_number, per_page=6)
#     sub_people = book.items
#     link_helpers = book.iter_pages(left_current=1, right_current=2)
#     return render_template("test.html", page_number=page_number, book=book, people=sub_people, pages=link_helpers)
#
#
# if __name__ == "__main__":
#     app.run(debug=True)

# # End of pagination test


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(email, password)
#     connection.sendmail(
#         from_addr=email,
#         to_addrs=e_mail,
#         msg=f"Subject:{unconfirmed_person.verification_code} is your verification code for WebBuildHQ\n\n"
#             f"Dear user,\n\nYour verification code is {unconfirmed_person.verification_code}. Please "
#             f"note that it will expire in 14 minutes.\n\nBest Regards,\nWebBuildHQ"
#     )


    # with smtplib.SMTP("smtp.ethereal.email", 587) as connection:
    #     connection.starttls()
    #     connection.login("era99@ethereal.email", "vqr3dG8HWUHu23AMhY")
    #     connection.sendmail(
    #         from_addr="reply@webbuildhq.com",
    #         to_addrs=e_mail,
    #         msg=f"Subject:Password reset for WebBuildHQ account ({password_changer.verification_code})\n\n"
    #             f"Dear user,\n\nYour verification code to use in changing your password "
    #             f"is {password_changer.verification_code}. Please note it will expire in "
    #             f"14 minutes.\n\nBest Regards,\nWebBuildHQ"
    #     )


from flask import Flask, render_template, request, jsonify


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Replace with the Ethereal credentials you got
SMTP_SERVER = "smtp.ethereal.email"
SMTP_PORT = 587
USERNAME = "abdullah.schuster@ethereal.email"
PASSWORD = "NXrqmBnURWTmKRNyGz"


email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")
smtp_server = "smtp.gmail.com"

# Create the message
msg = MIMEMultipart("alternative")
# msg["From"] = "Test App <no-reply@example.com>"
# msg["To"] = "recipient@example.com"
msg["Subject"] = "Your order made on August 8, 2025 at 23:48:54 UTC has been confirmed."
msg["From"] = email
msg["To"] = "folajimiabolade@gmail.com"
# msg["Subject"] = "4096 is your verification code for FolaDevelops"
# msg["Subject"] = "5124 is the code to reset your password for your FolaDevelops account"

order_successful = """
    <html>
    <body style="font-family: 'Noto Sans', sans-serif; background-color: ; padding: 20px;">
        <div style="background: #E7F2E4; padding: 20px; padding-top: 0; padding-bottom: 10px; border-top-left-radius: 8px; border-top-right-radius: 8px; max-width: 500px; margin: auto; background: #2b3035; overflow:hidden;">

            <img src="https://res.cloudinary.com/foladevelops/image/upload/v1755608891/fola-develops-dark_vywcqv.png" alt="Company Logo" width="34%" style="display:block; border:0; outline:none; text-decoration:none; margin: auto; padding-top: 10px; margin-bottom: 0;">
        </div>

        <div style="background: #E7F2E4; padding: 20px; padding-top: 0; border-bottom-left-radius: 8px; border-bottom-right-radius: 8px; max-width: 500px; margin: auto; margin-top: 0; overflow:hidden;">
            <p style="height: 1px; "background: #E7F2E4; "></p>

            <p style="color: #2b3035; font-size: 14px; font-weight: 500; "background: #E7F2E4; ">Hi Maxwell,</p>
            <p style="color: #2b3035; font-size: 14px; font-weight: 500;">Your order made on August 8, 2025 at 23:48:54 UTC has been confirmed successfully.</p>
            
            <p style="height: 1px"></p>

            <p style="color: #2b3035; font-size: 14px; font-weight: 500;">You ordered for:</p>
            <p style="color: #2b3035; font-size: 14px; font-weight: 500;">Item 1:</p>
            <table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;background: #E7F2E4;padding-top: 8px; border:0.5px solid #2b3035;">
                <tr>
                    <td style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px;border-top:0.5px solid #2b3035; font-weight: 500;">Image</td>
                    <td align="right" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px;border-top:0.5px solid #2b3035;">
                        <img src="https://res.cloudinary.com/foladevelops/image/upload/v1755356537/air_fryer_kdigcd.jpg" alt="Company Logo" style="display:block; border:0; outline:none; text-decoration:none; width: 50px; height: 50px; object-fit: cover;">
                    </td>
                </tr>
                <tr>
                    <td style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px; border-top:0.5px solid #2b3035;">Name</td>
                    <td align="right" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px; border-top:0.5px solid #2b3035;">SILVER CREST 8L Extra Large Capacity Digital AirFryer</td>
                </tr>
                <tr>
                    <td style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px;border-top:0.5px solid #2b3035; font-weight: 500;">Quantity</td>
                    <td align="right" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px;border-top:0.5px solid #2b3035;">2</td>
                </tr>
                <tr>
                    <td style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px; border-top:0.5px solid #2b3035;  border-bottom:0.5px solid #2b3035;">Price</td>
                    <td align="right" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px; border-top:0.5px solid #2b3035;  border-bottom:0.5px solid #2b3035;">₦36,785</td>
                </tr>
            </table>

            <p style="height: 1px"></p>

            <p style="color: #2b3035; font-size: 14px; font-weight: 500;">Item 2:</p>
            <table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;background: #E7F2E4;padding-top: 8px;border:0.5px solid #2b3035;">
                <tr>
                    <td style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px;border-top:0.5px solid #2b3035; font-weight: 500;">Image</td>
                    <td align="right" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px;border-top:0.5px solid #2b3035;">
                        <img src="https://res.cloudinary.com/foladevelops/image/upload/v1755356221/clothes_wlkwp1.jpg" alt="Company Logo" style="display:block; border:0; outline:none; text-decoration:none; width: 50px; height: 50px; object-fit: cover;">
                    </td>
                </tr>
                <tr>
                    <td style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px; border-top:0.5px solid #2b3035;">Name</td>
                    <td align="right" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px; border-top:0.5px solid #2b3035;">Men's Shorts And T-shirt Set -2 Pieces - Black</td>
                </tr>
                <tr>
                    <td style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px;border-top:0.5px solid #2b3035; font-weight: 500;">Quantity</td>
                    <td align="right" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px;border-top:0.5px solid #2b3035;">8</td>
                </tr>
                <tr>
                    <td style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px; border-top:0.5px solid #2b3035;  border-bottom:0.5px solid #2b3035;">Price</td>
                    <td align="right" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px; border-top:0.5px solid #2b3035;  border-bottom:0.5px solid #2b3035;">₦8,690</td>
                </tr>
            </table>

            <p style="height: 1px"></p>

            <table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;background: #E7F2E4;padding-top: 8px;border:0.5px solid #2b3035;">
                <tr>
                    <td style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px; border-top:0.5px solid #2b3035;  border-bottom:0.5px solid #2b3035;">Total</td>
                    <td align="right" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px; border-top:0.5px solid #2b3035;  border-bottom:0.5px solid #2b3035;">₦143,090</td>
                </tr>
            </table>

            <p style="height: 1px"></p>

            <p style="color: #2b3035; font-size: 14px; font-weight: 500;">Thanks for exploring!</p>


            <p style="color: #2b3035; font-size: 14px; font-weight: 500;">Warm regards,</p>

            <img src="https://res.cloudinary.com/foladevelops/image/upload/v1755623630/Fola_A_D_Script_ll0rr6.png" alt="Folajimi Abolade Logo" width="120" style="display:block; border:0; outline:none; text-decoration:none;">

            <p style="height: 1px"></p>
            <p style="height: 1px"></p>

            <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                <tr>
                    <td align="center">
                        <a href="https://foladevelops.onrender.com/"
                        style="display: inline-block; text-align: center; padding: 15px 45px; background-color: #0065F8; color: #E7F2E4; text-decoration: none; border-radius: 4px; font-size: 14px;">
                            Visit Website
                        </a>
                    </td>
                </tr>
                </table>
            

            

            <p style="height: 1px"></p>

            <p style="color: #2b3035; font-size: 14px; font-weight: bold; text-align: center; text-decoration: underlin;">Socials:</p>

            <table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;padding-top: 8px;">
                <tr>
                    <td align="center" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;width: ">
                        <a href="https://wa.me/2348067071135"
                            style="display:inline-block; background: #E7F2E4; background-image:url('https://res.cloudinary.com/foladevelops/image/upload/v1755618726/outline-whatsapp-wa-watsup-green-logo-icon-symbol-sign_szj5lc.png'); 
                                    background-size:cover; border-radius:8px; 
                                    color:#fff; font-family:Arial,sans-serif; 
                                    font-size:16px; text-decoration:none; padding:12px 12px;">
                            
                        </a>
                    </td>

                    <td align="center" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;width: ">
                        <a href="https://github.com/folajimiabolade"
                            style="display:inline-block; background-image:url('https://res.cloudinary.com/foladevelops/image/upload/v1755618724/aawpwnuou_hfei6a.webp'); 
                                    background-size:cover; border-radius:8px; 
                                    color:#fff; font-family:Arial,sans-serif; 
                                    font-size:16px; text-decoration:none; padding:12px 12px;">
                            
                        </a>
                    </td>

                    <td align="center" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;width: ">
                        <a href="https://www.linkedin.com/in/folajimi-abolade-379a01362"
                            style="display:inline-block; background-image:url('https://res.cloudinary.com/foladevelops/image/upload/v1755621132/7a791a7183478843b347a5d17fc79e13_qxdmu1.webp'); 
                                    background-size:cover; border-radius:8px; 
                                    color:#fff; font-family:Arial,sans-serif; 
                                    font-size:16px; text-decoration:none; padding:12px 12px;">
                            
                        </a>
                    </td>
                    

                </tr>
            </table>
            
            <div style="height: 5px"></div>

            <table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;padding-top: 8px;">
                <tr>
                    <td align="center" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;width: 33.33%">
                        <p style="color: #2b3035; font-size: 10px; font-weight: 500;">WhatsApp</p>
                    </td>

                    <td align="center" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;width: 33.33%">
                        <p style="color: #2b3035; font-size: 10px; font-weight: 500;">GitHub</p>
                    </td>

                    <td align="center" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;width: 33.33%">
                        <p style="color: #2b3035; font-size: 10px; font-weight: 500;">LinkedIn</p>
                    </td>
                    

                </tr>
            </table>

            <p style="height: 1px"></p>

        </div>
    </body>
    </html>
"""

verify_email = """<html>
    <body style="font-family: 'Noto Sans', sans-serif; background-color: ; padding: 20px;">
        <div style="background: #E7F2E4; padding: 20px; border-radius: 8px; max-width: 500px; margin: auto;">

            <img src="https://res.cloudinary.com/foladevelops/image/upload/v1755608886/fola-develops-light_iaekwp.png" alt="Company Logo" width="166.66" style="display:block; border:0; outline:none; text-decoration:none; margin: auto;">

            <p style="height: 1px"></p>

            <p style="color: #2b3035; font-size: 14px; font-weight: 500;">Dear user,</p>
            <p style="color: #2b3035; font-size: 14px; font-weight: 500;">Your verification code is:</p>
            <p style="color: #0065F8; font-size: 30px; font-weight: 900; text-align: center;">4096</p>
            <p style="color: #2b3035; font-size: 14px; font-weight: 500;">Please note that it will expire in 14 minutes.</p>
            
            <p style="height: 1px"></p>

            <p style="color: #2b3035; font-size: 14px; font-weight: 500;">Best regards,</p>

            <img src="https://res.cloudinary.com/foladevelops/image/upload/v1755623630/Fola_A_D_Script_ll0rr6.png" alt="Folajimi Abolade Logo" width="120" style="display:block; border:0; outline:none; text-decoration:none;">

            <p style="height: 1px"></p>


            <table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;padding-top: 8px;">
                <tr>
                    <td align="center" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;width: ">
                        <a href="https://wa.me/2348067071135"
                            style="display:inline-block; background: #E7F2E4; background-image:url('https://res.cloudinary.com/foladevelops/image/upload/v1755618726/outline-whatsapp-wa-watsup-green-logo-icon-symbol-sign_szj5lc.png'); 
                                    background-size:cover; border-radius:8px; 
                                    color:#fff; font-family:Arial,sans-serif; 
                                    font-size:16px; text-decoration:none; padding:12px 12px;">
                            
                        </a>
                    </td>

                    <td align="center" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;width: ">
                        <a href="https://github.com/folajimiabolade"
                            style="display:inline-block; background-image:url('https://res.cloudinary.com/foladevelops/image/upload/v1755618724/aawpwnuou_hfei6a.webp'); 
                                    background-size:cover; border-radius:8px; 
                                    color:#fff; font-family:Arial,sans-serif; 
                                    font-size:16px; text-decoration:none; padding:12px 12px;">
                            
                        </a>
                    </td>

                    <td align="center" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;width: ">
                        <a href="https://www.linkedin.com/in/folajimi-abolade-379a01362"
                            style="display:inline-block; background-image:url('https://res.cloudinary.com/foladevelops/image/upload/v1755621132/7a791a7183478843b347a5d17fc79e13_qxdmu1.webp'); 
                                    background-size:cover; border-radius:8px; 
                                    color:#fff; font-family:Arial,sans-serif; 
                                    font-size:16px; text-decoration:none; padding:12px 12px;">
                            
                        </a>
                    </td>
                    

                </tr>
            </table>
            
            <div style="height: 5px"></div>

            <table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;padding-top: 8px;">
                <tr>
                    <td align="center" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;width: 33.33%">
                        <p style="color: #2b3035; font-size: 10px; font-weight: 500;">WhatsApp</p>
                    </td>

                    <td align="center" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;width: 33.33%">
                        <p style="color: #2b3035; font-size: 10px; font-weight: 500;">GitHub</p>
                    </td>

                    <td align="center" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;width: 33.33%">
                        <p style="color: #2b3035; font-size: 10px; font-weight: 500;">LinkedIn</p>
                    </td>
                    

                </tr>
            </table>

            <p style="height: 1px"></p>

        </div>
    </body>
    </html>"""

reset_password = """<html>
    <body style="font-family: 'Noto Sans', sans-serif; background-color: ; padding: 20px;">
        <div style="background: #E7F2E4; padding: 20px; border-radius: 8px; max-width: 500px; margin: auto;">

            <img src="https://res.cloudinary.com/foladevelops/image/upload/v1755608886/fola-develops-light_iaekwp.png" alt="Company Logo" width="166.66" style="display:block; border:0; outline:none; text-decoration:none; margin: auto;">

            <p style="height: 1px"></p>

            <p style="color: #2b3035; font-size: 14px; font-weight: 500;">Dear user,</p>
            <p style="color: #2b3035; font-size: 14px; font-weight: 500;">Your verification code to use in changing your password is:</p>
            <p style="color: #0065F8; font-size: 30px; font-weight: 900; text-align: center;">5124</p>
            <p style="color: #2b3035; font-size: 14px; font-weight: 500;">Please note, it will expire in 14 minutes.</p>
            
            <p style="height: 1px"></p>

            <p style="color: #2b3035; font-size: 14px; font-weight: 500;">Best regards,</p>

            <img src="https://res.cloudinary.com/foladevelops/image/upload/v1755623630/Fola_A_D_Script_ll0rr6.png" alt="Folajimi Abolade Logo" width="120" style="display:block; border:0; outline:none; text-decoration:none;">

            <p style="height: 1px"></p>


            <table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;padding-top: 8px;">
                <tr>
                    <td align="center" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;width: ">
                        <a href="https://wa.me/2348067071135"
                            style="display:inline-block; background: #E7F2E4; background-image:url('https://res.cloudinary.com/foladevelops/image/upload/v1755618726/outline-whatsapp-wa-watsup-green-logo-icon-symbol-sign_szj5lc.png'); 
                                    background-size:cover; border-radius:8px; 
                                    color:#fff; font-family:Arial,sans-serif; 
                                    font-size:16px; text-decoration:none; padding:12px 12px;">
                            
                        </a>
                    </td>

                    <td align="center" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;width: ">
                        <a href="https://github.com/folajimiabolade"
                            style="display:inline-block; background-image:url('https://res.cloudinary.com/foladevelops/image/upload/v1755618724/aawpwnuou_hfei6a.webp'); 
                                    background-size:cover; border-radius:8px; 
                                    color:#fff; font-family:Arial,sans-serif; 
                                    font-size:16px; text-decoration:none; padding:12px 12px;">
                            
                        </a>
                    </td>

                    <td align="center" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;width: ">
                        <a href="https://www.linkedin.com/in/folajimi-abolade-379a01362"
                            style="display:inline-block; background-image:url('https://res.cloudinary.com/foladevelops/image/upload/v1755621132/7a791a7183478843b347a5d17fc79e13_qxdmu1.webp'); 
                                    background-size:cover; border-radius:8px; 
                                    color:#fff; font-family:Arial,sans-serif; 
                                    font-size:16px; text-decoration:none; padding:12px 12px;">
                            
                        </a>
                    </td>
                    

                </tr>
            </table>
            
            <div style="height: 5px"></div>

            <table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;padding-top: 8px;">
                <tr>
                    <td align="center" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;width: 33.33%">
                        <p style="color: #2b3035; font-size: 10px; font-weight: 500;">WhatsApp</p>
                    </td>

                    <td align="center" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;width: 33.33%">
                        <p style="color: #2b3035; font-size: 10px; font-weight: 500;">GitHub</p>
                    </td>

                    <td align="center" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;width: 33.33%">
                        <p style="color: #2b3035; font-size: 10px; font-weight: 500;">LinkedIn</p>
                    </td>
                    

                </tr>
            </table>

            <p style="height: 1px"></p>

        </div>
    </body>
    </html>"""


# Attach HTML body
msg.attach(MIMEText(order_successful, "html"))

# Send the email
# with smtplib.SMTP_SSL(smtp_server, 465, timeout=60) as server:
#     server.login(email, password)
#     server.sendmail(msg["From"], msg["To"], msg.as_string())


# Send the email
# with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=60) as server:
#     server.ehlo()
#     server.starttls()
#     server.ehlo()
#     server.login(USERNAME, PASSWORD)
#     server.sendmail(msg["From"], msg["To"], msg.as_string())


# print("✅ Email sent! Go to https://ethereal.email and log in with your test credentials to preview it.")

jimi = """liva"""
print(f'{jimi } wiva')



app = Flask(__name__)

@app.route("/")
def test():
    return order_successful
b = '#0065F8;'
a = """
        <a href="https://example.com"
            style="display: inline-block; text-align: center; padding: 10px 15px; background-color: #007BFF; color: white; text-decoration: none; border-radius: 4px;">
            Visit Site
        </a> """

th = """<tr style="background: #E7F2E4;">
                    <th align="left" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px;">Item</th>
                    <th align="right" style="font-family:'Noto Sans', sans-serif;font-size:14px;color: #2b3035;padding:10px;">Price</th>
                </tr>"""

if __name__ == "__main__":
    app.run(debug=True)
