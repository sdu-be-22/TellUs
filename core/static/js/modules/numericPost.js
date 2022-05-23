function numericPost(numbercPost, dynamicCountArticles) {
    try {
    
        const numberic_post = document.querySelectorAll(numbercPost), 
                dynamicCount_Articles= document.getElementById(dynamicCountArticles);
        let count = 0;
        let dynamicCount= {
            count: 0,
        };
            //numberic posts
            numberic_post.forEach((posts, n) => {
                count++;
                dynamicCount.count = count;
             
                if(count < 10) {
                    posts.innerHTML = `0${count}`;
                   
                }else {
                    posts.innerHTML = `${count}`;
                }
            });
            dynamicCount_Articles.innerHTML= `${dynamicCount.count} articles`;
            
    }catch {

    }
}

export default numericPost;