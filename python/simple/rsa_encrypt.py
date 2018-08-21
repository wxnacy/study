#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

# 伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)

def encrypt(message, pub_rsa_path):
    '''使用公钥加密'''
    with open(pub_rsa_path) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(message.encode()))
        return cipher_text

def decrypt(secret_message, rsa_path):
    '''使用私钥解密'''
    with open(rsa_path) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        text = cipher.decrypt(base64.b64decode(secret_message), random_generator)
        return text

def signature(message, rsa_path):
    '''使用私钥签名'''
    with open(rsa_path) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        signer = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(message.encode())
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)

        return signature

def verify_signature(message, signature, pub_rsa_path):
    '''验证签名'''
    with open(pub_rsa_path) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        verifier = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        # Assumes the data is base64 encoded to begin with
        digest.update(message.encode())
        print(digest)
        is_verify = verifier.verify(digest, base64.b64decode(signature))
        return is_verify


if __name__ == "__main__":
    plain = 'message'
    pub_rsa_path = '/Users/wxnacy/.ssh/id_rsa.pub'
    rsa_path = '/Users/wxnacy/.ssh/id_rsa'

    sign_pub_rsa_path = '/Users/wxnacy/.ssh/test_gmail_rsa.pub'
    sign_rsa_path = '/Users/wxnacy/.ssh/test_gmail_rsa'

    print('明文：', plain)
    secret = encrypt(plain, pub_rsa_path)
    print('加密文：', secret)
    text = decrypt(secret, rsa_path)
    print('解密文：', text)

    sign = signature(plain, sign_rsa_path)
    print('签名：', sign)
    flag = verify_signature(plain, sign, sign_pub_rsa_path)
    print('验证结果：', flag)
