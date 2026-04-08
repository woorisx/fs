 // 이미지 슬라이드
const swiper = new Swiper(".swiper", {
    direction: "horizontal",
    loop: "infinite",
    autoplay: {
        delay: 3000,
    },

    // Pagination
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },

    // Navigation arrows
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    }
});


const showSubMenu = () =>{
    let button = document.querySelector('.menu > li > a');
    let subMenu = document.querySelector('.sub');
    
        // 버튼 클릭 이벤트
        if(subMenu.style.display==='none'){
            subMenu.style.display='block';
        }else{
            subMenu.style.display='none';
        }
        // 문서 전체 클릭 이벤트
        document.addEventListener('click', (e) => {
        // 클릭된 요소가 버튼도 아니고 메뉴 내부도 아닐 때
        if (!button.contains(e.target) && !subMenu.contains(e.target)) {
            subMenu.style.display = 'none'; // 메뉴 닫기
        }
    });
}




