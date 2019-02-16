#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64


def signature(message, rsa_path):
    '''使用私钥签名'''
    with open(rsa_path) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        signer = PKCS1_v1_5.new(rsakey)
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
        verifier = PKCS1_v1_5.new(rsakey)
        digest = SHA.new()
        # Assumes the data is base64 encoded to begin with
        digest.update(message.encode())
        is_verify = verifier.verify(digest, base64.b64decode(signature))
        return is_verify


if __name__ == "__main__":
    plain = 'message'
    pub_rsa_path = '/Users/wxnacy/.ssh/id_rsa.pub'
    rsa_path = '/Users/wxnacy/.ssh/id_rsa'

    sign = signature(plain, rsa_path)
    print('签名：', sign)
    flag = verify_signature(plain, sign, pub_rsa_path)
    print('验证结果：', flag)
