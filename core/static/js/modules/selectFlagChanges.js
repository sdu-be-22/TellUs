function selectFlagChanges(language_select, select_options) {

    try {

        const tagSelect = document.querySelector(language_select),
                selectOptions = tagSelect.querySelectorAll(select_options);
        const flagUSA  = document.createElement("img"); 
        const flagRussia = document.createElement("img");
    
    
        flagUSA.setAttribute("src", flagUSAImg);   
        flagRussia.setAttribute("src", flagsRussianImg);   
    
    
       if(tagSelect.options[tagSelect.selectedIndex].text == "Русский (ru)") {
           tagSelect.before(flagRussia);
       }else if(tagSelect.options[tagSelect.selectedIndex].text == "English (en)") {
            tagSelect.before(flagUSA);
       }
    }catch {
            
    }

}

export default selectFlagChanges;