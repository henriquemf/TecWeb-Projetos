function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }
});

// Função para abertura da tela de Edição da nota. Código retirado de: https://github.com/bert799/TechWeb-Projeto1A

var postItCard = "post-it-"
var postItCardUpdate = "general-up-"

function editScreen(id) {
  document.getElementById(postItCard.concat(String(id))).style.display = "none"
  document.getElementById(postItCardUpdate.concat(String(id))).style.display = "flex"
}

function outEditScreen(id) {
  document.getElementById(postItCard.concat(String(id))).style.display = "flex"
  document.getElementById(postItCardUpdate.concat(String(id))).style.display = "none"
}