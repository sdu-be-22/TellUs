function subheaderScroll(subHeader, body) {
    const  subheader = document.getElementById(subHeader);
    
    
    //scroll
    window.onscroll = function() {
        scrollSubHeader();
    };
    
    function scrollSubHeader() {
        if(body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
            subheader.classList.add("navBar");
            subheader.style.position = `fixed`;
            subheader.style.paddingTop = "30px";
            subheader.style.verticalAlign = "top";
            subheader.style.transition = "0.3s all ease";
        }else {
            subheader.style.position = `relative`;
            subheader.className = subheader.className.replace("navBar", "subheader");
        }
    }
}

export default subheaderScroll;