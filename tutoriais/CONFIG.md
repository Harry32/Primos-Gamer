# Configurando o ambiente:
Aqui vamos ver o que é necessário para configurar o ambiente linux para rodar a aplicação.

## Pasta de projetos
Esse passo é opcional, mas você pode querer separar seus projetos em uma pasta. Para criar uma pasta `mkdir` seguido do nome da pasta desejada. Então se queremos criar uma pasta chamada "projetos" por exemplo, execute o comando `mkdir projetos`. Fique a contade para criar a estrutura de pastas que achar melhor

## Baixando o projeto
Como ainda não temos nada para acessar via Visual Studio Code, vamos executar o comenado de clone. Se você criou a pasta de projetos, entre nela com o comando `cd projetos`. Depois execute o comando `git clone` seguido do link de clonagem do projeto.

Para conseguir o link vá até a página do projeto e clique no botão verde escrito *<> Code* como mostra a imagem abaixo:

![github-1](./imgs/github-1.png "Página principal do github")

Na janelinha flutuante que aparecer, sertifique-se que a aba HTTPS está selecionada e copie o link.

![github-2](./imgs/github-2.png "Janela de informações de Clone")

Depois basta executar o comando `git clone https://<link>` que o código será baixado. Lembre-se que todo código é baixado da branch **main**.


## VENV
Antes de entrarmos nos projeto precisamos configurar a nossa VENV.

VENV ou Virtual Environment é uma ferramenta que permite instalar as bibliotecas do python para apenas um projeto especifico, não vários. Se você instalar um pacote do python sem VENV ele estara disponível na sua máquina como um todo. Isso pode ser um problema quando você tem mais de um projeto, um projeto pode estar usando o Django na versão 5.1.2 e outro na versão 4.3.7. Como você teria apenas uma versão do Django pra todos os projetos um deles não rodaria.

Para resolver isso criamos sempre uma VENV para cada projeto que trabalhamos. Pense nela como uma pasta de biblioteca para seu projeto. Vamos começar criando na pasta atual (fora da pasta do projeto Primos-Gamer) uma pasta apenas para nossas futuras VENVs. Execute o comando `mkdir venvs`.

Agora vamos instalar o venv. No linux o primeiro passo é executar o comando que atualiza a biblioteca de pacotes do sistema. Basta executar o comando `apt-get update`. Após o update podemos fazer a instalação com `apt-get install python3-virtualenv`. Você vai ver que vai ser perguntado se deseja instalar alguns pacotes. Basta digitar a resposta equivalente para permitir (normalmente Y ou YES). Se quiser instalar sem que seja perguntado basta colocar a propriedade **-y** no comando, ficando assim? `apt-get -y install python3-virtualenv`.

Com o pacote agora instalado podemos criar a VENV para o projeto executando o comando `python3 -m venv ./venvs/Primos-Gamer`. Finalmente nós vamos ativar a nossa VENV executando o comando. Podemos ativar a partir da pasta que estamos agora, mas como normalmente será executado de dentro da pasta do projeto vamos fazer isso. Entre na pasta do projeto (executando `cd Primos-Gamer`) e depois execute `source ../venvs/Primos-Gamer/bin/activate`. Você verá que agora no seu terminao há um parentese ao lado esquerdo da linha atual com o nome da VENV ativa *"(Primos-Gamer)"*

## Utilizando o Git
Nesse momento estamos na branch **main**. Mas para trabalhar precisaremos usar nossos próprios branches. Todo branch para desenvolver novas funcionalidades deve partir da branch de desenvolvimento, então vamos precisar priomeiro baixar essa branch.

Lembre-se que existem dois ambientes no git, o ambiente local (que está na sua máquina) e o ambiente remóto ou origin (que está no servidor do github). Ao criar um novo branch é necessário dizer de onde ele surge. Execute o comando `git checkout -b <nome_branch> origin/<branch_remoto>`. Onde <nome_branch> é o nome que o branch local terá. É recomendado que o nome seja o mesmo do branch remoto para evitar confusão. E <branch_remoto> é o nome do branch remóto. Como vamos baixar a develop o código ficará assim: `git checkout -b develop origin/develop`.

## Comandos Utilizados
```
# Atualiza pacotes do linux
apt-get update
```