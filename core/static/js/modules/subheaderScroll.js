function subheaderScroll(subHeader, body) {
    const  subheader = document.getElementById(subHeader);
    
    
    //scroll
    // Scroll certain amounts from current position 
    window.onscroll = function() {
        scrollSubHeader();
    };
    
    function scrollSubHeader() {
        if(body.scrollTop > 70 || document.documentElement.scrollTop > 70) {
            subheader.classList.add("navBar");
            subheader.style.position = `fixed`;
            subheader.style.paddingTop = "30px";
            subheader.style.verticalAlign = "top";
            subheader.style.transition = "0.5s all ease-in-out";
           
        }else {
            subheader.style.position = `static`;
            subheader.className = subheader.className.replace("navBar", "subheader");
        }
    }
}

export default subheaderScroll;