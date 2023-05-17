"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7pnu4dadc9vlvt81g-a",
        database="todoo_crj4",
        user="qwert",
        password="qoEfpzHwsOP3LHUtPC3dCaKX1BiXMatw")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
