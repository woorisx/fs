
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