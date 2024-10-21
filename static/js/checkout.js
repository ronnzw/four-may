// hide button by default
document.addEventListener('DOMContentLoaded', function() {
    let itemHidden = document.getElementById('loadPaynow');
    let shopField = document.getElementById('div_id_store');
    shopField.classList.add('d-none');

    if (itemHidden.classList.contains('d-block')) {
        itemHidden.classList.replace('d-block', 'd-none');
    }

});

// Show button when clicked
document.getElementById('paynowButton').addEventListener('click', function(){
    let itemHidden = document.getElementById('loadPaynow')
    let buttonDisabled = document.getElementById('paynowButton');
    if (itemHidden.classList.contains('d-none')) {
        itemHidden.classList.replace('d-none', 'd-block');
        buttonDisabled.classList.add('disabled')

    }

});

let deliveryMethodField = document.getElementById('id_pickup_instore');

deliveryMethodField.addEventListener('change', function(){
    console.log('It running')
    let shopField = document.getElementById('div_id_store');
    let storePickUp = document.getElementById('id_pickup_instore').checked;
    let pickupButton = document.getElementById('pickupButton');
    let addressSection = document.getElementById('addressSection');

    if (storePickUp) {
        console.log(storePickUp)
        shopField.classList.remove('d-none');
        shopField.classList.add('d-block');
        pickupButton.classList.remove('d-none');
        pickupButton.classList.add('d-block');
        addressSection.classList.remove('d-block');
        addressSection.classList.add('d-none');
        //shopField.classList.replace('d-none', );
    } else {
        shopField.classList.remove('d-block');
        shopField.classList.add('d-none');
        pickupButton.classList.remove('d-block');
        pickupButton.classList.add('d-none');
        addressSection.classList.remove('d-none');
        addressSection.classList.add('d-block');            
        //shopField.classList.replace('d-block', 'd-none');
    }
})



