#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import upyun
import datetime
import random
import string

__author__ = "Jiang Fengbing"
__copyright__ = "Copyright 2016 Jiang Fengbing. All rights reserved."


def save_path(path):
    open('path.txt', 'w').write(path)


def save_url(url):
    open('url.txt', 'w').write(url)


def load_config():
    try:
        data = open('config.json', 'r').read()
        return json.loads(data)
    except IOError:
        pass
    return None


def gen_suffix(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))


def gen_remote_path(path):
    file_name = path.split('/')[-1]
    date = datetime.datetime.now().date()
    url_suffix = gen_suffix(4)
    return '/wf/%d-%02d-%02d/%s/%s' % (date.year, date.month, date.day, url_suffix, file_name)


def full_url(remote_path, conf):
    return '%s/%s' % (conf['url_prefix'].rstrip('/'), remote_path)


def upload_pic(path, conf):
    up = upyun.UpYun(conf['bucket'], username=conf['username'], password=conf['passwd'])
    try:
        with open(path, 'rb') as f:
            remote_path = gen_remote_path(path)
            up.put(remote_path, f, checksum=True)
    except upyun.UpYunServiceException as se:
        return False, se.msg
    except upyun.UpYunClientException as ce:
        return False, ce.msg
    except IOError:
        return False, u'文件打开失败!'
    return True, full_url(remote_path, conf)


def main():
    conf = load_config()
    if not conf:
        print u'请配置图床!'.encode('utf-8')
        return

    lines = sys.stdin.readlines()
    if lines:
        path = lines[0]
        path = path.rstrip()
        ext = path.split('.')[-1]
        ext = ext.lower()
        if ext in ['jpg', 'jpeg', 'png', 'bmp', 'tif', 'tiff', 'gif', 'ico']:
            save_path(path)
            ret, msg = upload_pic(path, conf)
            if ret:
                save_url(msg)
        else:
            msg = u'你选中的不是图片文件!'.encode('utf-8')
        print msg


if __name__ == '__main__':
    main()
