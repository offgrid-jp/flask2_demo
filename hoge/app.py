from flask import Flask, json, jsonify
from flask.globals import request

app = Flask(__name__)

@app.route('/')
def index():
  return "世界のみなさん、こんにちは"

@app.route('/get1x', methods=["GET"])
def get1x():
  return "GETです"

@app.get('/get2x')
def get2x():
  return request.args["name"] + "です"

@app.get('/get2x/<name2>/myname')
def get2_myname(name2):

  if "name" in request.args:
    name = request.args["name"]
  else:
    name = "ななし"

  return f"{name} {name2}です"

@app.post('/post2x')
def post2x():
  if "name" in request.form:
    name = request.form["name"]
  else:
    name = "ななし"

  if "name2" in request.form:
    name2 = request.form["name2"]
  else:
    name2 = "ななし"

  return f"{name} {name2}です"

@app.post('/post2x/json')
def post2x_json():
  
  # headersにjsonが指定されていなかったらエラー
  if "Content-Type" not in request.headers or request.headers["Content-Type"] != "application/json":
    return jsonify({"message": "json形式ではありません"}), 500

  try:
    # bodyを文字列で取得
    body = request.data.decode("UTF-8")
    # jsonをdict型に変換
    json_data = json.loads(body)

    # 応答メッセージ追加
    json_data["message"] = "ok"

    return jsonify(json_data), 200

  except Exception:
    return jsonify({"message": "jsonの取得でエラーが発生しました"}), 500

