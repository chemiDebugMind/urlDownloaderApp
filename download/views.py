from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render
from .models import Downloader
import requests
import threading
from django.utils import timezone
from django.urls import reverse
import socket
import os
import zipfile
from django.contrib import messages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication
import ssl
from django.core.files import File
import io
def index(request):
    if request.method == 'POST':
        input_url = request.POST['urls']
        urls = input_url.split(',')
        threads = []
        download_folder = 'downloads'
        os.makedirs(download_folder, exist_ok=True)
        for url in urls:
            thread = threading.Thread(target=download_file, args=(url, download_folder))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
        
        files = [os.path.join(download_folder, os.path.basename(url)) for url in urls]
        zip_file_name = 'download.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            for file_name in files:
                zip_file.write(file_name)
        response = FileResponse(open(zip_file_name, 'rb'), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="%s"' % zip_file_name


        if (response.status_code == 200):
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            try:
                download = Downloader(urls=input_url,ip_address=IPAddr)
                if(len(request.POST['email']) != 0):
                    send_email(request.POST['email'],zip_file_name)
                    download.receiver_email = request.POST['email']
            except (KeyError):
                return render(request,'download/download.html', {
                    'urls': input_url,
                })
            else:
                download.save()
                messages.success(request, 'Download completed!')

                return response
                # return render(request, 'download/downloaded_files.html', {'message': 'Download completed!', 'response': response})
        else:
            return HttpResponse(status=404)
    else:
        return render(request,'download/download.html')


def download_file(url, download_folder):
    response = requests.get(url,stream=True)
    file_name = os.path.basename(url)
    file_path = os.path.join(download_folder, file_name)

    with open(file_path, 'wb') as f:
        for data in response.iter_content(1024):
            f.write(data)
                
    return file_name



def send_email(receiver_email,zip_file_name):
    # Create the message object
    message = MIMEMultipart()
    message['Subject'] = 'Your Downloaded File'
    message['From'] = 'tenzinchemi50@gmail.com'
    message['To'] = receiver_email

    # Attach the downloaded file to the message
    
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(zip_file_name, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename=zip_file_name)  
    message.attach(part)

    # Send the email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login('tenzinchemi50@gmail.com', '...')
        smtp.sendmail('tenzinchemi50@gmail.com', receiver_email, message.as_string())
    return 'success'






