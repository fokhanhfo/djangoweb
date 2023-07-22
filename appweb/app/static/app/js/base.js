var hidee=document.querySelectorAll(".hide");
console.log(hidee)
var valuelogin=document.querySelector(".hide-login")
var valueregister=document.querySelector(".hide-register")
var valuelogout=document.querySelector(".hide-logout")
var valuemenu=document.querySelector(".hide-menu")
if(user == "AnonymousUser"){
    valuelogin.innerHTML='<a class="nav-link hide-login__link" href="http://127.0.0.1:8000/login/">Đăng nhập</a>';
    valueregister.innerHTML='<a class="nav-link hide-register__link" href="http://127.0.0.1:8000/register/">Đăng kí</a>'
    valuelogout.remove();
}
else{
    var valueloginlink=document.querySelector(".hide-login__link")
    var valueregisterlink=document.querySelector(".hide-register__link")
    valueloginlink.remove();
    valueregisterlink.remove();
    valuemenu.innerHTML='<li><a class="dropdown-item hide-logout" href="http://127.0.0.1:8000/logout/">Logout</a></li>';
}
