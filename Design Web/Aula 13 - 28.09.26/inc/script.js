const {createApp, ref} = Vue

const lancheifrn = createApp({
    setup(){

        // a variável teve que ficar dentro do setup porque ela precisava mudar os valores
        //isto é, ser dinâmica, não apenas acessar seus dados, mas também alterar os dados.
        
        const lanches = ref([
            // lista de objetos 
            {
                descricao: 'Bolo',
                ativo: false,
                imagem: 'bolo.jpg'
            },
            {
                descricao: 'Bolacha',
                ativo: false,
                imagem: 'bolacha.jpg'
            },
            {
                descricao: 'Tapioca',
                ativo: false,
                imagem: 'tapioca.jpg'
            }
        ])

        function mudarAtivo(item){
            lanches.value.forEach(lanche => {
                lanche.ativo = false
            }) // vou colocar false em todos
            item.ativo = !item.ativo
        }

        const novoLancheInput = ref('')
        function novoLanche(){
            lanches.value.push({
                descricao: novoLancheInput.value,
                ativo: false,
                imagem: 'bolo.jpg'
            })
            
        }

        return{
            mensagem: ref("Olá, Mundo!!"), //é o getElementById            
            lanches,
            mudarAtivo,
            novoLancheInput,
            novoLanche
        }
    }
})
lancheifrn.component('app-header', AppHeader); //CHAMAR O ARQUIVO JS DO HEADER
lancheifrn.component('app-footer', AppFooter); //CHAMAR O ARQUIVO JS DO HEADER
lancheifrn.mount('#app');
