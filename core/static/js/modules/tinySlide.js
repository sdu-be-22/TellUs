import { tns } from "./../../../../node_modules/tiny-slider/src/tiny-slider";
function slider() {
        //slide 
        try {

            tns({
                container: '.my-slider',
                speed: 1200,
                items: 1,
                slideBy: 'page',
                autoplay: true,
                autoplayTimeout: 10000,
            });
        }catch(e) {
            console.log(e);
        }
}

export default slider;
