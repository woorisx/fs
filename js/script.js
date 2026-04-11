$(document).ready(function(){
    var menu_offset = $('nav').offset();

    $(window).scroll(function(){
        if($(document).scrollTop() > menu_offset.top){
            $('nav').addClass('menuFixed');
        }else{
            $('nav').removeClass('menuFixed');
        }
    })
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
        window.scrollTo({letf:0, top:scrollPosition, behavior:"smooth"})


    },{passive:false})
};


const textElement = document.getElementById('text');
const text = document.querySelector('.typed').innerHTML;
let i = 0;

function typing() {
    if (i < text.length) {
        // 줄바꿈 처리
        if (text.charAt(i) === '\n') {
            textElement.innerHTML += '<br>';
        } else {
            textElement.innerHTML += text.charAt(i);
        }
        
        i++;
        setTimeout(typing, 100);
    
        } 
}

typing();
backToTop();
scrollPageEvent();
typeWriter();