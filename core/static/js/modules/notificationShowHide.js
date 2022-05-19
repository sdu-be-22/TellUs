function notificationShowHide({showNotification, notificationIcon, body}) {
    const  showNoti = document.querySelector(showNotification),
            notiIcon = document.getElementById(notificationIcon);

        //show hide - notification
        try {

            body.addEventListener("click", (event) => {
                let target = event.target;
        
                if(target === notiIcon) {
                    
                    showNoti.classList.toggle("subheader_show");
                }else {
                    showNoti.classList.remove("subheader_show");
                }
            });
        
        }catch {
           
        }
}

export default notificationShowHide;