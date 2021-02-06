#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/4
# @Author: Lingchen
# @Prescription: 测试AnonymousSurvey类.
#                page_215.
import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """ 针对AnonymousSurvey类的测试. """

    def setUp(self):
        """ 创建一个调查对象和一组答案,供使用的测试方法使用.
            创建一个调查对象,一个答案列表.
        """

        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """ 测试单个答案会被妥善地存储. """

        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # self.my_survey.store_response('English')
        self.my_survey.store_response(self.responses[0])

        # AssertionError: 'English' != ['English'].
        # self.assertEqual('English', my_survey.responses)
        # self.assertIn('English', self.my_survey.responses)
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """ 测试三个答案会被妥善地存储. """

        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # responses = ['English', 'Spanish', 'Mandarin']
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == "__main__":
    unittest.main()
