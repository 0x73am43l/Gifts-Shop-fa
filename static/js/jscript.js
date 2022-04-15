/*  lightSlider  */
$(document).ready(function() {
    $('#autoWidth').lightSlider({
        autoWidth: true,
        loop: true,
        onSliderLoad: function () {
            $('#autoWidth').removeClass('cS-hidden');
        }
    });
    $('#autoWidth-2').lightSlider({
        autoWidth: true,
        loop: true,
        onSliderLoad: function () {
            $('#autoWidth-2').removeClass('cS-hidden');
        }
    });
});

/* Select Product */
// $(document).ready(function (){
//     $("input[name$='select_region']").click(function(){
//         var inputValue = $(this).attr("value");
//         var target =$("." + inputValue);
//         $('.prices').not(target).hide();
//         $(target).show();
//     });
//     $("input[name$='select_prices']").click(function(){
//         var inputValue = $(this).attr("value");
//         var target =$("." + inputValue);
//         $('span #price').not(target).hide();
//         $(target).show();
//     });
// });

/*  EnglishToPersian  */
$(function () {
    $('#yourphone').keyup(function (e) {
        var ctrlKey = 67, vKey = 86;
        if (e.keyCode != ctrlKey && e.keyCode != vKey) {
            $('#yourphone').val(persianToEnglish($(this).val()));
        }
    });
});
function persianToEnglish(input) {
    var inputstring = input;
    var persian = ["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"]
    var english = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for (var i = 0; i < 10; i++) {
        inputstring = inputstring.toString().replace(english[i], persian[i]);
    }
    return inputstring;
}

/* Just Allow Number */
$(document).ready(function (){
    $('#yourphone').keypress(function (e) {
    var charCode = (e.which) ? e.which : event.keyCode;
    if (String.fromCharCode(charCode).match(/[^0-9]/g))
        return false;
    });
});

/* Change Profile Pic */
$(document).ready(function() {
    $("#change_pic").hide();
    $(".profile-pic").hover(function() {
        $("#change_pic").show();
        }, function() {
        $("#change_pic").hide();
    });
});

/* SignIn Send SMS Button */
$('#send_otp').on('click', function() {

    if ($(this).hasClass('disabled')) {
        return false;
    } else {
        $(this).addClass('disabled');
    }
});

/* Send OTP With Spinner+Ajax */

jQuery(function ($){
    $('#yourphone').keyup(function (){
        if ($(this).val().length == 10) {
            $(document).ajaxSend(function () {
                $('spinner-grow').fadeIn(500);
                var loading = '<div class="spinner-grow spinner-grow-sm" role="status" style="color: #2a2a2a"></div>&nbsp;&nbsp;در حال ارسال کد...'
                $('#send_otp').html(loading);
             });
           $('#send_otp').click(function (){
               $.ajax({
                   type: 'PUT',
                   headers: {
                        'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()
                        // "X-CSRFToken": '{{csrf_token}}',
                   },
               }).done(function (){
                   setTimeout(function (){
                       $('spinner-grow').fadeOut(500);
                   },700);
               })
           })
        }
    })
})

/* Select Product Item */
$(document).ready(function() {
    $('.region-item').click(function () {
        var i;
        var tabshow = jQuery(this).attr('tabSHow');
        var buyingTab = jQuery(this).attr('buyingtab');
        var x = document.getElementsByClassName("charge");

        for (i = 0; i < x.length; i++) {
            x[i].classList.remove("activetab");
        }
        var region_item = document.getElementsByClassName("region-item");
        for (i = 0; i < region_item.length; i++) {
            region_item[i].classList.remove("active");
        }
        var PriceTab = document.getElementsByClassName("buy-btn");
        for (i = 0; i < PriceTab.length; i++) {
            PriceTab[i].classList.remove("activeBy");
        }
        var BuySections = document.getElementsByClassName("buysections");
        for (i = 0; i < BuySections.length; i++) {
            BuySections[i].classList.remove("activeBuying");
        }
        $('#' + tabshow).addClass('activetab');
        $('#buyingTabnoSelect').addClass('activeBuying');
        $(this).addClass('active');
        $('#buyingTabnoSelect .priceTabcontent:first-child').addClass('activeBy');
    });

    $('.charge-item').click(function () {
        var tabshow = jQuery(this).attr('showpricetab');
        var buyingTab = jQuery(this).attr('buyingtab');
        var i;
        var x = document.getElementsByClassName("buy-btn");
        for (i = 0; i < x.length; i++) {
            x[i].classList.remove("activeBy");
        }
        var M = document.getElementsByClassName("charge-item");
        for (i = 0; i < M.length; i++) {
            M[i].classList.remove("active");
        }
        var BuySections = document.getElementsByClassName("buysections");
        for (i = 0; i < BuySections.length; i++) {
            BuySections[i].classList.remove("activeBuying");
        }
        $('#' + tabshow).addClass('activeBy');
        $('#' + buyingTab).addClass('activeBuying');
        $(this).addClass('active');
    });
});
