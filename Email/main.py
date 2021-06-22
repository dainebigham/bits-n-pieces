import smtplib

# yahoo: smtp.mail.yahoo.com
# yahoo Password: truytubhpstpuqef

email = 'testdaine@gmail.com'
password = ''

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email, 
        to_addrs='dainetest@yahoo.com', 
        msg='Subject:Hello World!\n\nMy first cls email!')

# with smtplib.SMTP('smtp.mail.yahoo.com', port=587) as connection:
#     connection.starttls()
#     connection.login(user='dainetest@yahoo.com', password='')
#     connection.sendmail(
#         from_addr='dainetest@yahoo.com', 
#         to_addrs='testdaine@gmail.com', 
#         msg='Subject:Hello World!\n\nMy first cls email!')
