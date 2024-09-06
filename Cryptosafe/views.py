import datetime
import random

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from Cryptosafe.decrypt import *
from Cryptosafe.encrypt import *
from temp_data.models import current_id_no, feedback, user_data


# ***********************************************************************************
def mail_function(reciever_mail, message = "Someone is Trying to access your data"):
    subject = "MAIL FROM CRYPTOSAFE"
    message = '''Greetings of the day!!!!\nWe are here by to inform you that someone tried to access your data\nMay be Your key is leaked. Be assured that we can't leak your key as we don't have the Key anywhere with us.\nWe are here to make sure that the data is accessed by you or by your known ,\nHere are some steps that we recommend you to follow:\n\t1. Fetch Your data from the cryptosafe and save it somewhere on your desktop for a moment.\n\t2. Now, Delete your data from the Cryptosafe.\n\t3. Now save the Data again in Cryptosafe and keep the new key safe.\nIn case ,it's not you then kindly inform us on the gmail provided by us....'''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [reciever_mail]
    send_mail( subject, message, email_from, recipient_list)

def send_otp_function(reciever_mail,otp):
    subject = "MAIL FROM CRYPTOSAFE"
    message = "This is Secret code.\n" + str(otp) + "\nDon't Share OTP with anybody."
    email_from = settings.EMAIL_HOST_USER
    print(otp)
    recipient_list = [reciever_mail]
    send_mail( subject, message, email_from, recipient_list)

def otp_generator():
    global send_otp
    send_otp = random.randint(1000,9999)
# ***********************************************************************************


def home(request):
    # request.session.clear()

    return render(request,"home.html")


# *******************************************************************************************
def store(request):
    # request.session.clear()
    
    ch=0
    try:
        ch = int(request.GET.get("choice"))
        
        if request.method=="POST":
            if ch == 1:
                plain_text = request.POST.get("data_form")
            elif ch == 2:
                plain_text = (request.FILES['data_form']).read().decode('utf-8')

            mail_id = request.POST.get("mail_id")

            request.session['txt'] = plain_text
            request.session['mail'] = mail_id
            return HttpResponseRedirect('otp/')
            
    except:
        pass

    return render(request,"store.html",{"choice" : ch})

send_otp = 0

def store_otp(request):

    if not( "txt" in request.session):
        return HttpResponseRedirect("/store/")
    
    global send_otp
    alert = ""
    plain_text = request.session.get("txt")
    mail_id = request.session.get("mail")

    try:
        if request.method != 'POST':
            otp_generator()
            send_otp_function(mail_id,send_otp)
    except:
        pass

    try:
        if request.method == 'POST':
            en_otp = int(request.POST.get("otp"))
            if en_otp == send_otp:
                cur_id = current_id_no(ref_id = 1000)
                try :
                    cur_id = current_id_no.objects.all()[0]
                except:
                    cur_id = current_id_no(ref_id = 1000)
                
                id = cur_id.ref_id + random.randint(1,9)
                plain_text = "CrYpto" + plain_text
                cipher_text, key = encrypt_plain_text(plain_text , id)
                mail_id = encrypt_mail_id(mail_id, id)

                cur_time = timezone.now()

                data = user_data(user_id = id, encrypted = cipher_text, mail_id = mail_id, date_time = cur_time)
                data.save()
                cur_id.ref_id +=10
                cur_id.save()
                
                del request.session['txt']
                del request.session['mail']
                plain_text = request.session.get("txt")


                data = {
                    "key" : key
                }

                request.session['key'] = key
                return HttpResponseRedirect('key/')
            else:
                alert = "!!!INCORRECT OTP!!!"
    except:
        return render(request,'otp.html',{"alert" : alert})
    
    return render(request,'otp.html',{"alert" : alert})

def store_key(request):
    if not request.session:
        return HttpResponseRedirect("/store/")
    try:
        key = request.session.get('key')
        del request.session['key']
        request.session.clear()
        return render(request,"key.html",{'key':key})
    except:
        pass
    return HttpResponseRedirect("/store/")
# *******************************************************************************************


# *******************************************************************************************
def fetch(request):
    output=""
    data = {"output" : output}
    key_checker = False

    try:
        if request.method == 'POST':
            user_key = request.POST.get("key_form")
            en_user_id = find_id(user_key)
            cipher_text = user_data.objects.get(user_id = en_user_id)
            key_checker = True

            if cipher_text.wrong_count < 5:

                plain_text = decrypt_cipher_text(cipher_text.encrypted,user_key,en_user_id)

                if plain_text[0:6] == "CrYpto" :
                    plain_text = plain_text[6:]
                    cipher_text.date_time = timezone.now()
                    cipher_text.wrong_count = 0
                    cipher_text.save()

                else:
                    user_mail = str(cipher_text.mail_id)
                    user_mail = decrypt_mail_id(user_mail, en_user_id)
                    cipher_text.wrong_count += 1
                    cipher_text.save()
                    if cipher_text.wrong_count == 5:
                        try:
                            message = "Your data is Blocked because of continuous suspicious activities\nWe recommend You to delete the Data and Save it again and keep the New Key Safe and Secure"
                            mail_function(user_mail,message)
                        except:
                            pass

                    try:
                        mail_function(user_mail)
                    except:
                        pass
                    plain_text = "INVALID KEY"

            
            elif cipher_text.wrong_count >= 5:
                plain_text = "Data Blocked"

            data["output"] = plain_text
            
    except:
        if request.method == 'POST' and key_checker == False:
            data["output"] = "INVALID KEY"

    return render(request,"fetch.html",data)
# *******************************************************************************************

def delete(request):
    output=""
    data = {"output" : output}
    key_checker = False

    try:
        if request.method == 'POST':
            user_key = request.POST.get("key_form")
            en_user_id = find_id(user_key)
            cipher_text = user_data.objects.get(user_id = en_user_id)
            key_checker = True
            plain_text = decrypt_cipher_text(cipher_text.encrypted,user_key,en_user_id)
             
            if plain_text[0:6] == "CrYpto" :
                plain_text = "DELETED..\n\tThank You for using our Services!\nRegards, CryptoSafe"
                cipher_text.delete()
                
            else:
                user_mail = str(cipher_text.mail_id)
                user_mail = decrypt_mail_id(user_mail, en_user_id)
                
                try:
                    mail_function(user_mail,"hello")
                except:
                    pass
                plain_text = "INVALID KEY"
            
            data["output"] = plain_text
            
    except:
        if request.method == 'POST' and key_checker == False:
            data["output"] = "INVALID KEY"

    return render(request,"delete.html",data)


# *******************************************************************************************


def about_us(request):

    return render(request,"about_us.html")

# *******************************************************************************************

def _feedback(request):
    try:
        if request.method == 'POST':
            name = request.POST.get("name")
            Address = request.POST.get("Address")
            email = request.POST.get("email")
            country = request.POST.get("country")
            ufeedback = request.POST.get("feedback")
            cur_time = datetime.datetime.now()
            data = feedback(name = name, Address = Address, email = email, country = country, feedback = ufeedback, date_time = cur_time)
            data.save()
            
    except:
        pass

    return render(request,"feedback.html")
# *******************************************************************************************

def why_us(request):
    try:
        pass
    except:
        pass
    return render(request,"why_us.html")

def faq(request):
    return render(request,"faq.html")

def contact_us(request):
    # request.session.clear()

    return render(request,"contact_us.html")

def test(request):
    # request.session.clear()

    return render(request,"test.html")