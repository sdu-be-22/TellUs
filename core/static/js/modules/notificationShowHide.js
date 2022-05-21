function notificationShowHide({showNotification, notificationIcon, body}) {
    
    //show hide - notification
    try {
        
        const  showNoti = document.querySelector(showNotification),
                notiIcon = document.getElementById(notificationIcon);
            
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