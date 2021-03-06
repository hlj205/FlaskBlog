"""
The blog's auth blueprint. Contain the logic of login and logout.
"""
from flask import Blueprint

auth = Blueprint("auth", __name__, url_prefix="/auth/", static_folder="../../static/")
from . import view
