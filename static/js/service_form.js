let sizeInput = document.getElementById('size-input');
let numberInput = document.getElementById('number-input');
let acreInput = document.getElementById('acre-input');
let treeInput = document.getElementById('tree-input');
let weedInput = document.getElementById('weed-input');

let serviceName = document.getElementById('service-name').innerText.toLowerCase();
let serviceNoun = document.getElementsByClassName('service-name');

// Show relevant fields for Grass Cutting
if ( serviceName.includes('grass') ) {
    numberInput.setAttribute('class', 'd-none');
}

// Show relevant fields for Weeding and update based on surface type
if ( serviceName.includes('weed') ) {
    sizeInput.setAttribute('class', 'd-none');
    numberInput.setAttribute('class', 'd-none');
    
    weedInput.addEventListener('change', function () {
        let weedOption = document.getElementById('weedOption');
        console.log("weedOption.value:", weedOption.value);
        if ( weedOption.value == 'Bed/Planter' ) {
            updateServiceName(serviceNoun, "Bed/Planter");
            numberInput.removeAttribute('class', 'd-none');
            sizeInput.removeAttribute('class', 'd-none');

        } else {
            numberInput.setAttribute('class', 'd-none');
            sizeInput.setAttribute('class', 'd-none');
        }
    });
}

// Show relevant fields for Tree Cutting and Pruning
if ( serviceName.includes('tree felling') ) {
    updateServiceName(serviceNoun, "Tree");
}

// Show relevant fields for Hedge Cutting and Flowerbed Care
if ( serviceName.includes('hedge') || serviceName.includes('flower') ) {
    if ( serviceName.includes('hedge') ) {
        updateServiceName(serviceNoun, "Hedge");
    } else {
        updateServiceName(serviceNoun, "Flowerbed");
    }
    numberInput.removeAttribute('class', 'd-none');
}

// Show relevant fields for Tree Stump Removal
if ( serviceName.includes('stump') ) {
    numberInput.removeAttribute('class', 'd-none');
    updateServiceName(serviceNoun, "Stump");
}


// Function that updates the service-name spans with the correct word.
function updateServiceName(serviceNoun, string) {
    for (let i = 0; i < serviceNoun.length; i++) {
        serviceNoun[i].innerText = string;
    }
}

// Apply the correct width to the orange review stars
rating = Number($('#rating').text());
percentage = rating * 20;
$('.fill-ratings').css('width', percentage + "%")