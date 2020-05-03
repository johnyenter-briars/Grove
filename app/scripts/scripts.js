function deleteFile(fname) {
    var xhr = new XMLHttpRequest();
    var formData = new FormData();
    formData.append("filename", fname)
    xhr.open("POST", "/task/", true);
    //xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(formData);
}