function labelFormChanged({ labelForm, tagForm, tagInputs, justTagP, Textarea }) {
    try {
        //label form changed
        const label_form = document.querySelectorAll(labelForm),
            form = document.getElementById(tagForm),
            inputs = form.querySelectorAll(tagInputs),
            tagP = form.querySelectorAll(justTagP),
            textArea = document.getElementById(Textarea);

        textArea.setAttribute("rows", 4);
        textArea.setAttribute("cols", 38);

        inputs.forEach((input, i) => {
            let input_box = document.createElement("div");
            input_box.setAttribute("class", "inputbox");

            input_box.append(input);

            //hidden label when user cliced
            textArea.addEventListener("click", () => {
                if (label_form[i].getAttribute("for") == "id_comments")
                    label_form[i].style.opacity = "0";
            });

            //check to append in input
            if (input.getAttribute("name") != "csrfmiddlewaretoken") {
                if (label_form[i] == undefined) {
                    input.after(label_form[0]);
                    if(tagP[i] != undefined) {
                        
                        input.after(tagP[0]);
                    }
                } else {
                    input.after(label_form[i]);
                    if(tagP[i] != undefined) {
                        
                        input.after(tagP[i]);
                    }
                }
            }

            form.append(input_box);
        });

    } catch {
        try {

            //label form changed
            const label_form = document.querySelectorAll(labelForm),
                form = document.getElementById(tagForm),
                inputs = form.querySelectorAll(tagInputs),
                tagP = form.querySelectorAll(justTagP);
    
    
            inputs.forEach((input, i) => {
                let input_box = document.createElement("div");
                input_box.setAttribute("class", "inputbox");
    
                input_box.append(input);
    
                //check to append in input
                if (input.getAttribute("name") != "csrfmiddlewaretoken") {
                    if (label_form[i] == undefined) {
                        input.after(label_form[0]);
                        if(tagP[i] != undefined) {
                            
                            input.after(tagP[0]);
                        }
                    } else {
                        input.after(label_form[i]);
                        if(tagP[i] != undefined) {
                            
                            input.after(tagP[i]);
                        }
                    }
                }
    
                form.append(input_box);
            });
        }catch {
            ;
        }
    }
}

export default labelFormChanged;