#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from flask import Flask
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

from datetime import datetime
from sqlalchemy.orm import backref as b

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wxnacy@127.0.0.1:3306/tmddev?charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db=db)

class Screen( db.Model):
    __tablename__ = 'screen'
    id = db.Column(db.BIGINT, primary_key=True)
    code = db.Column(db.String, default="", doc='业务编号')
    name = db.Column(db.String, default="", doc='名称')
    shop_id = db.Column(db.BIGINT, db.ForeignKey("shop.id"), default=0,
                        doc="商品id")
    brand = db.Column(db.String, default="", doc="品牌")
    model = db.Column(db.String, default="", doc="型号")
    mac = db.Column(db.String, default="", doc="mac地址")
    identity = db.Column(db.String, default="", doc="识别标记")
    ver_num = db.Column(db.INT, default=0, doc="版本数字")
    ver_name = db.Column(db.String, default="", doc="版本名称")
    next_ver_num = db.Column(db.INT, default=0, doc='下一个版本')
    type = db.Column(db.INT, default=0,
                     doc="screen layout type: default 0 current layout")
    status = db.Column(db.String, default="unactivated", doc="业务状态")
    layout = db.Column(db.String, default="landscape",
                       doc="横竖屏 portrait/landscape")
    duration = db.Column(db.INT, default=10, doc="图片展示时长")
    is_online = db.Column(db.INT, default=0, doc="是否上线")
    is_available = db.Column(db.INT, default=1)
    time_zone = db.Column(db.INT, default=0, doc="时区")
    volume = db.Column(db.INT, default=50, doc="音量")
    open_duration = db.Column(db.INT, default=0, doc="开机时长")
    sn = db.Column(db.String, default='')
    ext_property = db.Column(db.JSON, default={})
    create_ts = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    update_ts = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    member_begin_ts = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    member_expire_ts = db.Column(db.TIMESTAMP)
    play_source = db.Column(db.String, default='', doc="屏幕播放源")
    play_source_id = db.Column(db.BIGINT, default=0, doc="播放源id")
    is_parse = db.Column(db.INT, default=0, doc="是否解析 youtube")
    remark = db.Column(db.String(512), default='', doc="备注")
    usagefor = db.Column(db.String(64), default='', doc="用途:内部测试 inner_test、合作方自测 coop_test、赠送设备 gift、临时演示 temp_demo")
    is_ad_alliance = db.Column(db.INT, default=0, doc="是否加入联盟")
    is_ad_alliance_report = db.Column(db.INT, default=0,
        doc="是否有联盟广告的反馈")
    gold_coin = db.Column(db.INT, default=0, doc="金币")
    size_weight = db.Column(db.INT, default=1, doc="尺寸权重")
    position_weight = db.Column(db.INT, default=1, doc="位置权重")
    hardware_weight = db.Column(db.INT, default=1, doc="设备权重")

    shop = db.relationship("Shop", backref=b("screens", lazy="dynamic"))

class Shop(db.Model):
    __tablename__ = 'shop'
    id = db.Column(db.BIGINT, primary_key=True)
    code = db.Column(db.String, default="", doc='业务编号')
    name = db.Column(db.String, default="", doc="店铺名")
    logo = db.Column(db.String, default="", doc="logo")
    login_name = db.Column(db.String, default="", doc="登录名")
    login_pass = db.Column(db.String, default="", doc="登陆密码")
    token = db.Column(db.String, default="", doc="token")
    shop_type = db.Column(db.String, default="1",
                          doc="店铺类型: repast/notrepast 1:中餐/2:寿司/3:酒吧/4:KTV/5:韩餐/6:泰餐")
    addr = db.Column(db.String, default="", doc="地址")
    zip = db.Column(db.String, default="", doc="邮编")
    owner = db.Column(db.String, default="", doc="店主")
    mobile = db.Column(db.String, default="", doc="手机")
    email = db.Column(db.String, default="", doc="邮箱")
    language = db.Column(db.String, default="", doc="语言")
    nationality = db.Column(db.String, default="", doc="国籍")
    status = db.Column(db.String, default="", doc="业务状态")
    is_available = db.Column(db.INT, default=1)
    ext_property = db.Column(db.JSON, default={})
    create_ts = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    update_ts = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    is_muslim = db.Column(db.INT, default=0, doc="是否穆斯林")
    price_level = db.Column(db.INT, default=0, doc="价位:1,2,3,4，代表$,$$,$$$,$$$$")
    price_min = db.Column(db.INT, default=0, doc="价位下限")
    price_max = db.Column(db.INT, default=0, doc="价位上限")
    is_alcohol = db.Column(db.INT, default=0, doc="是否允许饮酒")
    shop_area = db.Column(db.INT, default=0, doc="面积")
    seat_number = db.Column(db.INT, default=0, doc="座位数")
    weekly_open_hours = db.Column(db.INT, default=0, doc="周营业小时数")
    daily_customer = db.Column(db.INT, default=0, doc="日均客流量")
    dish_type = db.Column(db.String(64), default='',
                          doc="菜品风格：中餐、日餐、韩餐、泰餐、越餐、印度餐")
    neighborhoods = db.Column(db.String(64), default='', doc="临近的标志地点")
    tag1 = db.Column(db.String(64), default='', doc="标签1")
    tag2 = db.Column(db.String(64), default='', doc="标签2")
    tag3 = db.Column(db.String(64), default='', doc="标签3")
    screen_amount = db.Column(db.INT, default=0, doc="屏幕数量")
    gender = db.Column(db.String, default='', doc='male,famale')
    wechat = db.Column(db.String, default='', doc='微信号')
    tax_id = db.Column(db.String(128), default='', doc="门店税号")
    ssn = db.Column(db.String(128), default='', doc="社会安全码")
    telephone = db.Column(db.String, default='', doc='门店电话')
    daily_open_time = db.Column(db.INT, default=0, doc="开店时间")
    daily_close_time = db.Column(db.INT, default=0, doc="关门时间")
    daily_open_hours = db.Column(db.INT, default=0, doc="开门时长")
    mobile_zone = db.Column(db.String, default="", doc="手机区号")
    open_duration = db.Column(db.INT, default=0, doc="开机时长")
    is_ad_alliance = db.Column(db.INT, default=0, doc="是否加入联盟")
    gold_coin = db.Column(db.INT, default=0, doc="开店币")
    town = db.Column(db.String, default='', doc="城市")
    referral_code = db.Column(db.String, default='', doc="推荐号")




def get_single_screen(**kwargs):
    print(kwargs)
    kwargs.update(dict(is_available=0))

def get_resource(**kwargs):
    print(kwargs)

def get_single_result(result):
    print(result)
    result['sss'] = 'ss'

def preprocessor(**kw):
    print(kw)


def fetch_preprocessor(filters=None, sort=None, group_by=None, single=None,
                       **kw):
    print(kw)

#  ,url_prefix='/api'
screen_include = ['id', 'code', 'is_available',  'mac', 'create_ts', 'shop', 'shop.id', 'shop.code']
screen_api_params = dict(
    methods=['GET'], include_columns=screen_include, results_per_page=2,
    preprocessors={
        "GET_SINGLE": [preprocessor],
        "GET_MANY": [preprocessor],
        "GET_RESOURCE": [preprocessor],
        'GET_COLLECTION': [preprocessor]
    },
    postprocessors={
        "GET_SINGLE": [get_single_result],
        "GET_MANY": [postprocessor],
    },
    allow_functions=True
)
manager.create_api(Screen, **screen_api_params)
shop_include = ['id', 'code', 'name', 'create_ts']
manager.create_api(Shop, methods=['GET'], include_columns=shop_include)

app.run(debug=True)
