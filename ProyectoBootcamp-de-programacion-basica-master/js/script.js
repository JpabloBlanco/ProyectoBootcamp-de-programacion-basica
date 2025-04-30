document.addEventListener("DOMContentLoaded", function () {
    document.querySelector(".arrow").addEventListener("click", function () {
        window.scrollTo({
            top: window.innerHeight,
            behavior: "smooth"
        });
    });
});
