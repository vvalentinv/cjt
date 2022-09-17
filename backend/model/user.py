class User:
    def __init__(self, user_id, first_name, last_name, email, password, phone, role_name, description, photo_url):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone
        self.role_name = role_name
        self.description = description
        self.photo_url = photo_url

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "role_name": self.role_name,
            "description": self.description,
            "photo": self.photo_url
        }
