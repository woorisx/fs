const thumbs = document.querySelectorAll(".thumb");
const mainImg = document.getElementById("mainImg");
const zoom = document.getElementById("zoom");

// 썸네일 클릭 시 이미지 변경
thumbs.forEach(thumb => {
  thumb.addEventListener("click", () => {

    // active 제거
    thumbs.forEach(t => t.classList.remove("active"));
    thumb.classList.add("active");

    // 메인 이미지 변경
    mainImg.src = thumb.src;
  });
});

// 확대 기능
mainImg.addEventListener("mousemove", (e) => {

  zoom.style.display = "block";
  zoom.style.backgroundImage = `url(${mainImg.src})`;

  const rect = mainImg.getBoundingClientRect();

  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;

  const xPercent = (x / rect.width) * 100;
  const yPercent = (y / rect.height) * 100;

  zoom.style.backgroundSize = "200%";
  zoom.style.backgroundPosition = `${xPercent}% ${yPercent}%`;
});

// 마우스 나가면 숨김
mainImg.addEventListener("mouseleave", () => {
  zoom.style.display = "none";
});