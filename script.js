// ====== Nav-buttons ====== //

function buttonChange(element) {
    element.style.backgroundColor = "white";
    element.style.color = "black";
}

function buttonRevert(element) { 
    element.style.backgroundColor = "inherit";
    element.style.color = "white";
}

// ====== Images====== //

function exImg(element) {
    element.style.transition = "500ms";
    element.style.height = "200px";
    element.style.width = "200px";
    element.style.position = "relative";
    element.style.filter = "drop-shadow(10px 10px 10px black)";
}

function decrMain(element) {
    element.style.transition = "500ms";
    element.style.height = "130px";
    element.style.width = "130px";
    element.style.position = "static";
    element.style.filter = "drop-shadow(0px 0px 0px black)";
}

function decrSide(element) {
    element.style.transition = "500ms";
    element.style.height = "100px";
    element.style.width = "100px";
    element.style.position = "static";
    element.style.filter = "drop-shadow(0px 0px 0px black)";
}

// ====== Quote Card ====== //

// quote 1

function quoteCardEnter1() {
    var qCard = document.getElementById("quoteCard1");
    qCard.style.opacity = "1";
}

function quoteCardLeave1() {
    var qCard = document.getElementById("quoteCard1");
    qCard.style.opacity = "0";
}

// quote 2

function quoteCardEnter2() {
    var qCard = document.getElementById("quoteCard2");
    qCard.style.opacity = "1";
}

function quoteCardLeave2() {
    var qCard = document.getElementById("quoteCard2");
    qCard.style.opacity = "0";
}

// quote 3

function quoteCardEnter3() {
    var qCard = document.getElementById("quoteCard3");
    qCard.style.opacity = "1";
}

function quoteCardLeave3() {
    var qCard = document.getElementById("quoteCard3");
    qCard.style.opacity = "0";
}


