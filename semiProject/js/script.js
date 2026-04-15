
  
const showSubMenu = () => {
    let buttons = document.querySelectorAll('.menu > li');
    let subMenu = document.querySelectorAll('.sub');

    // 버튼 클릭 이벤트
    buttons.forEach((btn, index) => {
        btn.addEventListener('click', () => {
            if (subMenu[index].style.display == 'none') {
                subMenu[index].style.display = 'block';
            } else {
                subMenu[index].style.display = 'none';


            }
        })
    })


    // 3. ⭐️ 핵심: 화면 어디든 클릭하면 서브메뉴 닫기
    document.addEventListener('click', (e) => {
        // 클릭한 대상이 메뉴 내부가 아닐 때만 닫기
        buttons.forEach(item => {
            // 클릭된 요소(e.target)가 item의 자식이 아니면 닫음
            if (!item.contains(e.target)) {
                item.querySelector('.sub').style.display = 'none';
            }
        });
    });


}

const hoverItems = () => {
    let items = document.querySelectorAll('.item');
    let cover = document.querySelectorAll('.item-cover');

    items.forEach((item, index) => {
        item.addEventListener('mouseover', () => {
            if (cover[index].style.display == 'none') {
                cover[index].style.display = 'block';
            } else {
                cover[index].style.display = 'none';
            }
            item.addEventListener('mouseleave', () => {
                if (cover[index].style.display == 'block') {
                    cover[index].style.display = 'none';
                } else {
                    cover[index].style.display = 'block';
                }
            })
        })

    })
}

// 탭 요소
const tabs = document.querySelectorAll(".detail-tabs span");

// 섹션 정보
const sections = [
    { id: "detail", tab: 0 },
    { id: "review", tab: 1 },
    { id: "recommend", tab: 2 },
    { id: "info", tab: 3 }
];

// 👉 클릭 시 이동 + 색 변경
function moveTab(id, index) {
    document.getElementById(id).scrollIntoView({
        behavior: "smooth"
    });

    tabs.forEach(t => t.classList.remove("active"));
    tabs[index].classList.add("active");
}

// 👉 스크롤 시 자동 활성화 (핵심🔥)
window.addEventListener("scroll", () => {
    let scrollY = window.scrollY;

    sections.forEach((section, index) => {
        const el = document.getElementById(section.id);
        const buyWrap = document.getElementsByClassName('buyWrap')
        if (!el) return;

        const top = el.getBoundingClientRect().top;
        // const top = el.offsetTop - 120; // 여유값
        const bottom = top + el.offsetHeight;

        if (scrollY >= top && scrollY < bottom) {
            tabs.forEach(t => t.classList.remove("active"));
            tabs[index].classList.add("active");    
        }
    });
});

const buyBar = document.querySelector(".buyWrap");
const footer = document.querySelector("footer");

window.addEventListener("scroll", () => {
    const footerTop = footer.getBoundingClientRect().top;
    const windowHeight = window.innerHeight;

    // footer가 화면에 들어오면 숨김
    if (footerTop < windowHeight) {
        buyBar.style.opacity = "0";
        buyBar.style.pointerEvents = "none";
    } else {
        buyBar.style.opacity = "1";
        buyBar.style.pointerEvents = "auto";
    }
});
$(".menu li a").click(function(){
    $(".menu li a").removeClass("active");
    $(this).addClass("active");
});




showSubMenu();
hoverItems();
