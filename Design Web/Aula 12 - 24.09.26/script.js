const {createApp, ref} = Vue;
// Criação do objeto Vue e chamada dos métodos 
const lanches = ['Pão com Queijo', 'Tapioca', 'Cuscuz com Ovo', 'Bolo', 'Bolacha']
// Variável de lista

const app = createApp({
    // Crio uma nova aplicação de vue
    setup(){
        // onde se declara dados e funções
        return {
            mensagem: ref("Olá, Mundo!"),
            lanches
            // variável reativa do vue (no lugar de usar getelementbyid)
        }
    }
})
app.component("app-header", AppHeader)
app.component("app-footer", AppFooter)
app.mount("#app")
// Aqui a aplicação é incluída na marcação que tem o id "app"
