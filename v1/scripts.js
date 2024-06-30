function scrollToForm() {
    document.getElementById('cta').scrollIntoView({ behavior: 'smooth' });
}

document.getElementById('signupForm').addEventListener('submit', function(e) {
    e.preventDefault();
    var email = document.getElementById('email').value;
    document.getElementById('message').innerText = `Thank you for signing up, ${email}!`;
    document.getElementById('signupForm').reset();
});
