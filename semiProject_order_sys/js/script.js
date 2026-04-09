


const showSubMenu = () =>{
    let buttons = document.querySelectorAll('.menu > li');
    let subMenu = document.querySelectorAll('.sub');
    
    // 버튼 클릭 이벤트
    buttons.forEach((btn, index)=>{
        btn.addEventListener('click', ()=>{
            if(subMenu[index].style.display=='none'){
                subMenu[index].style.display='block';
            }else{
                subMenu[index].style.display='none';
               
                
            }
        })
    })
    

    // 3. ⭐️ 핵심: 화면 어디든 클릭하면 서브메뉴 닫기
    document.addEventListener('click', (e) => {
        // 클릭한 대상이 메뉴 내부가 아닐 때만 닫기
        buttons.forEach(item => {
            // 클릭된 요소(e.target)가 item의 자식이 아니면 닫음
            if (!item.contains(e.target)) {
            item.querySelector('.sub').style.display='none';
            }
        });
    });
      
    
}

const hoverItems = ()=>{
    let items = document.querySelectorAll('.item');
    let cover = document.querySelectorAll('.item-cover');

    items.forEach((item, index) =>{
        item.addEventListener('mouseover',()=>{
            if(cover[index].style.display=='none'){
                cover[index].style.display='block';
            }else{
                cover[index].style.display='none';
            }
            item.addEventListener('mouseleave', ()=>{
            if(cover[index].style.display=='block'){
                cover[index].style.display='none';
            }else{
                cover[index].style.display='block';
            }
        })
        })
        
    })
}

showSubMenu();
hoverItems();
