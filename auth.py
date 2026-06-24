import jwt

SECRET = "lks-secret"

users = {
    "admin@mail.com": {
        "password": "123",
        "role": "admin"
    },

    "puji@mail.com": {
        "password": "123",
        "role": "citizen"
    }
}

def login(email, password):
    user = users.get(email)

    if not user:
        return {"success": False, "message": "user tidak ditemukan"}

    if user["password"] != password:
        return {"success": False, "message": "password salah"}

    token = jwt.encode(
        {"email": email, "role": user["role"]},
        SECRET,
        algorithm="HS256"
    )

    return {"success": True, "token": token}
