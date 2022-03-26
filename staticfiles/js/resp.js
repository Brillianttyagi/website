// burger = document.querySelector('.burger')
// navbar = document.querySelector('.navbar')
// a = document.querySelectorAll('.navbar .options')

// burger.addEventListener('click',()=>{
//     for (i = 0; i < a.length; i++) {
//         a[i].classList.toggle('v-class-resp');
//     }
//     navbar.classList.toggle('h-nav-resp');
// })

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    //document.getElementById("header").style.marginLeft = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    //document.getElementById("header").style.marginLeft= "0";
};
function myFunction() {
    var x = document.getElementById("password-field");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function myFunction_two() {  
    let alert_ = $('.alert')
    alert_.removeClass('alert-danger')
    alert_[0].innerHTML=''

    let input_ = document.getElementById("login_otp_mobile_or_email")
    let y = input_.value;
    let regexp=RegExp(/^[0-9]{10}$/)
    if(regexp.test(y)==false){
        input_.style.borderColor='red'
        return
    }
    let x = document.getElementById("myDIV");
    x.style.display = "block";
    input_.style.borderColor='green'
    let abc = $('#login_otp_mobile_or_email_submit')[0]
    abc.style.color='black'
    abc.style.padding = '0px 13px'
    abc.disabled=true
    let time=30
    login_otp_setinterval_id = setInterval(() => {
        abc.innerHTML=time
        time-=1

    }, 1000);
    let b = setTimeout(() => {
        clearInterval(login_otp_setinterval_id)
        abc.innerHTML='Resend OTP';
        abc.disabled=false
        
    }, 30000);
    $.post('/account/sendotplogin/',{'mobileNumber':y}).done(()=>{
        
    }).fail((exhr,textStatus,errorThrow)=>{
        let alert_ = $('.alert')
        alert_.addClass('alert-danger')
        if(exhr.status==400){
            
            Swal.fire({
                height: '200px',
                width:'400px',
            position: 'top',
            icon: 'success',
            title: 'Account already registered Please Login',
            showConfirmButton: false,
            timer: 1500
            })
        }
        else 
        Swal.fire({
            height: '200px',
            width:'400px',
        position: 'top',
        icon: 'failed',
        title: 'Failed to send OTP, Please retry',
        showConfirmButton: false,
        timer: 1500
        })
        clearInterval(login_otp_setinterval_id)
        abc.innerHTML='Resend OTP';
        abc.disabled=false
    })
}
function myFunction_three() {
    var x = document.getElementById("menu");
        x.style.display = "block";
    
}

