#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-05 09:23:14
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import sys
import os


class Student:
    def __init__(self):
        self.__name = ""

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name


def main():
    print(sys.version)
    st1 = Student()
    st1.setName("张三")
    print(st1.getName())
    print(dir(st1))
    print(st1._Student__name)


if __name__ == '__main__':
    main()
