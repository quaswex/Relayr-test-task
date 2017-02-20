# -*- coding: utf-8 -*-


class LoginPage(object):
    email_field = '#email[name="email"]'
    password_field = '#password[name="password"]'
    confirm_button = 'form#auth_form input[type=submit]'
    welcome_alert = '[id=welcomeAlert]'
    authorization_error = '.error.show'
