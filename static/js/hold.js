
document.addEventListener('DOMContentLoaded', function() {
    let sizeValue = null;
    let colorValue = null;

    function handleDropdownItemClick(event, valueVariable, displayElementId, productIdData, productNameData) {
        event.preventDefault();
        const valueId = event.target.getAttribute(productIdData);
        const valueName = event.target.getAttribute(productNameData);

        // Update the selected value variable
        valueVariable = valueId;

        // Display the selected value in the corresponding <p> tag
        document.getElementById(displayElementId).textContent = 'Selected: ' + valueName;

        // Enable the add-to-cart button if both size and color are selected
        return {'valueId': valueId , 'valueName': valueName}

    }

    document.querySelectorAll('.size-dropdown').forEach(function(item) {
        item.addEventListener('click', function(event) {
            event.preventDefault();

            handleDropdownItemClick(event, sizeValue, 'selected-size', 'data-size', 'data-size-name' )

            document.getElementById('add-to-cart').addEventListener('click', function() {
                const productUrl = this.getAttribute('data-product-url');
                //window.location.href = productUrl;  // Navigate to the home page
 
            });
        });
    });
  
    document.querySelectorAll('.color-dropdown').forEach(function(item) {
        item.addEventListener('click', function(event) {
            event.preventDefault();

            handleDropdownItemClick(event, colorValue, 'selected-color', 'data-color', 'data-color-name' )

            document.getElementById('add-to-cart').addEventListener('click', function() {
                const productUrl = this.getAttribute('data-product-url');
                //window.location.href = productUrl;  // Navigate to the home page
            });
        });
    });
    console.log(sizeValue)
    console.log(colorValue)
    console.log(sizeValue && colorValue)

    if (sizeValue && colorValue) {
        document.getElementById('add-to-cart').disabled = false;
    }
});