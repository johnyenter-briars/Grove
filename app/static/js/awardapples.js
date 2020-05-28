function clearSelection(){
    var radioList = document.getElementsByTagName("input");

    for(radioElement of radioList){
        radioElement.checked = false;
    }
}

function checkElements(){
    var $rb = $('input:radio')
    var djangoData = $('#my-data').data().name;
    var count = 0;
    var showAlert = true;
    $('#my_radio_box').submit(function(){
        for (var i = 0; i < $rb.length; i += 1) {
            if ($($rb[i]).is(':checked')) {            
                count++;
            }
        }
        if(count > djangoData && showAlert) {
            showAlert = false;
            alert("You are exceeding your limit. You may only submit " + djangoData);
            return false;
        }

    });
}