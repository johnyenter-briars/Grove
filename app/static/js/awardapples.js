function clearSelection(){
    var radioList = document.getElementsByTagName("input");

    for(radioElement of radioList){
        radioElement.checked = false;
    }
}