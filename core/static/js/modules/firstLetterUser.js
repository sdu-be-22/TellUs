function firstLetterUser(userName) {
    const  user_name = document.querySelector(userName);


        /**
     * @param user_firstLetter-toUpperCase...
     */
    user_name.innerHTML = user_name.innerHTML[0].toUpperCase() + user_name.innerHTML.slice(1);

}


export default firstLetterUser;