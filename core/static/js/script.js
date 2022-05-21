/**
 * @param {obj} loaded-DOM elements 
 * @param {DOM} clickShowHide-notification
 * @param {DOM} scrollSubHead - position fixed
 * @param {slide} slider- with npm package tiny slider ❤
 * @param {main} mainScript - all import in this file 
 */

import numericPost          from "./modules/numericPost";
import subheaderScroll      from "./modules/subheaderScroll"; 
import labelFormHide        from "./modules/labelFormHide";
import notificationShowHide from "./modules/notificationShowHide"; 
import slider               from "./modules/tinySlide";
import labelFormChanged     from "./modules/labelFormChanged"; 
import tinySlideModified    from "./modules/tinySlideModified"; 
import modalWindow          from "./modules/modalWindow";
import changeRowsColsTextArea       from "./modules/changeRowsColsTextArea";
import globeIO              from "./modules/globe";

window.addEventListener('DOMContentLoaded', () => { 
    
    /**
     * @property.import  allelements-get variables
     */

    slider();
    globeIO();
    subheaderScroll("subheader", document.body);
    numericPost(".popular_post_number");
    modalWindow('#modal', "exampleModal", "label", "modal_block");
    changeRowsColsTextArea("#update_data", "textarea", 30, 100);
    labelFormHide({
        labelForm: "label",
        tagForm: ".style_label_mt25",
        TextArea: "id_text"
    });
    changeRowsColsTextArea(".style_label_mt25", "textarea", 10, 37);


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



