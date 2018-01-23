	
function validate() {
	var pass = document.getElementById('password');
	var cpass = document.getElementById('conf_password');

	if(pass.value != cpass.value){
		cpass.setCustomValidity("Password do not match");
	}
	else if(pass.length < 8){
		pass.setCustomValidity("Length cannot be less than 8");
	}
	else {
		cpass.setCustomValidity('');
	}
	}
//pass.onchange = validate;
//cpas.onkeyup = validate;

window.onload = function() {
	sign_up = document.getElementById('signup');
    form = document.getElementById('myForm');
    document.getElementById('password').onchange = validate;
    document.getElementById('conf_password').onkeyup = validate;
	sign_up.onclick = function() {
		form.action = "/signup"
	}
}