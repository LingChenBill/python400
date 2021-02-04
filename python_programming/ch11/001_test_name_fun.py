#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/4
# @Author: Lingchen
# @Prescription: 编写测试用例.
#                需要继承unittest.TestCase.
#                方法必须以test_开头.
#                page_208.
import unittest
from name_fun import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """ 测试name_fun.py. """

    def test_first_last_name(self):
        """ 能够正确地处理像Janis Joplin这样的姓名吗? """

        # TypeError: get_formatted_name() missing 1 required positional argument: 'last'.
        formatted_name = get_formatted_name('janis', 'joplin')
        # 断言方法用来核实得到的结果是否与期望的结果一致.
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """ 能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗? """

        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == "__main__":
    unittest.main()
