#-*-coding:utf-8-*-
"""
MyFrame1类通过wxFormBuilder生成
作者：overpan
电子邮箱：overpan(at)gmail.com
描述：逍遥论坛某版块灌水机
创建时间：2013.04.19
最后修改：2013.04.26
"""
 
import wx, sys, string
import re, random
import gui, os
import urllib, urllib2, cookielib
# Implementing MyFrame1
class Jx3BbsMyFrame1( gui.MyFrame1 ):
    def __init__( self, parent ):
        gui.MyFrame1.__init__( self, parent )
        self.timer = wx.Timer(self, 1)
        self.Bind(wx.EVT_TIMER, self.setTimer, self.timer)
         
    def Denglu_anniu( self, event ):
        name = self.m_ZhanghaoSRK.GetValue()
        pwd = self.m_MimaSRK.GetValue()
        scode = self.m_YanZhengMaSRK.GetValue()
        vals = {'name':name,
                'pwd':pwd,
                'scode':scode,
                'needCode':'0'}
        # 如果登陆成功就将验证码图片框中显示自制的提示图片
        if fbm.logForumId(urllib.urlencode(vals)):
            img = wx.Image('win.jpg', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            self.m_YanZhengMaTPK.SetBitmap(img)
        else:
            m = u"""
            登陆失败，请检查账号密码或者验证码是否输入正确。
            请重开程序重复登陆过程，并确保输入内容正确。
            """
            wx.MessageBox(m, u'错误提示', wx.OK)
            wx.Exit()
 
    def KaishiGuanshui( self, event ):
        if self.timer.IsRunning():
            self.timer.Stop()
            self.m_GuanshuiAN.SetLabel(u'开始')
        else:
            self.timer.Start(32009)
            self.m_GuanshuiAN.SetLabel(u'停止')
 
    def setTimer(slef, event):
        # 一开始并不知道还能用choice还傻傻的直接取随机整数来切片
        cycleEvents(random.choice(g_postMsg).encode('utf-8'))
 
class App(wx.App):
    def OnInit(self):
        frame = Jx3BbsMyFrame1(None)
        frame.Show()
        return True
 
class falseBrowserModel():
    def __init__(self):
        self.cj = cookielib.CookieJar()
        self.op = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.op)
 
    def downloadTheCodeImage(self):
        self.url = "https://my.xoyo.com/login/scode/small/"
        self.image = urllib2.urlopen(self.url).read()
        self.f = open("code.jpg", "wb")
        self.f.write(self.image)
        self.f.close()
 
    def logForumId(self, postdate):
        self.url = "https://my.xoyo.com/login/loginAction/"
        self.htm = urllib2.urlopen(self.url, postdate).read()
        self.url="http://jx3.bbs.xoyo.com/forumdisplay.php?fid=7101&page=2"
        self.htm = urllib2.urlopen(self.url).read()
        self.i = re.search(u'退出'.encode('utf-8'), self.htm)
        if self.i:
            return 1
 
    def refreshPage(self, url):
        return urllib2.urlopen(url).read()
        # 其实我也知道这两个方法其实可以写作一个，不过为了区分还是多写一遍吧
    def postmsg(self, url, msg):
        urllib2.urlopen(url, msg).read()
         
 
def main():
    fbm.downloadTheCodeImage()
    app = App()
    app.MainLoop()
 
def extractData(regex, content, index=1):
    r = '0'
    p = re.compile(regex)
    m = p.search(content)
    if m:
        r = m.group(index)
    return r
 
def cycleEvents(msg):
    url = "http://jx3.bbs.xoyo.com/forumdisplay.php?fid=7101&page=2"
    page = fbm.refreshPage(url)
    regex = 'tid=(\d+).*New'
    tid = extractData(regex, page)
    var_list = ["http://jx3.bbs.xoyo.com/viewthread.php?tid=",
            tid, "&extra=page%3D2"]
    url = ''.join(var_list)
    page = fbm.refreshPage(url)
    regex = 'value="(\w{8,8})"'
    formhash = extractData(regex, page)
    varlist=["http://jx3.bbs.xoyo.com/post.php?action=reply&fid=7101&tid=",
        tid,
        "&extra=page%3D2&replysubmit=yes&infloat=yes&handlekey",
        "=fastpost&inajax=1&local=undefined"]
    url = ''.join(varlist)
    postdate = {'formhash':formhash,
            'subject':'',
            'usesig':'1',
            'message':msg}
    fbm.postmsg(url, urllib.urlencode(postdate))
 
# 到现在都不知道为什么直接使用global定义会出错，只有放在这里了。
fbm = falseBrowserModel()
g_postMsg = [u'好的我知道了，退下吧',
    u'太阳当空照，花儿对我笑',
    u'你的就是我的，我的还是我的',
    u'听说最近脑残片涨价了，我都买不到了',
    u'自己打败自己是最可悲的失败，自己战胜自己是最可贵的胜利。',
    u'用行动祈祷比用言语更能使上帝了解，尽管我是无神论者',
    u'不要问别人为你做了什么，而要问你为别人做了什么。',
    u'你一天的爱心可能带来别人一生的感谢。',
    u'人之所以有一张嘴，而有两只耳朵，原因是听的要比说的多一倍。',
    u'山不辞土，故能成其高；海不辞水，故能成其深！ ']
 
if __name__ == "__main__":
    main()
