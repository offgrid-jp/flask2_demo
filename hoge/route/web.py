from flask import Blueprint
from models import Yamada

bp = Blueprint('web', __name__, url_prefix="/yamada")

yamada = Yamada.Yamada()

@bp.get('/name')
def name():
  return yamada.name()

@bp.get('/age')
def age():
  return yamada.age()

@bp.get('/weight')
def weight():
  return yamada.weight()

from route import web_sub
bp.register_blueprint(web_sub.bp)
