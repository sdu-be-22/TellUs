function darkMode(body) {
    if((localStorage.getItem('mode') || 'dark') === 'dark') {
        
     document.querySelector(body).classList.add('dark');

    }else {
        document.querySelector(body).classList.remove('dark');
    }
}
export default darkMode;
