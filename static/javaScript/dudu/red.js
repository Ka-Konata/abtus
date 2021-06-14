function redFriends() {
    window.location.href = "/d/friends"
}

function copyText() {
    var button = document.getElementById("copiar")
    button.value = "Copiado!"
    navigator.clipboard.writeText("Dudu#9656")
}