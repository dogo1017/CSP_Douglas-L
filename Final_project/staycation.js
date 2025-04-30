function hidden() {
    const arrow = document.getElementById("arrow");
    if (arrow.innerHTML === "►") {
        arrow.innerHTML = "▼";
    } else {
        arrow.innerHTML = "►"; 
    }
}