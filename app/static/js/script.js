console.log("hello there!");
async function deleteFile(fname) {
    var xhr = new XMLHttpRequest();
    var formData = new FormData();
    formData.append("filename", fname);
    console.log(fname);
    xhr.open("POST", "/task/{{taskID}}", true);
    //xhr.setRequestHeader('Content-Type', 'application/json');
    await xhr.send(formData);
    await this.reload();
    return false;
}
function reload(){
    window.location.reload(true);
}