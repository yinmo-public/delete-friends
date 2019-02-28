# -*- coding: utf-8 -*-
from linepy import *
yinmo = LINE ()
int1 = len(yinmo.getAllContactIds())
if int1 == 0:
    print("Friendslist Empty")
else:
    for contact in yinmo.getAllContactIds():
        if contact in "u085311ecd9e3e3d74ae4c9f5437cbcb5":
            pass
        try:
            print("Unfriend " + yinmo.getContact(contact).displayName)
            yinmo.deleteContact(contact)
        except:
            pass
    print("\nYou unfriend" + str(int1) + "friends")
    