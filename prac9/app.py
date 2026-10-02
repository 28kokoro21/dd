from flask import flask
import psycopg2
import os

app = flask(__name__)


@app.route("/")
def home():
    try:
        conn=psycopg2.connect(
            host = os.getenv("DB_HOST"),

        ) 
    return 

