# -*- coding: utf-8 -*-

from locators import LoginPage


class TestTest(object):
    def test_login_positive(self, action):
        action.authorize(login='valid_email_for_relayr@gmail.com',
                         password='valid_password')
        action.find_by_css(LoginPage.welcome_alert)

    def test_login_negative(self, action):
        action.authorize(login='negative_test_user@relayr.io',
                         password='password')
        action.find_by_css(LoginPage.authorization_error)
