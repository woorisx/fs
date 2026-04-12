$(document).ready(function(){
    var menu_offset = $('nav').offset();

    $(window).scroll(function(){
        if($(document).scrollTop() > menu_offset.top){
            $('nav').addClass('menuFixed');
        }else{
            $('nav').removeClass('menuFixed');
        }
    })


    var typed = new Typed('#motto', {
      strings: ['꿈이여, 이루어져라.', '&amp; Everyone deserves a second chance.'],
      typeSpeed: 50,
      backSpeed:50,
      loop:true
    });
});





var backToTop = () =>{
    
    //scroll
    window.addEventListener('scroll', () =>{
        if(document.querySelector('html').scrollTop > 100){
            document.getElementById('topbutton').style.display='block';
        }else{
            document.getElementById('topbutton').style.display='none';
        }
    });
    
    //back to top
    document.getElementById('topbutton').addEventListener('click', ()=>{
        window.scrollTo({
            top:0,
            left:0,
            behavior: 'smooth'
        });
    })
};

var scrollPageEvent = () =>{

    console.log("pageYOffset : "+pageYOffset);
    let pageCount=0;
    let scrollPosition=0
    const bodyObject = document.querySelector('#container');
    const sections = document.querySelectorAll('section').length;
        bodyObject.addEventListener('wheel', function(e){
            e.preventDefault();
            if(e.deltaY < 0){
                //위로
                if(pageCount<=0) return;
                pageCount--;
            }
            if(e.deltaY > 0){
                //아래로
                if(pageCount >= 3) return;
                pageCount++;

            }
            scrollPosition = pageCount * window.innerHeight;
            window.scrollTo({left:0, top:scrollPosition, behavior:"smooth"})
            
            const aObj = document.querySelectorAll(".main-menu > li > a");
            const fixedObj = document.querySelector(".fixed");
                fixedObj.classList.remove("fixed");
                aObj[pageCount].classList.add("fixed");

            aObj.forEach((item, index)=>{
                item.addEventListener('click', function(){
                    aObj.forEach(menu =>{
                        menu.classList.remove('fixed');
                    })
                    item.classList.add("fixed");
                    
                })
            })
        },{passive:false})
    };




// const text = document.getElementById('h1').innerHTML;
// const typingElement = document.getElementById("motto");
// let index =0;
// function type() {
//     if (index < text.length) {
//         typingElement.textContent += text.charAt(index);
//         index++;
//         setTimeout(type,150);// 0.15초 간격으로 반복
//     }
// }

// type();
backToTop();
scrollPageEvent();