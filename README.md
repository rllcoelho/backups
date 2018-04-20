# Desafio

Desafio: O comando rsync pode ser utilizado para fazer backup de arquivos, principalmente quando combinado com a opção "--suffix", que armazena uma cópia do arquivo modificado porém com um nome sufixado pelo argumento do parâmetro. Por exemplo, suponha uma pasta com o seguinte conteúdo:

/home/joaozinho/
├── ArquivosDCC
│   ├── historico.pdf
│   ├── MATC99
│   │   └── trabalho-final.c
│   └── MATE88
│       └── resultados_1a_prova.pdf
└── Resultado Seleção STI.eml

Joãozinho executa o backup dos seus arquivos todo dia às 21hs com o comando rsync -apr --suffix="-bkp-$(date +%s)" /home/ /media/backup/. Enquanto estava fazendo o trabalho da disciplina MATC99, como estava alterando o trabalho todos os dias, percebeu que sua rotina de backup armazena muitas cópias do arquivo, como pode ser visto abaixo:

/media/backup/joaozinho/
├── ArquivosDCC
│   ├── historico.pdf
│   ├── MATC99
│   │   ├── trabalho-final.c
│   │   ├── trabalho-final.c-bkp-1523662200
│   │   ├── trabalho-final.c-bkp-1523722680
│   │   ├── trabalho-final.c-bkp-1523873324
│   │   ├── trabalho-final.c-bkp-1523913424
│   │   └── trabalho-final.c-bkp-1523926363
│   └── MATE88
│       └── resultados_1a_prova.pdf
└── Resultado Seleção STI.eml

Sua missão é desenvolver um programa, em qualquer linguagem de programação, para armazenar apenas os últimos 2 backups (além do arquivo original), ou seja, os dois backups mais recentes. No caso acima, a pasta deveria ficar:

/media/backup/joaozinho/
├── ArquivosDCC
│   ├── historico.pdf
│   ├── MATC99
│   │   ├── trabalho-final.c
│   │   ├── trabalho-final.c-bkp-1523913424
│   │   └── trabalho-final.c-bkp-1523926363
│   └── MATE88
│       └── resultados_1a_prova.pdf
└── Resultado Seleção STI.eml

O seu programa será executado logo após a execução do rsync!

# Solução
