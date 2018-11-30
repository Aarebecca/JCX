import os
import json
from flask import Blueprint, request, jsonify
from app import utils

info = Blueprint('info', __name__)


# 获取新闻列表
# page - 新闻页数
# psize - 每页条数
@info.route('/api/getnewslist', methods=['GET'])
def get_newslist():
    page = request.args.get('page') or "1"
    psize = request.args.get('psize') or "8"
    s = utils.SQL()
    sql = "call `newslist`(" + page + "," + psize + ")"
    return jsonify({"status": "ok", "data": s.query(sql)})


# 根据新闻id获取具体详情
# id - 新闻id
@info.route('/api/getnewsdetail', methods=['GET'])
def get_newsdetail():
    newid = request.args.get("id")
    s = utils.SQL()
    sql = "select * from `news` where id = " + newid
    return jsonify({"status": "ok", "data": s.query(sql)})


# 获取图片链接
@info.route('/api/mainpic', methods=['GET'])
def get_images():
    return jsonify({"status": "ok", "data": json.load(open(os.path.dirname(__file__)+'/../asset/data.json', 'r'),
                                                      encoding='UTF-8')["images"]})


# 获取公告列表
@info.route('/api/getnoticelist', methods=['GET'])
def get_noticelist():
    page = request.args.get('page') or "1"
    psize = request.args.get('psize') or "8"
    s = utils.SQL()
    sql = "call `noticelist`(" + page + "," + psize + ")"
    return jsonify({"status": "ok", "data": s.query(sql)})


# 获取公告详情
@info.route('/api/getnoticedetail', methods=['GET'])
def get_noticedetail():
    nid = request.args.get("id")
    s = utils.SQL()
    sql = "select * from `notice` where id = " + nid
    return jsonify({"status": "ok", "data": s.query(sql)})


# 获取模块列表
@info.route('/api/module', methods=['POST'])
def get_module():
    pass
