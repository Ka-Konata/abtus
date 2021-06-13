function getIcons() {
    var url = "http://127.0.0.1:5000/icons";

    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", url, false);
    xhttp.send(async=true);

    var icons = JSON.parse(xhttp.responseText)

    var kaImg = document.getElementById("ka")
    if (kaImg != null) {
        kaImg.src = icons["ka"]
    }

    var duduImg = document.getElementById("dudu")
    if (duduImg != null) {
        duduImg.src = icons["dudu"]
    }

    var lannaImg = document.getElementById("lanna")
    if (lannaImg != null) {
        lannaImg.src = icons["lanna"]
    }

    var gibsImg = document.getElementById("gibs")
    if (gibsImg != null) {
        gibsImg.src = icons["gibs"]
    }

    var sayuImg = document.getElementById("sayu")
    if (sayuImg != null) {
        sayuImg.src = icons["sayu"]
    }
}