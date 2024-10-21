let wishListBtn = document.getElementsByClassName('wish-icon');


for(let i = 0; i < wishListBtn.length; i++){
    wishListBtn[i].addEventListener('click', function(){
        const productId = this.getAttribute('data-product-id');        
        //baseUrl = baseUrl.slice(0, -2);
        let url = baseUrlsplit + productId + '/';
        //let url = `wishlist/${productId}/`
        fetch(url , {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.added_to_wishlist) {
                this.classList.add('filled');
            } else {
                this.classList.remove('filled');
            }
        });

    })

}