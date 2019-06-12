# -*- coding: utf-8 -*-
from linepy import *
from time import sleep
yinmo = LINE ()
int1 = len(yinmo.getAllContactIds())
if int1 == 0:
    print("Friendslist Empty")
else:
    for contact in yinmo.getAllContactIds():
        if contact in "u085311ecd9e3e3d74ae4c9f5437cbcb5":
            pass
        try:
            print("Del " + yinmo.getContact(contact).displayName)
            sleep(0.5)
            yinmo.deleteContact(contact)
        except:
            pass
    print("\nYou del" + str(int1) + "friends")
    
