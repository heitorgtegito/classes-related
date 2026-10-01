
const {createApp, ref, watch} = Vue
/* o método watch foi adicionado para ser usado no localstorage */

const lancheifrn = createApp({
    setup(){
        // a variável teve que ficar dentro do setup porque ela precisava mudar os valores
        //isto é, ser dinâmica, não apenas acessar seus dados, mas também alterar os dados.
        
        const lancheifrnLS = localStorage.getItem("lanches");
        //criou uma variável que representa a TABELA do banco de dados do navegador da nossa aplicação

        const fruta_lista = localStorage.getItem("frutas")

        //o array de objetos precisa ficar dentro do setup para mudar os valores das propriedades
        const lanches = ref(
            lancheifrnLS ? JSON.parse(lancheifrnLS):
            //caso não tenham dados, serão adicionados
            //condição ? se SIM : se NÃO

            [
            //lista de objetos
            {
                descricao: 'Bolo',
                ativo: false,
                imagem: 'bolo.jpg',
            },
            {
                descricao: 'Bolacha',
                ativo: false,
                imagem: 'bolacha.jpg',
            },
            {
                descricao: 'Tapioca',
                ativo: false,
                imagem: 'tapioca.jpg',
            }
            ]
        )
        const frutas = ref(
            fruta_lista ? JSON.parse(fruta_lista):
            //caso não tenham dados, serão adicionados
            //condição ? se SIM : se NÃO

            [
            //lista de objetos
            {
                descricao: 'Goiaba',
                ativo: false,
                imagem: 'goiaba.jpg',
            },
            {
                descricao: 'Tangerina',
                ativo: false,
                imagem: 'tangerina.jpg',
            },
            {
                descricao: 'Melancia',
                ativo: false,
                imagem: 'melancia.jpg',
            }
            ]
        )


        watch(lanches, () => {
            localStorage.setItem('lanches', JSON.stringify(lanches.value))
        }, {deep: true, immediate: true})
        watch(frutas, () => {
            localStorage.setItem('frutas', JSON.stringify(frutas.value))
        }, {deep: true, immediate: true})
        //função watch - observa a lista: qualquer alteração é feita lá no localstorage
        //stringify esse método é usado porque o localstorage só recebe string, ele converte objeto para string
        //deep: true - profundo... significa que observa até os valores das propriedades do objeto
        //se houver alteração no valor, por exemplo do 'ativo', este é atualizado no localstorage
        //immediate: true - coloca os valores, os objetos, na tabela do localstorage imediatamente ao abrir a aplicação

        
        function mudarAtivo(item){
            lanches.value.forEach(lanche => {
                lanche.ativo = false
            })
            item.ativo = !item.ativo
        }

        const novoLancheInput = ref('');
        function novoLanche(){
            lanches.value.push({
                descricao: novoLancheInput.value,
                ativo: false,
                imagem: 'bolo.jpg'
            })
        }

        const novaFrutaInput = ref('');
        function novaFruta(){
            frutas.value.push({
                descricao: novaFrutaInput.value,
                ativo: false,
                imagem: 'banana.jpg'
            })
        }
        
        function remover_lanche(){
            frutas.pop()
        }

        return{
            mensagem: ref("Olá, Mundo!!"), //é o getElementById            
            lanches,
            mudarAtivo,
            novoLancheInput,
            novoLanche,
            remover,
            frutas,
            novaFrutaInput,
            novaFruta,
        }

    }
})
lancheifrn.component('app-header', AppHeader); //CHAMAR O ARQUIVO JS DO HEADER
lancheifrn.component('app-footer', AppFooter); //CHAMAR O ARQUIVO JS DO HEADER
lancheifrn.mount('#app');

/* 
PARA DEFINIR O LOCALSTORAGE:
LOCAL STORAGE É um banco de dados que fica dentro do navegador

passo1: colocar o watch na criação do vue
passo2: definir a variável de tabela do banco de dados - nome da tabela criada "lanche"
passo3: condicional para criação da tabela
passo4: observar (watch - assistir)
    atualiza a lista na tabela do local storage assim que a mesma é alterada
    isto é, mudou a propriedade 'ativo', então observa e altera também lá na tabela
    adicionou um novo projeto, altera na tabela do local storage
*/

/*
ATIVIDADE

- criar uma lista para frutas
- adicionar frutas no adm
- excluir lanches - usar a função pop(...)
- excluir frutas
- editar lanche
    - vou colocar a descrição lá no formulário
    - reaproveitar a função novoLanche
*/