// ==UserScript==
// @name         BalticStates template
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Baltic border and hearts
// @author       u/Karolinskis
// @match        https://hot-potato.reddit.com/embed*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=reddit.com
// @grant        none
// ==/UserScript==
function getImage() {
            const i = document.createElement("img");
            i.src = "https://i.imgur.com/1i32rVv.png";
            i.style = "position: absolute; left: 0; top: 0; image-rendering: pixelated; width: 1000px; height: 1000px; ";
            return i;
        }

if (window.top !== window.self) {
    window.addEventListener('load', () => {
            document.getElementsByTagName("mona-lisa-embed")[0].shadowRoot.children[0].getElementsByTagName("mona-lisa-canvas")[0].shadowRoot.children[0].appendChild(getImage());
    }, false);

}

