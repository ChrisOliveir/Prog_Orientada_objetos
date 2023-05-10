# Data Science 

## Orientação a Objeto x Programação estruturada

Tudo em python é um Objeto

 - String é objeto
 - Lista é objeto
 - Dicionarios são objetos

Exemplo: Pense no controle remoto de uma TV
 - Control é um objeto
 - cada botão dele é um comando (um método)
 - cada metodo faz uma ação específica 
 - Por tras de cada método podem acontecer milhares de coisas quando vc aperta um botão.


## Orientação a Objetos (POO)

- CLASSES 
  - Class TV():

    cor = 'preta' --> atributos

    tamanho = 55

    canal = 10

    volume = 50

       def mudar_canal(self): --> método (função que faz parte de uma classe)

       def ligar_desligar(self) --> método (função que faz parte de uma classe)

- VANTAGEM POO:

  - Aproveita o código sem precisar refazer/copiar tudo
  - Encapsulamento -> Proteção a mudanças indesejadas ( Ex: TV- não podemos desligaree a tv no botão de mudar o volume)
  - Herança -> Quando definimos uma váriavel sendo uma instancia daquele objeto podemos usar todos métodos e atributos que vem dessa classe.
     
     ex: nome = 'Cristiane'
         nome.capitalize() --> recebe por herança métodos e atributos da classe string (nome)
  - Poliformismo -> Um mesmo método pode ter várias formas em diferentes classes(ou subclasses) ex Animais --> Gatos x Cachorro


## Programação Estruturada 
variavel = 10

lista =[1,2,3,4,5]

for item in lista:

  if ....
         

