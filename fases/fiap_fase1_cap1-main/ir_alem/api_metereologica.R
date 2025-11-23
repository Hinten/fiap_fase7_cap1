install.packages(c("openmeteo",
                   "tibblify",
                   "withr",
                   "purrr",
                   "testthat",
                   "dplyr",
                   "tidyr"
), lib= 'ir_alem/lib', repos = "https://cloud.r-project.org/")
library('openmeteo', lib.loc = "ir_alem/lib")
library('tibblify', lib.loc = "ir_alem/lib")
library('withr', lib.loc = "ir_alem/lib")
library('purrr', lib.loc = "ir_alem/lib")
library('testthat', lib.loc = "ir_alem/lib")
library('dplyr', lib.loc = "ir_alem/lib")
library('tidyr', lib.loc = "ir_alem/lib")

#Repo: https://github.com/tpisel/openmeteo

timezone <- 'America/Sao_Paulo'

sair <- function(){

    sair <- tolower(trimws(readline(prompt = "Tem certeza que deseja sair? (s/n)")))

    if (sair == 's'){
        quit(save = "no")
    } else if (sair == 'n'){
        print("voltando ao menu")
    } else {
        print("Opção invalida, voltando ao menu")
    }
}

obter_nome_cidade <- function(){
  cidade <- tolower(trimws(readline(prompt = "Digite o nome da cidade: ")))
  return(cidade)
}

previsao_do_tempo <- function(cidade){
  cidade <- obter_nome_cidade()
  weather <- weather_now(cidade, timezone = timezone)

  #uma tiblle renomeando as colunas
    weather_novo <- tibble(
        data = weather$datetime,
        temperatura = weather$temperature,
    )

  print(weather_novo)
}

previsao_proxima_semana <- function(cidade){
  cidade <- obter_nome_cidade()
  weather <- weather_forecast(cidade,
                   start = Sys.Date() + 1,
                   end = Sys.Date()+ 7,
                   daily = "temperature_2m_max",
                   timezone = timezone)

  #renomear colunas
  weather_novo <- tibble(
      data = weather$date,
      temperatura = weather$daily_temperature_2m_max,
  )

  print(weather_novo)
}

previsao_semana_passada <- function(cidade){
  cidade <- obter_nome_cidade()
  weather <- weather_history(cidade,
                  start = Sys.Date() - 7,
                  end = Sys.Date() - 1,
                  daily = "temperature_2m_max",
                  timezone = timezone)
  #renomear colunas
  weather_novo <- tibble(
      data = weather$date,
      temperatura = weather$daily_temperature_2m_max,
  )

  print(weather_novo)
}

menu_weather <- function(){
  while(TRUE){
    cat(strrep("-", 20), "\n")
    cat(sprintf("%10s\n", "Menu"))
    cat(strrep("-", 20), "\n")
    print("1 - Previsao do tempo de hoje")
    print("2 - Previsao do tempo da proxima semana")
    print("3 - Previsao do tempo da semana passada")
    print("4 - Sair")

    opcao <- trimws(readline(prompt = "Digite a opcao: "))

    switch(opcao,
           '1' = previsao_do_tempo(),
           '2' = previsao_proxima_semana(),
           '3' = previsao_semana_passada(),
           '4' = sair(),
           print('Opcao invalida')
    )
  }
}




if (sys.nframe() == 0) {
  menu_weather()
}