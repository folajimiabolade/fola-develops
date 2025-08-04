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