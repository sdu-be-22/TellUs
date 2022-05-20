function changeRowsColsTextArea(tagForm, tagTextarea, rows, cols) {
    try {

        const form = document.querySelector(tagForm),
                textarea = form.querySelector(tagTextarea);
      
        textarea.setAttribute("rows", rows);
        textarea.setAttribute("cols", cols);
    }catch {
       
    }

}

export default changeRowsColsTextArea;