let updateBtn = document.getElementsByClassName('update-cart')

for(let i = 0; i < updateBtn.length; i++){
    updateBtn[i].addEventListener('click', function(){
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log(productId)
        console.log(action)

        if(user === 'AnonymousUser'){
            addCookieItem(productId, action)
        }else{
            console.log('Running else')
            userOrder(productId, action)
        }
    })
}

function addCookieItem(productId, action){
    console.log("Not looged...")

    if(action == 'add'){
        if(cart[productId] == undefined){
            cart[productId] = {'quantity': 1}
        }else{
            cart[productId]['quantity'] += 1
        }
    }

    if(action == 'remove'){
        cart[productId]['quantity'] -= 1

        if(cart[productId]['quantity'] <= 0){
            console.log('Remove item')
            delete cart[productId]
        }
    }

    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}



function userOrder(productId, action){

    let url = "/orders/update_item"

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data :', data )
        location.reload()
    })
}