#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Jiang Fengbing"
__copyright__ = "Copyright 2016 Jiang Fengbing. All rights reserved."


def main():
    try:
        print open('url.txt', 'r').read()
    except IOError:
        pass


if __name__ == '__main__':
    main()
