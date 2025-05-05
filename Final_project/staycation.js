function toggleimages() {
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
function cursor() {
document.getElementById("arrow").style.cursor = "pointer";
}

function img1text() {
    document.getElementById("img1").
}