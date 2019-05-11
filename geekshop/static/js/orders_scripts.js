var _quantity, _price, orderitem_num, delta_quantity, orderitem_quantity, delta_cost;
var quantity_arr = [];
var price_arr = [];
var $orderForm, $orderTotalQuantity, $orderTotalCost;
var totalForms, order_total_quantity, order_total_cost;


function orderSummaryUpdate(orderitem_price, delta_quantity) {
    delta_cost = orderitem_price * delta_quantity;

    order_total_cost = Number((order_total_cost + delta_cost).toFixed(2));
    order_total_quantity = order_total_quantity + delta_quantity;

    $('.order_total_cost').html(order_total_cost.toString());
    $('.order_total_quantity').html(order_total_quantity.toString());
}


function deleteOrderItem(row) {
    target_name = row[0].querySelector('input[type="number"]').name;
    orderitem_num = parseInt(target_name.replace('orderitems-', '').replace('-quantity', ''));
    delta_quantity = -quantity_arr[orderitem_num];
    orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
}


window.onload = function () {
    // $orderForm = $('.order_form');
    // $orderTotalQuantity = $('.order_total_quantity');
    // $orderTotalCost = $('.order_total_cost');
    // totalForms = parseInt($('input[name="orderitems-totalForms"]').val());
    //
    // order_total_quantity = parseInt($orderTotalQuantity.text()) || 0;
    // order_total_cost = parseFloat($orderTotalCost.text().replace(',', '.')) || 0;
    //
    // for (i = 0; i < totalForms; i++) {
    //     _quantity = parseInt($('input[name="orderitems-' + i + '-quantity"]').val());
    //     _price = parseFloat($('.orderitems-' + i + '-price').text().replace(',', '.'));
    //     quantity_arr[i] = _quantity;
    //     price_arr[i] = _price || 0;
    // }
    // // console.log(quantity_arr);
    // // console.log(price_arr);
    //
    // if (!order_total_quantity) {
    //     for (i = 0; i < totalForms; i++) {
    //         order_total_quantity += quantity_arr[i];
    //         order_total_cost += quantity_arr[i] * price_arr[i];
    //     }
    //     $orderTotalQuantity.html(order_total_quantity.toString());
    //     $orderTotalCost.html(Number(order_total_cost.toFixed(2)).toString());
    // }
    //
    // $orderForm.on('change', 'input[type="number"]', function (event) {
    //     var target = event.target;
    //     orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-quantity', ''));
    //     if (price_arr[orderitem_num]) {
    //         orderitem_quantity = parseInt(target.value);
    //         delta_quantity = orderitem_quantity - quantity_arr[orderitem_num];
    //         quantity_arr[orderitem_num] = orderitem_quantity;
    //         orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
    //     }
    // });
    //
    // $orderForm.on('click', 'input[type="checkbox"]', function (event) {
    //     var target = event.target;
    //     orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-DELETE', ''));
    //     if (target.checked) {
    //         delta_quantity = -quantity_arr[orderitem_num];
    //     } else {
    //         delta_quantity = quantity_arr[orderitem_num];
    //     }
    //     orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
    // });
    //
    // console.log($('.formset_row'));

    $('.formset_row').formset({
        addText: 'добавить продукт',
        deleteText: 'удалить',
        prefix: 'orderitems',
        removed: deleteOrderItem
    });
};
