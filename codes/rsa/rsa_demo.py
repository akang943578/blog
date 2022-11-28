#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/28 14:28
# @Author  : David Hao
# @File    : rsa_demo.py
# @Software: IntelliJ IDEA

import itertools


def find_mod_reverse(e, r):
    # 这里直接用模逆元定义的概念，for循环找出d
    # 也可以用扩展欧几里得算法或者欧拉定理计算出来
    for d in itertools.count(1):
        if (e * d) % r == 1:
            return d


def get_new_key(p, q, e=3):
    # e的定义是比r小和r互质的的正整数
    # 【注意】: 这里取3是方便计算演示，一般使用65537
    N = p * q
    r = (p - 1) * (q - 1)
    d = find_mod_reverse(e, r)
    return N, e, d


def rsa(N, key, message):
    # 加密和解密本质上都是求指数和模的过程，所以可用参数不同的同一个函数
    # 这也是为什么公私钥可以互换，但是不建议（原因是公钥出于种种原因一般都很短）
    me = message ** key
    return me % N


def rsa_demo(raw_message):
    # 取2个质数
    p = 17
    q = 23
    # 获取公私钥
    (N, e, d) = get_new_key(p, q)
    print('public key: (%s, %s)' % (N, e))
    print('private key: (%s, %s)' % (N, d))

    full_m_c = ''
    for en_m in list(raw_message):
        # 加密
        m = ord(en_m)
        c = rsa(N, e, m)
        full_m_c += chr(c)

    full_raw_message = ''
    for en_c in list(full_m_c):
        # 解密
        c = ord(en_c)
        m = rsa(N, d, c)
        full_raw_message += chr(m)

    print('原始消息：%s' % raw_message)
    print('加密后的值：%s' % full_m_c)
    print('解密后的值：%s' % full_raw_message)


if __name__ == '__main__':
    rsa_demo('hello rsa algorithm!')
