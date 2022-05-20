function labelFormHide({ labelForm, tagForm }) {
    try {

        const form = document.querySelector(tagForm);
        const label_form = document.querySelectorAll(labelForm);
        label_form.forEach((input, i) => {  
            if(input.getAttribute("name") != "csrfmiddlewaretoken") {
               // if(label_form[i] == undefined) {
                    label_form[i].classList.add("hideLabels");
                //}
            }
        });
    }catch(e) {
        console.log(e);
    }
}

export default labelFormHide; 