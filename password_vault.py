
import sqlite3
import base64
import os
import sys
from getpass import getpass

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Security Configuration
DB_NAME = "vault.db"
ph = PasswordHasher()
