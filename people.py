from main import People

try:
    user_name = input("Enter name \n")
    user_phone_number = input("Enter phone number \n")
    user_email = input("Enter email \n")
    user_county = input("Enter county \n")
    user_gender = input("Enter your gender \n")
    user_religion = input("Enter religion \n")
    user_password = input("Enter your password \n")

    People.create(name=user_name, phone_number=user_phone_number, email=user_email, county=user_county,
                  gender=user_gender, religion=user_religion, password=user_password)
    print("Information created successfully")

except:
    print("Failed to create user information")
