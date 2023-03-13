function toggleEmailInput() {
    var emailInput = document.getElementById("email-input");
    var sendEmailCheckbox = document.getElementById("sendEmail");
    var email = document.getElementById("email");

    
    if (sendEmailCheckbox.checked) {
        emailInput.style.display = "block";
        // Set the 'required' attribute
        email.setAttribute("required", "");
    } else {
        emailInput.style.display = "none";
        // Remove the 'required' attribute
        email.removeAttribute("required");
    }
}


console.log("hello world!")