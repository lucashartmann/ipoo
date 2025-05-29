Ferrovia:

- Trem
    - Locomotiva
    - Vagão
    - Desa

- Locomotiva
    - 

- Vagão
    - Capacidade

Vagão engata em uma Locomotiva
Vagão engata em outro vagão

Vagão pode ser desengatado. Porém, caso ele não seja o último vagão, quando ele for desengatado, ele vai estar desengatando (removendo) os vagões engatados nele da locomotiva

Não se pode engatar o vagão em mais de uma locomotiva
O trem pode possuir mais uma locomotiva


### Falta:

- Poder adicionar uma lista de vagões e locomotivas ao trem
- Resolver ID. Se fizer uma única garagem para cada veiculo, o método get_veiculo_por_id passa a ser um problema. Porque se eu criar uma locomotiva, ela vai ter id = 1, se eu criar um vagão, ele vai ter id = 1. Entao eu terei na garagem dois veiculos com id = 1. 
    - Forma de resolver: Eu tenho que somar 1 ao ID deles no momento que estou adicionando na garagem