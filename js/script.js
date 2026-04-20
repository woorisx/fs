$(document).ready(function () {
    const nav = document.querySelector("nav");
    const topButton = document.getElementById("topbutton");
    const menuLinks = Array.from(document.querySelectorAll(".main-menu > li > a"));
    const sectionLinks = menuLinks.filter((link) => {
        const href = link.getAttribute("href") || "";
        return href.startsWith("#") && href !== "#";
    });
    const sections = sectionLinks
        .map((link) => document.querySelector(link.getAttribute("href")))
        .filter(Boolean);

    let isWheelLocked = false;

    const getNavHeight = () => (nav ? nav.offsetHeight : 0);

    const getSectionTop = (section) => {
        const top = section.getBoundingClientRect().top + window.scrollY;
        return Math.max(top - getNavHeight(), 0);
    };

    const setActiveMenu = (targetId) => {
        menuLinks.forEach((link) => {
            const href = link.getAttribute("href");
            const isMatch = href === `#${targetId}`;
            const isHome = targetId === "home" && href === "#";
            link.classList.toggle("fixed", isMatch || isHome);
        });
    };

    const syncMenuState = () => {
        if (!nav) {
            return;
        }

        const scrollY = window.scrollY;
        const navTop = nav.offsetTop;

        if (scrollY > navTop) {
            nav.classList.add("menuFixed");
        } else {
            nav.classList.remove("menuFixed");
        }

        let current = null;

        for (let index = sections.length - 1; index >= 0; index -= 1) {
            if (scrollY + getNavHeight() + 20 >= sections[index].offsetTop) {
                current = sections[index];
                break;
            }
        }

        if (scrollY < 40 || !current) {
            setActiveMenu("home");
            return;
        }

        setActiveMenu(current.id);
    };

    const scrollToSection = (section) => {
        window.scrollTo({
            top: getSectionTop(section),
            left: 0,
            behavior: "smooth"
        });
    };

    menuLinks.forEach((link) => {
        link.addEventListener("click", (event) => {
            const href = link.getAttribute("href");

            if (href === "#") {
                event.preventDefault();
                window.scrollTo({ top: 0, left: 0, behavior: "smooth" });
                setActiveMenu("home");
                return;
            }

            const target = document.querySelector(href);

            if (!target) {
                return;
            }

            event.preventDefault();
            scrollToSection(target);
            setActiveMenu(target.id);
        });
    });

    window.addEventListener("scroll", () => {
        if (topButton) {
            topButton.style.display = window.scrollY > 100 ? "block" : "none";
        }

        syncMenuState();
    });

    if (topButton) {
        topButton.addEventListener("click", () => {
            window.scrollTo({
                top: 0,
                left: 0,
                behavior: "smooth"
            });
        });
    }

    document.addEventListener("wheel", (event) => {
        if (window.innerWidth <= 768 || isWheelLocked || sections.length === 0) {
            return;
        }

        const direction = Math.sign(event.deltaY);

        if (direction === 0) {
            return;
        }

        const currentIndex = sections.findIndex((section, index) => {
            const sectionTop = getSectionTop(section);
            const nextTop = index < sections.length - 1 ? getSectionTop(sections[index + 1]) : Number.POSITIVE_INFINITY;
            const currentScroll = window.scrollY + 10;
            return currentScroll >= sectionTop && currentScroll < nextTop;
        });

        let nextIndex = currentIndex;

        if (direction > 0) {
            nextIndex = currentIndex < 0 ? 0 : Math.min(currentIndex + 1, sections.length - 1);
        } else {
            nextIndex = currentIndex <= 0 ? -1 : currentIndex - 1;
        }

        if ((direction < 0 && currentIndex === -1) || nextIndex === currentIndex) {
            return;
        }

        event.preventDefault();
        isWheelLocked = true;

        if (nextIndex === -1) {
            window.scrollTo({ top: 0, left: 0, behavior: "smooth" });
            setActiveMenu("home");
        } else {
            scrollToSection(sections[nextIndex]);
            setActiveMenu(sections[nextIndex].id);
        }

        window.setTimeout(() => {
            isWheelLocked = false;
        }, 700);
    }, { passive: false });

    if (document.getElementById("motto")) {
        new Typed("#motto", {
            strings: ["Dreams are always unfinished.", "&amp; Everyone deserves a second chance."],
            typeSpeed: 50,
            backSpeed: 50,
            loop: true
        });
    }

    syncMenuState();
});
