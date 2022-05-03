function numericPost(numbercPost) {
    const numberic_post = document.querySelectorAll(numbercPost);
    let count = 0;

        //numberic posts
        numberic_post.forEach((posts, n) => {
            count++;
            if(count < 10) {
                posts.innerHTML = `0${count}`;
            }else {
                posts.innerHTML = `${count}`;
            }
        });
}

export default numericPost;