function getIcons() {
    var url = "http://20.201.114.48//icons";

    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", url, false);
    xhttp.send(async=true);

    var icons = JSON.parse(xhttp.responseText)

    // Setando os icons --------------------------------------------
    // Donos dos perfils
    var kaImg = document.getElementById("ka")
    if (kaImg != null) {
        kaImg.src = icons["ka"]
    }

    var duduImg = document.getElementById("dudu")
    if (duduImg != null) {
        duduImg.src = icons["dudu"]
    }

    // Amigos: Ka
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

    var linImg = document.getElementById("lin")
    if (linImg != null) {
        linImg.src = icons["lin"]
    }

    var snayImg = document.getElementById("snay")
    if (snayImg != null) {
        snayImg.src = icons["snay"]
    }

    var kahImg = document.getElementById("kah")
    if (kahImg != null) {
        kahImg.src = icons["kah"]
    }

    // Amigos: Dudu

    var brunoImg = document.getElementById("bruno")
    if (brunoImg != null) {
        brunoImg.src = icons["bruno"]
    }

    var andriImg = document.getElementById("andri")
    if (andriImg != null) {
        andriImg.src = icons["andri"]
    }
}