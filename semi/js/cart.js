$(function () {

    function updateTotal() {
        let total = 0;

        $(".cartItem").each(function () {
            let price = 5000; // 예시 (실제로는 데이터로 가져와야 함)
            let count = $(this).find(".count").val();

            let itemTotal = price * count;
            $(this).find(".totalPrice").text(itemTotal + "원");

            if ($(this).find(".check").is(":checked")) {
                total += itemTotal;
            }
        });

        $("#totalItemPrice").text(total);

        let delivery = total >= 30000 ? 0 : 3000;
        $("#deliveryFee").text(delivery);

        $("#finalPrice").text(total + delivery);
    }

    // 수량 증가
    $(".plus").click(function () {
        let input = $(this).siblings(".count");
        input.val(parseInt(input.val()) + 1);
        updateTotal();
    });

    // 수량 감소
    $(".minus").click(function () {
        let input = $(this).siblings(".count");
        let val = parseInt(input.val());
        if (val > 1) {
            input.val(val - 1);
        }
        updateTotal();
    });

    // 체크 시 금액 계산
    $(".check").change(function () {
        updateTotal();
    });

    // 삭제
    $(".delete").click(function () {
        $(this).closest(".cartItem").remove();
        updateTotal();
    });

    updateTotal();
});