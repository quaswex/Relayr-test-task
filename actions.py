# -*- coding: utf-8 -*-

from splinter.browser import Browser
from locators import LoginPage


class BaseActions(object):
    def __init__(self):
        self.browser = Browser('chrome')
        '''
        Sorry for this eternal URL, but you got tricky access to API page :)
        The fastest way to make test work
        '''
        self.base_url = 'https://api.relayr.io/oauth2/auth?client_id=3b383d97-8287-4a95-8bc6-c4cfeb5ddc6a&redirect_uri=https://developer.relayr.io/dashboard/scrape&response_type=token&scope=access-own-user-info+configure-devices+read-device-history'

    def destroy(self):
        browser = self.browser
        browser.quit()


class Actions(BaseActions):

    def open_page(self, url):
        browser = self.browser
        browser.visit('%s%s' % (self.base_url, url))

    def authorize(self, login, password):
        browser = self.browser
        browser.driver.implicitly_wait(10)
        self.open_page("")
        browser.find_by_css(LoginPage.email_field).type(login)
        browser.find_by_css(LoginPage.password_field).type(password)
        browser.find_by_css(LoginPage.confirm_button).click()

    def find_by_css(self, elem):
        browser = self.browser
        browser.driver.implicitly_wait(15)
        assert browser.find_by_css(elem)
