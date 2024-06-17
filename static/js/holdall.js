let redButtonClicked = false;
let blueButtonClicked = false;



let sizeElements = document.getElementsByClassName('size-dropdown')
let colorElements = document.getElementsByClassName('color-dropdown')
function getDataAttributes(dropdownElements,par_id){
    let attribute_id = null;
    for(let i = 0; i < dropdownElements.length; i++){
        dropdownElements[i].addEventListener('click', function(){
            let name = this.dataset.name;
            attribute_id = this.dataset.id;
            document.getElementById(par_id).textContent = 'Selected: ' + name;
        })
    }
    return attribute_id
}

document.getElementById('gs').addEventListener('click', function() {
    redButtonClicked = true;
    hidBtn(redButtonClicked, blueButtonClicked)


});

document.getElementById('gos').addEventListener('click', function() {
    blueButtonClicked = true;
    hidBtn(redButtonClicked, blueButtonClicked)

});

getDataAttributes(sizeElements, 'selected-size');
getDataAttributes(colorElements, 'selected-color');

function hidBtn(sizeBtn, colorBtn){
    if (sizeBtn && colorBtn) {
        document.getElementById('add-to-cart').disabled = false;
    }
}


//Navbar js
let currentLocation = location.href;
let navBarItem = document.getElementsByClassName('nav-link');
console.log(navBarItem)

for(let i = 0; i < navBarItem.length; i++){
    if(navBarItem[i].href == currentLocation){
        navBarItem[i].className = 'active'
    }
    
}



let updateBtn = document.getElementsByClassName('update-cart')

for(let i = 0; i < updateBtn.length; i++){
    updateBtn[i].addEventListener('click', function(){
        console.log("The thing is running")
        let productId = this.dataset.product
        let action = this.dataset.action
        let size = sizeValue
        console.log(productId)
        console.log(action)
        console.log(size)

        if(user === 'AnonymousUser'){
            addCookieItem(productId, action)
        }else{
            console.log('Running else')
            userOrder(productId, action, size)
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



function userOrder(productId, action, size){
    console.log('User is logged in, sending data...')

    let url = '/orders/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action, 'size': size})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data :', data )
        //location.reload()
    })
}


