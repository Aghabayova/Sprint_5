from generators import generate_random_email, generate_random_password, generate_random_name

REGISTRATION_DATA = {
    "valid": {
        "name": generate_random_name(),
        "email": generate_random_email(),
        "password": generate_random_password()
    },
    "invalid_password": {
        "name": generate_random_name(),
        "email": generate_random_email(),
        "password": "123"
    }
}

LOGIN_DATA = {
    "valid": {
        "email": 'sam@gmail.com',
        "password": '1234567890'
    }
}

URLS = {
    "base": "https://stellarburgers.nomoreparties.site",
    "login": "/login",
    "register": "/register",
    "profile": "/profile",
    "restore_password": '/forgot-password'
}
