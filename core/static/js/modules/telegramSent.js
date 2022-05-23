function telegramSent(formInput) {
    try {

        const form_input = document.getElementById(formInput),
                modal = document.getElementById("exampleModal2");
    
        form_input.addEventListener("submit", (e) => {

            e.preventDefault();
            modal.classList.toggle("fade");

        });
    }catch {

    }
}

export default telegramSent;