import smtplib
import random

#otp =str(random.randint(100000,999999))
otp=['','','','','','']
for i in range(0,6):
    otp[i]=random.randint(0,9)
#otp[2]=5
a=str(otp)
print(a)
b=int((a[1]+a[4]+a[7]+a[10]+a[13]+a[16]))
c=str(b)
smtp_port=587
smtp_server='smtp.gmail.com'
gondereninMaili='ayasiraltun@gmail.com'
alaninMaili=input('mail adresini girin: ')
password='rwqxcwrihjtxerhd'
konu=f'tek kullanimlik sifreniz: {c}'
mesage=c
message='''From: %s\nTo: %s\nSubject: %s\n%s\n 
'''% (gondereninMaili,alaninMaili,konu,mesage)

s = smtplib.SMTP(smtp_server,smtp_port)
s.ehlo()
s.starttls()
s.ehlo()
s.login(gondereninMaili,password)
#s.sendmail(gondereninMaili, alaninMaili,message)


kullaniciOtp=int(input('otp kodunuzu girin: '))
if kullaniciOtp == b:
    print('otp kodunuzu doğru girdiniz')
else:
    print('otp kodunuzu yanlış girdiniz')


