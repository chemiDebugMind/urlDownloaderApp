function sendEmail() {
    if (document.getElementById('sendEmail').checked) {
        document.getElementById('email-input').style.visibility = 'visible';
    }
    else document.getElementById('email-input').style.visibility = 'hidden';

}