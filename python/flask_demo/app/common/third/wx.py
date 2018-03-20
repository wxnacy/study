#!/usr/bin/env python
# ! -*- coding:utf-8 -*-
"""wx 工具类"""

__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseObject
from app.config import app
from app.config import BaseConfig
from datetime import datetime
from enum import Enum

import requests
import xmltodict
import json


class Action(Enum):
    token = 'token'
    user_get = 'user/get'
    user_info = 'user/info'
    shorturl = 'shorturl'
    create_menu = 'menu/create'


class MediaPlatform():
    def __init__(self, app_id=BaseConfig.WX_MP_APP_ID,
                 app_secret=BaseConfig.WX_MP_APP_SECRET):
        self.app_id = app_id
        self.app_secret = app_secret
        self.origin_url = 'https://api.weixin.qq.com/cgi-bin/{}'
        self.id = BaseConfig.WX_MP_ID

    def get_access_token(self):
        """获取access_token
        https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140183
        """
        return self._get(Action.token.value, grant_type='client_credential',
                         **self._auth_args())

    def get_users(self, access_token, next_openid=None):
        """
        公众号可通过本接口来获取帐号的关注者列表，关注者列表由一串OpenID
        （加密后的微信号，每个用户对每个公众号的OpenID是唯一的）组成。
        一次拉取调用最多拉取10000个关注者的OpenID，可以通过多次拉取的方式来满足需求。
        https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140840
        :param open_id:
        :param access_token:
        :return:
        """
        return self._get(Action.user_get.value, access_token=access_token,
                         next_openid=next_openid)

    def get_user_info(self, access_token, openid, lang=None):
        return self._get(Action.user_info.value, access_token=access_token,
                         openid=openid, lang=lang)

    def generator_short_url(self, access_token, long_url):
        """
        将一条长链接转成短链接。
        https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1443433600
        :param access_token:
        :param long_url:
        :return:
        """
        return self._post(Action.shorturl.value, action='long2short',
                          access_token=access_token, long_url=long_url)

    def create_menu(self, access_token):
        return self._post(Action.create_menu.value, access_token=access_token,
                          button=[dict(type='click', name='测试', key='test')])

    def _auth_args(self):
        return {'appid': self.app_id, 'secret': self.app_secret}

    def _get(self, _action, **kwargs):
        url = self.origin_url.format(_action)
        res = requests.get(url, params=kwargs)
        self._print_res(res.json())
        return res.json()

    def _post(self, _action, **kwargs):
        url = self.origin_url.format(_action)
        params = {"access_token": kwargs.get('access_token')}
        kwargs.pop('access_token')
        res = requests.post(url, params=params, json=kwargs)
        self._print_res(res.json())
        return res.json()

    def _print_res(self, res):
        """打印结果"""
        if 'errcode' in res:
            app.logger.error(res)

    class Message():
        class MsgType(Enum):
            text = 'text'
            news = 'news'
            event = 'event'
            image = 'image'
            voice = 'voice'
            video = 'video'
            location = 'location'
            link = 'link'

        class Event(Enum):
            subscribe = 'subscribe'
            unsubscribe = 'unsubscribe'
            click = 'CLICK'
            view = 'VIEW'
            location = 'LOCATION'

        def __init__(self, xml_input):
            self.msg = json.loads(json.dumps(xmltodict.parse(xml_input)))
            data = self.msg['xml']
            self.owner_id = data['ToUserName']
            self.sender_id = data['FromUserName']
            self.msg_type = data['MsgType']

            self.event = data.get('Event')
            self.event_key = data.get('EventKey')
            # 用户发送消息给公众号会产生的字段
            self.msg_id = data.get('MsgId')
            self.content = data.get('Content')
            self.pic_url = data.get('PicUrl')
            self.media_id = data.get('MediaId')
            self.thumb_media_id = data.get('ThumbMediaId')
            self.media_format = data.get('Format')  # amr speex
            self.location_x = data.get('Location_X')
            self.location_y = data.get('Location_Y')
            self.scale = data.get('Scale')  # 缩放范围
            self.label = data.get('Label')  # 地理位置
            self.title = data.get('Title')
            self.description = data.get('Description')
            self.url = data.get('Url')
            # 用户点击菜单会产生的字段
            self.latitude = data.get('Latitude')
            self.longitude = data.get('Longitude')
            self.precision = data.get('Precision')  # 位置精度

        def is_text(self):
            return self.msg_type == self.MsgType.text.value

        def is_event(self):
            return self.msg_type == self.MsgType.event.value

        def reply_text(self, content):
            """回复文本"""
            return self._generator_reply(content)

        def reply_news(self, news):
            """回复图文消息"""
            return self._generator_reply(msg_type=self.MsgType.news.value,
                                         news=news)

        def _generator_reply(self, *args, **kwargs):
            content = args[0] if args else kwargs.get('content')
            msg_type = kwargs.get('msg_type') or self.MsgType.text.value

            xml = dict(
                ToUserName=self.sender_id,
                FromUserName=self.owner_id,
                CreateTime=int(datetime.now().timestamp()),
                MsgType=msg_type
            )

            if msg_type == self.MsgType.text.value:
                xml['Content'] = content
            elif msg_type == self.MsgType.news.value:
                items = kwargs.get('news')
                xml['Articles'] = dict(item=items)
                xml['ArticleCount'] = len(items)

            return xmltodict.unparse({"xml": xml})

        class New(BaseObject):
            def __init__(self, title, pic_url, url, desc=""):
                self.Title = title
                self.PicUrl = pic_url
                self.Url = url
                self.Description = desc
