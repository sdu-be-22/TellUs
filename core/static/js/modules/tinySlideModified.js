function tinySlideModified({buttonPrev, buttonNext, naviga_Tns}) {
    //tiny slide modified
   const btnPrev= document.querySelector(buttonPrev),
            btnNext = document.querySelector(buttonNext),
             tns_navs = document.querySelectorAll(naviga_Tns);
    
    try {

        tns_navs.forEach(item => {
            item.classList.add("tns_nav_all");
        });

        btnPrev.innerHTML= "";
        btnNext.innerHTML = "";

        let iconNext = document.createElement("i"), 
            iconPrev = document.createElement("i");
        iconNext.setAttribute("class", "fa-solid fa-caret-right");
        iconPrev.setAttribute("class", "fa-solid fa-caret-left");

        btnNext.append(iconNext);
        btnPrev.append(iconPrev);

        btnNext.classList.add("btnNext");
        btnPrev.classList.add("btnNext");
    }catch(e) {
        console.log("Plase sign in", e.message);
    }
}

export default tinySlideModified;