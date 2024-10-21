let updateBtn = document.getElementsByClassName('update-cart');
let addToCartClicked = '';


for(let i = 0; i < updateBtn.length; i++){
    updateBtn[i].addEventListener('click', function(){
        let productId = this.dataset.product;
        let action = this.dataset.action;
        let variantId = this.dataset.variantid;

        if (this.dataset.buttonclicked !== undefined){
            addToCartClicked = this.dataset.buttonclicked;
        };

        if(user === 'AnonymousUser'){
            addCookieItem(productId, action)
        }else{
            userOrder(productId, action, variantId)
        }
    })
}


function addCookieItem(productId, action){

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


function userOrder(productId, action, variantId){

    let url_path = "/orders/update_item"

    $.ajax({
        url: url_path,
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrftoken,
        },        
        data: JSON.stringify({'productId': productId, 'action': action, 'variantId': variantId}),
        success: function(data) {
            var received_data = JSON.parse(data);
            var itemId = '#' + variantId + 'updateText' + productId
            var totalId = '#' + variantId + 'updateTotal' + productId
            var grandTotalId = '#updateGrandTotal'
            var cartTotalId = '#updateCartTotal'
            var qnty = received_data.quantity

            if (qnty <= 0) {
                location.reload()
            } else {
                $(itemId).text(received_data.quantity);
                $(totalId).html(received_data.price_with_currency);
                $(grandTotalId).html(received_data.grand_total_with_currency);
                $(cartTotalId).text(received_data.cartTotal);

                if(addToCartClicked == "yes"){
                    ajaxUpdate()
                }
            }
        },
        error: function() {
            console.error('There has been a problem with your AJAX operation:');
        }
    });
};

function ajaxUpdate(){
        $.ajax({
            url: "/orders/canvascontent", // Your URL to fetch new context
            type: 'GET',
            success: function(data) {
                var newData = JSON.parse(data);
                // Update the offcanvas content
                $('#ajaxrefresh').html(newData.ajax_render);
                if(newData !== undefined){
                    $('#cart-not-empty').removeClass('d-none');
                    $('#cart-not-empty').addClass('d-block');
                    $('#cart-is-empty').addClass('d-none');
                    // document.getElementById('cart-not-empty').style.display = 'block';
                    //document.getElementById('cart-is-empty').style.display = 'none';
                } else {
                    $('#cart-is-empty').addClass('d-block');
                    $('#cart-not-empty').addClass('d-none');
                    //document.getElementById('cart-not-empty').style.display = 'none';
                    //document.getElementById('cart-is-empty').style.display = 'block';
                }
            },
            error: function(error) {
                console.log('Error fetching new content:', error);
            }
        });
}