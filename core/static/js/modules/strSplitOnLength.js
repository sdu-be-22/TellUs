function paragraphSplit(tagP) {

    const para = document.getElementById(tagP);


    function strSplitOnLength(data, your_desired_width) {
        if(data.length <= 0) {
            return [];
        }
    
        let splitData = data.split(/([\s\n\r]+)/);
        let arr = []; 
        let cnt = 0; 
    
        for(let i =0; i < splitData.length; i++) {
            if(!arr[cnt]) {
                arr[cnt] = "";
            }
    
            if (your_desired_width < (splitData[i].length + arr[cnt].length)) {
                cnt++;
                
            }
            arr[cnt] += splitData[i];
        }
    
        return arr;
    }


    const arrStr = strSplitOnLength(para.innerHTML, 140)
    console.log(arrStr);
    para.innerHTML = arrStr[0];
}

export default paragraphSplit; 