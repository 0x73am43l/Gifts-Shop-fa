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
$(document).ready(function (){
    $("input[name$='select_region']").click(function(){
        var inputValue = $(this).attr("value");
        var target =$("." + inputValue);
        $('.prices').not(target).hide();
        $(target).show();
    });
    $("input[name$='select_prices']").click(function(){
        var inputValue = $(this).attr("value");
        var target =$("." + inputValue);
        $('span #price').not(target).hide();
        $(target).show();
    });
});

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