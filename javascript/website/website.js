document.addEventListener("DOMContentLoaded", () => {
    const toggleFlawsBtn = document.getElementById("toggleFlawsBtn");
    const flawsSection = document.getElementById("flawsSection");

    // Toggle visibility of the flaws section
    toggleFlawsBtn.addEventListener("click", () => {
        if (flawsSection.style.display === "none" || flawsSection.style.display === "") {
            flawsSection.style.display = "block";
        } else {
            flawsSection.style.display = "none";
        }
    });
});


const hoverImage = document.getElementById('hoverImage');

const originalSrc = "https://eurotuner.de/wp-content/uploads/photo-gallery/Hennessey-Dodge-Charger-SRT-Hellcat-HPE1000-Redeye-Tuning-Leistungssteigerung-US-Car-Limousine-Topmodell-01.jpg?bwg=1699466276";
const hoverSrc = "https://s.yimg.com/ny/api/res/1.2/cJOCUKmQSNecywJ_BGHOzg--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD04MDA-/https://media.zenfs.com/en/motorious_297/6b0aa773307466984f6e7a22d3ae3c0f";

hoverImage.addEventListener("mouseover", () => {
    hoverImage.src = hoverSrc;
});

hoverImage.addEventListener("mouseout", () => {
    hoverImage.src = originalSrc;
});
