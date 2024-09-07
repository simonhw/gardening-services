function handleEnableDisable(itemId) {
    let currentValue = parseInt($(`#id_number_${itemId}`).val());
    // console.log('currentValue is', currentValue);
    let minusDisabled = currentValue < 2;
    let plusDisabled = currentValue > 98;
    $(`#decrement-number_${itemId}`).prop('disabled', minusDisabled);
    $(`#increment-number_${itemId}`).prop('disabled', plusDisabled);
}

let allNumberInputs = $('.number_input');
for (let i = 0; i < allNumberInputs.length; i++) {
    let itemId = $(allNumberInputs[i]).data('item_id');
    handleEnableDisable(itemId);
}

$('.number_input').change(function(){
    let itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

// Increment quantity
$('.increment-number').click(function(e) {
    e.preventDefault();
    let closestInput = $(this).closest('.input-group').find('.number_input')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);
    let itemId = $(this).data('item_id');
    console.log('itemId is', itemId);
    handleEnableDisable(itemId);
});

// Decrement quantity
$('.decrement-number').click(function(e) {
    e.preventDefault();
    let closestInput = $(this).closest('.input-group').find('.number_input')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
    let itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});