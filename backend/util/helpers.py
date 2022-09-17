import re
import bcrypt

from exception.invalid_parameter_value import InvalidParameter


def hash_registering_password(passwd):
    return bcrypt.hashpw(passwd, bcrypt.gensalt())


def validate_password(passwd, hash1):
    return bcrypt.checkpw(passwd.encode(), hash1)


def validate_name(string):
    reg_invalid_character = r"[^a-zA-Z]"

    if not string:
        raise InvalidParameter("Names cannot be blank")
    if re.findall(reg_invalid_character, string):
        raise InvalidParameter("Names must have only letters a-zA-Z and no other characters or spaces")
    elif len(string) > 30:
        raise InvalidParameter("Names are limited to 30 letters ")
    elif len(string) < 2:
        raise InvalidParameter("Names must have at least 2 letters")

    return True


def validate_phone(string):
    reg_phone = r"[0-9]{3}-[0-9]{3}-[0-9]{4}"
    if not string:
        raise InvalidParameter("mobile phone cannot be blank")
    if not re.match(reg_phone, string):
        raise InvalidParameter("mobile phone format <555-555-5555>")
    if 12 < len(string) > 12:
        raise InvalidParameter("Remove characters to achieve this exact format <555-555-5555>")
    return True


def validate_email(string):
    reg_email = r"[^@]+@[^@]+\.[^@]+"
    if not string:
        raise InvalidParameter("email cannot be blank")
    if not re.match(reg_email, string):
        raise InvalidParameter("accepted email address format is: username@company.domain")
    return True


def validate_password_value(string):
    if not string:
        raise InvalidParameter("password cannot be blank")
    elif not 20 >= len(string) >= 8:
        raise InvalidParameter("Accepted password length is between 8 and 20 characters inclusive")

    if string:
        alphabetical_characters = "abcdefghijklmnopqrstuvwxyz"
        special_characters = "!@#$%^&*"
        numeric_characters = "0123456789"

        lower_alpha_count = 0
        upper_alpha_count = 0
        special_character_count = 0
        numeric_character_count = 0

        for char in string:
            if char in alphabetical_characters:
                lower_alpha_count += 1
            elif char in alphabetical_characters.upper():
                upper_alpha_count += 1
            elif char in special_characters:
                special_character_count += 1
            elif char in numeric_characters:
                numeric_character_count += 1
            else:
                raise InvalidParameter("Password must contain only alphanumeric and special characters from this set (!@#$%^&*)")
        if lower_alpha_count < 1:
            raise InvalidParameter("Password must have at least 1 lowercase character")
        if upper_alpha_count < 1:
            raise InvalidParameter("Password must have at least 1 uppercase character")
        if special_character_count < 1:
            raise InvalidParameter("Password must have at least 1 special (!@#$%^&*) character")
        if numeric_character_count < 1:
            raise InvalidParameter("Password must have at least 1 numeric character")

    return True


def validate_tour(tour):
    if not len(tour.tour_name):
        raise InvalidParameter("You have to add a title")
    if tour.inactive is 2:
        raise InvalidParameter("A status must be chosen before updating the changes")
    try:
        price = int(float(tour.price_per_person_in_cents) * 100)
    except ValueError:
        raise InvalidParameter("The price must be a numeric value with maximum 2 decimal places")
    try:
        bool(tour.inactive)
    except ValueError:
        raise InvalidParameter("Please select a tour status Active or Inactive")

    if price < 0:
        raise InvalidParameter("The price must be a positive value")
    if price > 10000:
        raise InvalidParameter("The price must be a positive value under 100")
    return True
