document.addEventListener("DOMContentLoaded", () => {
    const hoverTitle = document.getElementById("hover-spot");
    const hiddenImage = document.getElementById("hidden-image");

    hoverTitle.addEventListener("mouseenter", () => {
        hiddenImage.style.display = "block";
    });

    // Commented out the hide command for testing
    // hoverTitle.addEventListener("mouseleave", () => {
    //     hiddenImage.style.display = "none";
    // });
});
