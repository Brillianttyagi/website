
        const sections = document.querySelectorAll('section');
        const navli = document.querySelectorAll('.menu ul li');
            window.addEventListener('scroll',()=>{
            let current = "";
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;
                if(pageYOffset>sectionTop-sectionHeight/3){
                    current.section.getAttribute('id');
                }
            });
            navli.foreach( li =>{
                li.classList.remove('active-a');
                if(li.classList.contains(current)){
                    li.classList.add('active-a')
                }
            });
        }) ;
        // Get all sections that have an ID defined


// const sections = document.querySelectorAll("section");
// window.addEventListener("scroll", navHighlighter);

// function navHighlighter() {
//   let scrollY = window.pageYOffset;
//   sections.forEach(current => {
//     const sectionHeight = current.offsetHeight;
//     const sectionTop = current.offsetTop - 50;
//     sectionId = current.getAttribute("id");
    
//     if (
//       scrollY > sectionTop &&
//       scrollY <= sectionTop + sectionHeight
//     ){
//       document.querySelector(".menu a[href*=" + sectionId + "]").classList.add("active-a");
//     } else {
//       document.querySelector(".menu a[href*=" + sectionId + "]").classList.remove("active-a");
//     }
//   });
// }
                function toggleMenu(){
        var menuToggle = document.querySelector('.toggle');
        var menu = document.querySelector('#menu');
        menuToggle.classList.toggle('active');
        menu.classList.toggle('active');
        }
        var slideImg = document.getElementById("slideImg");

        var images = new Array(
        "img/1.jpg",
        "img/2.jpg",
        "img/3.jpg",
        "img/4.jpg"
        );
        var len = images.length;
        var i = 0;
        function slider(){
        if(i>len-1){
        i =0;
        }
        slideImg.src = images[i];
        i++;
        setTimeout('slider()',3000);
        }
    