function notificationShowHide({showNotification, notificationIcon, body}) {
    const  showNoti = document.querySelector(showNotification),
            notiIcon = document.getElementById(notificationIcon);

        //show hide - notification
        try {

            body.addEventListener("click", (event) => {
                let target = event.target;
        
                if(target === notiIcon) {
                    showNoti.classList.add("subheader_show");
                }else {
                    showNoti.classList.remove("subheader_show");
                }
            });
        
            notiIcon.addEventListener("click", () => {
                if(!showNoti.classList.contains("subheader_show")) {
                    showNoti.classList.add("subheader_show");
                }else {
                    showNoti.classList.remove("subheader_show");
                }
            });
        }catch(e) {
            console.log("Plase sign in", e.message);
        }
}

export default notificationShowHide;