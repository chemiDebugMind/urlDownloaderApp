# Download App

The download app is a Django app that allows users to download multiple files from different URLs simultaneously, and then combine them into a zip file for easy downloading. This app also allows users to receive an email with the zip file attached after downloading.

## Installation
1. Install Django: pip install django
2. Add 'download' to the INSTALLED_APPS list in your Django project's settings.py file.
3. Run python manage.py migrate to create the necessary database tables for the Downloader model.
4. Import the download URL configuration into your Django project's urls.py file by adding the following line: path('download/', include('download.urls'))

### Usage
1. Navigate to the download page by visiting /download/ in your browser.
2. Enter one or more URLs in the input field, separated by commas.
3. If you would like to receive an email with the downloaded files, enter your email address in the "Email" field.
4. Click the "Download" button.
5. Wait for the download to complete. A zip file containing all downloaded files will be automatically generated.
6. If you entered an email address, you will receive an email with the zip file attached.

#### Notes
- The download_file function downloads files in chunks of 1024 bytes to avoid loading large files into memory all at once.
- The send_email function sends the email using the SMTP protocol and Gmail's SMTP server. You will need to provide your own Gmail account credentials in order to use this functionality.
- The Downloader model logs each download request, including the URLs downloaded, the IP address of the requester, and the email address (if provided).


