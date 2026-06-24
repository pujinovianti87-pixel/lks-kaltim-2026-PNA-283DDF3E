import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer

SECRET = "lks-secret"
security = HTTPBearer()

def verify_token(token: str = Security(security)):
    try:
        data = jwt.decode(token.credentials, SECRET, algorithms=["HS256"])

        # 🔥 PAKSA FORMAT JELAS (INI KUNCI)
        return {
            "email": data.get("email"),
            "role": data.get("role")
        }

    except:
        raise HTTPException(status_code=401, detail="Token tidak valid")
