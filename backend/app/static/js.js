const form = document.querySelector('form');
form.addEventListener('submit', (e) => {
  e.preventDefault();
  const username = form.username.value;
  const password = form.password.value;
  const email = form.email.value;
  const formData = new FormData();
  formData.append('username', username);
  formData.append('password', password);
  formData.append('email', email);
  fetch('/createUser', {
    method: 'POST',
    body: formData,
  });
});