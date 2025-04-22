let images = ["https://www.greenthumbsgarden.com/cdn/shop/products/Bartlett_Pear_2_1400x.jpg?v=1580261573", "https://waapple.org/wp-content/uploads/2021/06/Variety_Cosmic-Crisp-transparent-300x300.png", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZbB_doR9LVg_xVbDXOOZc3TNbgNCEIzLLKw&s", "https://i5.walmartimages.com/seo/Fresh-Mangoes-Each-Sweet_cc54242f-cb87-4a25-9baa-fccaa20f5443.64fa79325ad44a7352dcd3c2a8b477be.jpeg"]
let counter = 0

function change() {
    if (counter < images.length) {
    document.getElementById(img).src = images[counter]
    counter += 1
    }else{
        counter = 0
        document.getElementById(img).src = images[counter]        
    }
}

function hello() {
    document.getElementById("title").innerHTML = "Hello World"
}
function hover() {
document.getElementById("img").src = "https://www.greenthumbsgarden.com/cdn/shop/products/Bartlett_Pear_2_1400x.jpg?v=1580261573"
}
function leave() {
document.getElementById("img").src = "https://waapple.org/wp-content/uploads/2021/06/Variety_Cosmic-Crisp-transparent-300x300.png"
}
function hidden(){
    document.getElementById("meme").style.display = "block"
}