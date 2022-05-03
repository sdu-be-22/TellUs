/**
 * @param {obj} loaded-DOM elements 
 * @param {DOM} clickShowHide-notification
 * @param {DOM} scrollSubHead - position fixed
 * @param {slide} slider- with npm package tiny slider ❤
 */

import numericPost          from "./modules/numericPost";
import subheaderScroll      from "./modules/subheaderScroll"; 
import firstLetterUser      from "./modules/firstLetterUser";
import notificationShowHide from "./modules/notificationShowHide"; 
import slider               from "./modules/tinySlide";
import labelFormChanged     from "./modules/labelFormChanged"; 
import tinySlideModified    from "./modules/tinySlideModified"; 

window.addEventListener('DOMContentLoaded', () => { 
    
    /**
     * @property.import  allelements-set variables
     */

    slider();
    firstLetterUser(".subheader_user_name");
    subheaderScroll("subheader", document.body);
    numericPost(".popular_post_number");
 
    labelFormChanged({
        labelForm: "label",
        tagForm: "add_form",
        tagInputs: "input",
        Textarea: "id_comments",
        justTagP: "p"
    });

    tinySlideModified({
        buttonPrev: '[data-controls = "prev"]',
        buttonNext: '[data-controls = "next"]', 
        naviga_Tns: "[data-nav]"
    });
 
    notificationShowHide({
        notificationIcon: "subheader_drop_down",
        body: document.body,
        showNotification: ".subheader_drop_down_menu"
    });

});



