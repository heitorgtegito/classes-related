const fotos = document.querySelectorAll(".slide");
const proximo = document.querySelector(".proximo");
const anterior = document.querySelector(".anterior");
const botao_menu = document.querySelector('#menu')
const navegacao = document.querySelector('.nav')

let index = 0;

function mostrarSlide(i) {
  fotos.forEach(slide => slide.classList.remove("ativo"));
  fotos[i].classList.add("ativo");
}

proximo.addEventListener("click", () => {
  index = (index + 1) % fotos.length; 
  mostrarSlide(index);
});

anterior.addEventListener("click", () => {
  index = (index - 1 + fotos.length) % fotos.length;
  mostrarSlide(index);
});

botao_menu.addEventListener('click', () => {
  navegacao.classList.toggle('aparecer')
}) 
