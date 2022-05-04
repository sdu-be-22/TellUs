function changeRowsCols(tagForm, tagTextarea) {
    try {

        const form = document.getElementById(tagForm),
                textarea = form.querySelector(tagTextarea);
    
        textarea.setAttribute("rows", 30);
        textarea.setAttribute("cols", 100);
    }catch {
        
    }

}

export default changeRowsCols;