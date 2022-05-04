
// Modal window 
function modalWindow(modal_Fade, modalBlock, label_form) {
    try {

        const modalShow = document.querySelectorAll(modal_Fade); 
        const modal = document.getElementById(modalBlock),
                labels = modal.querySelectorAll(label_form);
    
    
        labels.forEach(label => {
            if(label.getAttribute("for") == "id_text") {
                label.classList.add("modal_labelText");
            }else if(label.getAttribute("for") == "id_picture") {
                label.classList.add("moda_labelPic");
            }
        });
    
        modalShow.forEach(item => {
            item.addEventListener("click", () => {
                modal.classList.toggle("fade");
            });
        });
    }catch {
        ;
    }
}

export default modalWindow;