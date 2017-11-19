from random import *
from gmail import *
open("note1")
gmail = GMail('kaizenn.tk@gmail.com','maconglinh')
msg = Message('Test Message',to='c4e13.lab.huynq@gmail.com',text=randint(note1.html, note2.html, note3.html))
gmail.send(msg)
