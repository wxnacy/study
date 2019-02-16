#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64

#  伪随机数生成器
random_generator = Random.new().read

def encrypt(message, pub_rsa_path):
    '''使用公钥加密'''
    with open(pub_rsa_path) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = PKCS1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(message.encode()))
        return cipher_text

def decrypt(secret_message, rsa_path):
    '''使用私钥解密'''
    with open(rsa_path) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = PKCS1_v1_5.new(rsakey)
        text = cipher.decrypt(base64.b64decode(secret_message), random_generator)
        return text


if __name__ == "__main__":
    plain = 'message'
    pub_rsa_path = '/Users/wxnacy/.ssh/id_rsa.pub'
    rsa_path = '/Users/wxnacy/.ssh/id_rsa'


    print('明文：', plain)
    secret = encrypt(plain, pub_rsa_path)
    print('加密文：', secret)
    text = decrypt(secret, rsa_path)
    print('解密文：', text)

