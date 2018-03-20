#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''加密工具'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

import hashlib
import time
from urllib.request import urlopen

from Crypto.Cipher import AES
from Crypto import Random
from binascii import b2a_hex, a2b_hex
import base64
import random

class AESecurity():
    @classmethod
    def generate_key(cls):
        '''生成 key 长度必须为 16 位'''
        STR = [
            '0', '1', '2', '3', '4', '5',
            '6', '7', '8', '9', 'a', 'b',
            'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z',
            '!', '@', '#', '$', '^', '&',
            '*', '(', ')'
        ]
        res = [str(STR[int(random.uniform(0, len(STR)))]) for x in range(0, 16)]
        return ''.join(res)

    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        """
        加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
        """
        cryptor = AES.new(self.key, self.mode, self.key)
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext).decode("utf-8")

    def decrypt(self, text):
        '''
        解密后，去掉补足的空格用strip() 去掉
        '''
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text)).decode("utf-8")
        print(plain_text)
        return plain_text.rstrip('\x00')


class Md5():
    @classmethod
    def encrypt(cls, text):
        """
        计算字符的md5摘要
        :param str:
        :return:
        """
        return hashlib.md5(text.encode("utf-8")).hexdigest()

    @classmethod
    def encrypt_by_url(cls, url, max_file_size=100 * 1024 * 1024):
        remote = urlopen(url)
        hash = hashlib.md5()

        total_read = 0
        while True:
            data = remote.read(4096)
            total_read += 4096

            if not data or total_read > max_file_size:
                break
            hash.update(data)
        return hash.hexdigest()

    @classmethod
    def encrypt_by_file(cls, filename):
        hash_md5 = hashlib.md5()
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()


class Base64():
    @classmethod
    def encode(cls, content):
        return base64.b64encode(content.encode()).decode()

    @classmethod
    def decode(cls, content):
        return base64.b64decode(content).decode()


if __name__ == '__main__':
    key = AESecurity.generate_key()
    print(key)
    #  #
    aes = AESecurity(key)
    id = Md5.encrypt('1')
    id = 12
    #  #
    res = aes.encrypt('message')
    print(res)
    plain = aes.decrypt(res)
    print(plain)
    # 820fb3cd26ad5e9bd8925ec34ded98a2
    # 820fb3cd26ad5e9bd8925ec34ded98a2

    #  m1 = Md5.encrypt_by_file('/Users/wxnacy/Documents/app-release-21.apk')
    #  print(m1)
    #  m2 = Md5.encrypt_by_url('https://s3-ap-northeast-1.amazonaws.com/i.vego.tv/app/app-release-21.apk')
    #  print(m2)
    #  key = b'Sixteen byte key sssssss'
    #  print(len(key))
    #  iv = Random.new().read(AES.block_size)
    #  print(iv, len(iv))
    #  cipher = AES.new(key, AES.MODE_CBC, iv)
    #  msg = cipher.encrypt('Attack at dawn')
    #  print(msg)
    #  res = b2a_hex(msg).decode("utf-8")
    #  print(res)
    #  print(b2a_hex(cipher.decrypt(res)).decode('utf-8'))
    #  plain = cipher.decrypt(a2b_hex(res)).decode("utf-8")
    #  print(plain)
