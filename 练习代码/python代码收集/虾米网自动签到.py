#!/usr/bin/python
# encoding:utf-8
# +-----------------------------------------------------------------------------
# | File: xiami_auto_checkin.py
# | Author: huxuan
# | E-mail: i(at)huxuan.org
# | Created: 2011-12-11
# | Last modified: 2013-04-25
# | Description:
# |     Description for xiami_auto_checkin.py
# |
# | Copyrgiht (c) 2012 by huxuan. All rights reserved.
# | License GPLv3
# +-----------------------------------------------------------------------------
 
import re
import os
import sys
import urllib.request as http  # instead of urllib2
import urllib.parse  # urlencode is used
import datetime
import http.cookiejar as cookie
 
 
class XiamiCheckin:
 
    def __init__(self, email=None, password=None):
        print('虾米音乐签到\n')
        # Get log file
        LOG_DIR = os.path.join(os.path.expanduser("~"), 'log')
        if not os.path.isdir(LOG_DIR):
            os.mkdir(LOG_DIR)
        self.LOG_PATH = os.path.join(LOG_DIR, 'xiami_auto_checkin.log')
 
        self.users = set(self.__get_users())
 
        if not self.users:
            return
 
        # Init
        myCookie = http.HTTPCookieProcessor(cookie.CookieJar())
        self.opener = http.build_opener(myCookie)
        http.install_opener(self.opener)
 
        if email and password:
            self.__add_user(email, password)
 
        for each_user in self.users:
            (email, password) = each_user.split(':')
            self.__checkin(email.strip(), password.strip())
 
    def __get_users(self):
        try:
            with open(self.LOG_PATH, 'r', encoding='utf-8') as users:
                return users.readlines()
        except FileNotFoundError:
            print('第一次使用必须添加用户名和密码，只需添加一次\n'
                  '[用法] xiami_auto_checkin.py yourEmail yourPassword')
            return None
 
    def __add_user(self, email, password):
        insert_str = email + ' : ' + password
        if not insert_str + '\n' in self.users:
            with open(self.LOG_PATH, 'a', encoding='utf-8') as users:  # append
                print('添加用户' + email + '\n')
                print(email, ':', password, file=users)
                self.__checkin(email.strip(), password.strip())
        else:
            print('用户已存在\n')
 
    def __check_status(self, response):
        pattern = re.compile(r'<div class="idh">(已连续签到\d+天)</div>')
        result = pattern.search(response)
        if result:
            return result.group(1)
        return False
 
    def __print_result(self, response, email, out=sys.stdout):
        print(datetime.datetime.now(), file=out)
        result = self.__check_status(response)
        if result:
            print('[完成] 已经签到!', email, result, file=out)
        else:
            print('[错误] 登录失败!', email, file=out)
 
    def __login(self, email, password):
        # Login
        login_url = 'http://www.xiami.com/web/login'
        post_data = {'email': email, 'password': password, 'LoginButton': '登陆'}
        # data should be encoded.
        login_data = urllib.parse.urlencode(post_data).encode(encoding='utf8')
        login_headers = {'Referer': 'http://www.xiami.com/web/login', 'User-Agent': 'Opera/9.60'}
        login_request = urllib.request.Request(login_url, login_data, login_headers)
        # login_response = urllib.request.urlopen(login_request).read()
        login_response = self.opener.open(login_request).read().decode('UTF8')
        return login_response
 
    def __checkin(self, email, password):
        login_response = self.__login(email, password)
        checkin_pattern = re.compile(r'<a class="check_in" href="(.*?)">')
        checkin_result = checkin_pattern.search(login_response)
        # 如果已经签到，则直接打印签到次数
        if not checkin_result:
            self.__print_result(login_response, email)
            return
        # 如果未签到，则签到
        checkin_url = 'http://www.xiami.com' + checkin_result.group(1)
        checkin_headers = {'Referer': 'http://www.xiami.com/web', 'User-Agent': 'Opera/9.60'}
        checkin_request = urllib.request.Request(checkin_url, None, checkin_headers)
        checkin_response = self.opener.open(checkin_request).read().decode('UTF8')
        self.__print_result(checkin_response, email + "!!!!")
 
if len(sys.argv) == 3:
    email = sys.argv[1]
    password = sys.argv[2]
    XiamiCheckin(email, password)
else:
    XiamiCheckin()
