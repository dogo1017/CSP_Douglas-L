function toggleimages() {
    const arrow = document.getElementById("arrow");
    const hiddenImages = document.getElementById("hidden-images");

    if (hiddenImages.style.display === "none" || hiddenImages.style.display === "") {
        arrow.innerHTML = "▲";
        hiddenImages.style.display = "block";
    } else {
        arrow.innerHTML = "▼";
        hiddenImages.style.display = "none";
    }
}

function togglefacts() {
    const factsArrow = document.getElementById("facts-arrow");
    const factsList = document.getElementById("facts-list");

    if (factsList.style.display === "none" || factsList.style.display === "") {
        factsArrow.innerHTML = "▲";
        factsList.style.display = "block";
    } else {
        factsArrow.innerHTML = "▼";
        factsList.style.display = "none";
    }
}