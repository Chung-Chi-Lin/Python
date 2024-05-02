# Email 字串解析

email = "z0123456@gmail.com"
email_index = email.index("@")
email_find = email.find("@")

print(email_index)
print(email_find)

print(email[:email_index])
print(email[email_index+1:])
