function hidden() {
    const arrow = document.getElementById("arrow");
    const hiddenImages = document.getElementById("hidden-images");

    if (arrow.innerHTML === "►") {
        arrow.innerHTML = "▼";
        hiddenImages.style.display = "block";
    } else {
        arrow.innerHTML = "►";
        hiddenImages.style.display = "none";
    }
}