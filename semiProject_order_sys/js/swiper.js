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
