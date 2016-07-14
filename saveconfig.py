#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json

__author__ = "Jiang Fengbing"
__copyright__ = "Copyright 2016 Jiang Fengbing. All rights reserved."


def main():
    try:
        lines = sys.stdin.readlines()
        data = []
        for line in lines:
            line = line.rstrip()
            data.append(line)

        config = {'bucket': data[0], 'username': data[1], 'passwd': data[2], 'url_prefix': data[3]}
        open('config.json', 'w').write(json.dumps(config))
        print u'配置成功!'.encode('utf-8')
        return
    except:
        pass
    print u'配置失败!'.encode('utf-8')


if __name__ == '__main__':
    main()
