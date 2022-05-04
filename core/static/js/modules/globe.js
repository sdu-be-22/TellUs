var GIO = require('giojs');
const data = require("../service/data.json");

function globeIO() {
    try {
        // get the container to hold the IO globe
        var container = document.getElementById( "globalArea" );
     
        // create controller for the IO globe, input the container as the parameter
        var controller = new GIO.Controller( container );
     
       controller.addData( data );
     
        // call the init() API to show the IO globe in the browser
        controller.setInitCountry("KZ");
        controller.init(); 

    }catch {
        ;
    }
} 

export default globeIO;