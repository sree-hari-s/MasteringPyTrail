import smtplib

my_email = "sreeharis1999@gmail.com"
password = "vektoylzxigdxcxc"

"""
connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="jepivi4306@jybra.com",
    msg="Subject:Hello\n\nThis is the body of the email")
connection.close()
"""
# ALternative to the above code
with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="jepivi4306@jybra.com",
        msg="Subject:Hello\n\nThis is the body of the email"
    )
