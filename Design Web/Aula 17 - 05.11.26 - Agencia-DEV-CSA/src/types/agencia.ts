export interface projeto{
    id: number,
    nome: string,
    descricao: string,
    status: 'Em Andamento' | 'Concluído'
}
// para cada gerenciamento de estado, é importante fazer uma interface