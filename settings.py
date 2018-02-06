from flask import Flask, redirect, request, jsonify
from flask_pymongo import PyMongo

app = Flask("didsys")
mongo = PyMongo(app)