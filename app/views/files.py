import os
# from app import utils
from flask import Blueprint, request, jsonify

files = Blueprint("file", __name__)


# 文件上传
# 参数：accesstoken 、 文件信息等
@files.route('/api/upload', methods=['GET', 'POST'])
def get_receivefile():
    param = request.form.get("n")
    if param == "123":
        f = request.files["file"]
        f.save(os.path.dirname(__file__)+'/../asset/upload/'+f.filename)
        return jsonify({"status": "ok"})
    else:
        return jsonify({"status": "false"})


# 文件下载
# 参数：accesstoken 、 文件id
@files.route('/api/download', methods=['GET', 'POST'])
def get_download():
    return jsonify({"status": "ok"})