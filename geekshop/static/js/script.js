window.onload = function () {
    $(".basket_list").on('click', 'input[type="number"]', function (event) {
        console.log(event);
        var product_id = event.target.name;
        var _value = event.target.value;
        $.ajax({
            url: "/basket/add/" + product_id + "/" + _value + "/ajax/",
            success: function (data) {
                $(".basket_list").html(data.result);
            }
        });
    })
};