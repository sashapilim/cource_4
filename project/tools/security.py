import base64
import hashlib
from flask import current_app


def __generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name=current_app.config['HASH_NAME'],
        password=password.encode('utf-8'),
        salt=current_app.config['PWD_HASH_SALT'].encode('utf-8'),
        iterations=current_app.config['PWD_HASH_ITERATIONS'],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')


