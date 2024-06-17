let updateBtn = document.getElementsByClassName('update-cart');
let addToCartClicked = '';


for(let i = 0; i < updateBtn.length; i++){
    updateBtn[i].addEventListener('click', function(){
        let productId = this.dataset.product;
        let action = this.dataset.action;
        let variantType = this.dataset.varianttype;
        let variantId = '';
        let sizeId = '';
        if (this.dataset.buttonclicked !== undefined){
            addToCartClicked = this.dataset.buttonclicked;
            console.log('I was clicked man')
        };



        if(variantType == 'Size-Color' || variantType == 'Color'){
            variantId = document.getElementById("variantid").value
        }else{
            variantId = document.getElementById("variantid").value
            sizeId = document.getElementById("size").value
            console.log(variantId)

        }

        if(user === 'AnonymousUser'){
            addCookieItem(productId, action)
        }else{
            console.log('Running else')
            userOrder(productId, action, variantId, sizeId)
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


function userOrder(productId, action, variantId, sizeId){

    let url_path = "/orders/update_item"

    $.ajax({
        url: url_path,
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrftoken,
        },        
        data: JSON.stringify({'productId': productId, 'action': action, 'variantId': variantId, 'sizeId': sizeId}),
        success: function(data) {
            var received_data = JSON.parse(data);
            $('ajaxrefresh').html(data.render_ajax);
            // $('#appendHere').html(data.rendered_table);
            var itemId = '#updateText' + productId
            var totalId = '#updateTotal' + productId
            var grandTotalId = '#updateGrandTotal'
            var cartTotalId = '#updateCartTotal'
            var qnty = received_data.quantity

            if (qnty <= 0) {
                location.reload()
            } else {
                $(itemId).text(received_data.quantity);
                $(totalId).text(received_data.itemTotal);
                $(grandTotalId).text(received_data.grandTotal);
                $(cartTotalId).text(received_data.cartTotal);



                if(addToCartClicked == "yes"){
                    ajaxUpdate()
                    console.log('Running function')
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
            url: "/orders/canvascontent", // Your URL to fetch new content
            type: 'GET',
            success: function(data) {
                console.log("Yes its working")
                $('#ajaxrefresh').html(data.render_ajax); // Update the offcanvas content
                console.log(data.render_ajax)
            },
            error: function(error) {
                console.log('Error fetching new content:', error);
            }
        });
}