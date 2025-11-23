source("objetivo_g/read_file.R")
source("objetivo_g/calcula_media.R")
source("objetivo_g/calcula_desvio.R")
source("objetivo_g/calcula_mediana.R")
source("objetivo_g/calcula_moda.R")

sair <- function (){
    sair <- tolower(trimws(readline(prompt = "Tem certeza que deseja sair? (s/n)")))

    if (sair == 's'){
        quit(save = "no")
    } else if (sair == 'n'){
        print("voltando ao menu")
    } else {
        print("Opção invalida, voltando ao menu")
    }
}

menu <- function(){

  data <- loadData()


  while(TRUE){
    cat(strrep("-", 20), "\n")
    cat(sprintf("%10s\n", "Menu"))
    cat(strrep("-", 20), "\n")
    print("1 - Calcular media")
    print("2 - Calcular mediana")
    print("3 - Calcular moda")
    print("4 - Calcular desvio simples")
    print("5 - Calcular desvio absoluto medio")
    print("6 - Calcular desvio padrao amostral")
    print("7 - Calcular desvio relativo percentual")
    print("8 - Sair")

    opcao <- trimws(readline(prompt = "Digite a opcao: "))

    switch(opcao,
      '1' = calculaMediasFromJson(data),
      '2' = calculaMedianaFromJson(data),
      '3' = calcularModaFromJson(data),
      '4' = desvioSimplesFromJson(data),
      '5' = desvioAbsolutoMedioFromJson(data),
      '6' = desvioPadraoAmostralFromJson(data),
      '7' = desvioRelativoPercentualFromJson(data),
      '8' = sair(),
      print('Opcao invalida')
    )
  }
}

if (sys.nframe() == 0) {
  menu()
}