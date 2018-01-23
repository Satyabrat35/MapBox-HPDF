window.onload = function () {
  sign_in = document.getElementById('signin');
  form = document.getElementById('myForm');
  sign_in.onclick = function () {
    form.action = "/signin"
  }
}
