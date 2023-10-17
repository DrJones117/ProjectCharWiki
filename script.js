function buttonChange(element) {
    element.style.backgroundColor = "white";
    element.style.color = "black";
}

function buttonRevert(element) { 
    element.style.backgroundColor = "inherit";
    element.style.color = "white";
}

// ======= Expanding Image ====== //

function exImg(element) {
    element.style.transition = "500ms";
    element.style.height = "200px";
    element.style.width = "200px";
    element.style.position = "relative";
}

function decrMain(element) {
    element.style.transition = "500ms";
    element.style.height = "130px";
    element.style.width = "130px";
    element.style.position = "static";
}

function decrSide(element) {
    element.style.transition = "500ms";
    element.style.height = "100px";
    element.style.width = "100px";
    element.style.position = "static";
}
