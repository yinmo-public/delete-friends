# -*- coding: utf-8 -*-
from linepy import *
yinmo = LINE ()
oepoll = OEPoll(yinmo)
for contact in yinmo.getAllContactIds():
    yinmo.deleteContact(yinmo.getAllContactIds())
    print("已刪除1位好友")