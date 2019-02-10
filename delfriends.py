# -*- coding: utf-8 -*-
from linepy import *
yinmo = LINE ()
oepoll = OEPoll(yinmo)
int1 = len(yinmo.getAllContactIds())
if int1 == 0:
    print("您還沒有任何好友")
else:
    for contact in yinmo.getAllContactIds():
        print("刪除好友 " + yinmo.getContact(contact).displayName)
        yinmo.deleteContact(contact)
    print("\n您刪除" + str(int1) + "位好友")
    