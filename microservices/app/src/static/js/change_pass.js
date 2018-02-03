window.onload = function () {
  sign_in = document.getElementById('change_pass');
  form = document.getElementById('myForm');
  sign_in.onclick = function () {
    form.action = "/change_pass"
  }
}
