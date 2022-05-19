function firstLetterUser(USER_NAME) {
    try {
        
        const  userName = document.querySelector(USER_NAME);
    
    
        /**
         * @param user_firstLetter-toUpperCase...
        */
             userName.innerHTML = userName.innerHTML[0].toUpperCase() + userName.innerHTML.slice(1);
    }catch {
        ;
    }

}


export default firstLetterUser;