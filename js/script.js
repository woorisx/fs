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

backToTop();