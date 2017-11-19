from gmail import GMail, Message
from random import choice
file_mess = ['note1.html', 'note2.html', 'note3.html']
file_messs = choice(file_mess)

reasons = ['ebola', 'bored', 'tired', 'lazy', 'haha']
reason = choice(reasons)
html_content = html_content.replace('{{reason}}', reason)

template_file = open(file_messs, encoding='utf-8')
html_content = template_file.read()
template_file.close()

print(file_messs)

gmai= GMail('kaizenn.tk@gmail.com','maconglinh')
message = Message(to='kaizenn.tk@gmail.com', html=html_content)
gmai.send(message)




# just feel so boring about it
# i feel i don't suit with this job :(
