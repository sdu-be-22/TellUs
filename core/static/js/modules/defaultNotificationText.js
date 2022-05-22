function defaultNotification(notificationDrop, checkElementsSum, txt ) {
    try {

        const notificationDropDown = document.querySelector(notificationDrop), 
                tagLi = notificationDropDown.querySelectorAll(checkElementsSum);
    
        const defaulTxt = document.createElement("p");
    
        if(tagLi.length < 1) {
            defaulTxt.innerHTML = txt;
            notificationDropDown.append(defaulTxt);
        }
    }catch {
        
    }

}

export default defaultNotification;