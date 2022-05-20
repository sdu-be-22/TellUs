import { tns } from "./../../../../node_modules/tiny-slider/src/tiny-slider";
function slider() {
        //slide 
        try {

            tns({
                container: '.my-slider',
                mode: "carousel",
                speed: 1200,
                swipeAngle: false,
                items: 1,
                slideBy: 'page',
                autoplay: true,
            });
        }catch(e) {
            console.log(e);
        }
}

export default slider;
