let x = 0;
const title = []
const nick = 'dudu <3'

for (let i = 1; i <= nick.length; ++i) {
//   if (nick.slice(0, -i).endsWith(" ")) continue
  title.push(nick.slice(0, i))
}
for (let i = 1; i < nick.length; ++i) {
// if (nick.slice(0, -i).endsWith(" ")) continue
  title.push(nick.slice(0, -i))
}
title.push('&lrm;')

function titleLoop() {
    document.getElementsByTagName('title')[0].innerHTML = title[x++ % title.length];
    setTimeout(() => titleLoop(), 250)
}