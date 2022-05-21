
// Modal window 
function modalWindow(modal_Fade, modalBlock, label_form, modal_Mainblock) {
    try {

        const modalShow = document.querySelectorAll(modal_Fade); 
        const modal = document.getElementById(modalBlock),
                labels = modal.querySelectorAll(label_form),
                modal_block = document.getElementById(modal_Mainblock);
    
    
        labels.forEach(label => {
            if(label.getAttribute("for") == "id_text") {
                label.classList.add("modal_labelText");
            }else if(label.getAttribute("for") == "id_picture") {
                label.classList.add("moda_labelPic");
            }
        });
    
        modalShow.forEach(item => {
            item.addEventListener("click", (e) => {
  
                modal.classList.toggle("fade");
                bodyScroll("fade");
            });
        });

        modal.addEventListener("click",  (e) => {
            if(e.target == modal) {
                modal.classList.toggle("fade");
                bodyScroll("fade");
            }
        });

        const bodyScroll = (className) => {
                 
            if(modal.classList.contains(className)) {
                document.body.style.overflow = "hidden";
            }else if(!modal.classList.contains(className)){
                document.body.style.overflow = "auto";
            }

        };

    }catch {
       
    }
}

export default modalWindow;