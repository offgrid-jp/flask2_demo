from flask import Blueprint
from models import Tarou

bp = Blueprint('web_sub', __name__, url_prefix="/tarou")

tarou = Tarou.Tarou()

@bp.get('/name')
def name():
  return tarou.name()

@bp.get('/age')
def age():
  return tarou.age()

@bp.get('/weight')
def weight():
  return tarou.weight()
