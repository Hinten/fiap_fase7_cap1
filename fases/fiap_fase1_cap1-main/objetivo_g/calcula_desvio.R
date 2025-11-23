source("objetivo_g/utils.R")
source("objetivo_g/calcula_media.R")
source("objetivo_g/preparar_dados.R")

desvioSimples <- function (vetor, verbose = TRUE){
  media <- calculaMedia(vetor, verbose = FALSE)

  desvio_simples <- vetor - media

  if (verbose) {
    #todo formatar
    print(paste('O desvio simples: ', paste(desvio_simples, collapse = ', ')))

  }
  return(desvio_simples)

}

desvioSimplesFromJson <- function (json){

  cultura_1 <- getDadosCultura1(json)

  print(paste("Calculando o desvio simples da area de plantio de", CULTURA_1))

  desvio_simples <- desvioSimples(cultura_1$area, verbose = FALSE)

  print(paste("O desvio simples da area de plantio de", CULTURA_1, ":", desvio_simples))

  desvio_fosforo <- desvioSimples(cultura_1$fosforo, verbose = FALSE)

  print(paste("O desvio simples do fosforo de", CULTURA_1, ":", desvio_fosforo))

  desvio_potassio <- desvioSimples(cultura_1$potassio, verbose = FALSE)

  print(paste("O desvio simples do potassio de", CULTURA_1, ":", desvio_potassio))

  print(paste("Calculando o desvio simples da area de plantio de", CULTURA_2))

  cultura_2 <- getDadosCultura2(json)

  desvio_simples2 <- desvioSimples(cultura_2$area, verbose = FALSE)

  print(paste("O desvio simples da area de plantio de", CULTURA_2, ":", desvio_simples2))

  desvio_fosforo2 <- desvioSimples(cultura_2$fosforo, verbose = FALSE)

  print(paste("O desvio simples do fosforo de", CULTURA_2, ":", desvio_fosforo2))

  desvio_potassio2 <- desvioSimples(cultura_2$potassio, verbose = FALSE)

  print(paste("O desvio simples do potassio de", CULTURA_2, ":", desvio_potassio2))


}

desvioAbsolutoMedio <- function (vetor, verbose = TRUE){
  desvios <- desvioSimples(vetor, FALSE)

  absoluto_medio <- mean(abs(desvios))

  if (verbose){
    #todo formatar
    print(paste('O desvio absoluto medio:', paste(absoluto_medio, collapse = ', ')))
  }

  return(absoluto_medio)

}

desvioAbsolutoMedioFromJson <- function (json){

  cultura_1 <- getDadosCultura1(json)

  print(paste("Calculando o desvio absoluto medio da area de plantio de", CULTURA_1))

  dam <- desvioAbsolutoMedio(cultura_1$area, verbose = FALSE)

  print(paste("O desvio absoluto medio da area de plantio de", CULTURA_1, ":", dam))

  dam_fosforo <- desvioAbsolutoMedio(cultura_1$fosforo, verbose = FALSE)

  print(paste("O desvio absoluto medio do fosforo de", CULTURA_1, ":", dam_fosforo))

  dam_potassio <- desvioAbsolutoMedio(cultura_1$potassio, verbose = FALSE)

  print(paste("O desvio absoluto medio do potassio de", CULTURA_1, ":", dam_potassio))

  print(paste("Calculando o desvio absoluto medio da area de plantio de", CULTURA_2))

  cultura_2 <- getDadosCultura2(json)

  dam2 <- desvioAbsolutoMedio(cultura_2$area, verbose = FALSE)

  print(paste("O desvio absoluto medio da area de plantio de", CULTURA_2, ":", dam2))

  dam_fosforo2 <- desvioAbsolutoMedio(cultura_2$fosforo, verbose = FALSE)

  print(paste("O desvio absoluto medio do fosforo de", CULTURA_2, ":", dam_fosforo2))

  dam_potassio2 <- desvioAbsolutoMedio(cultura_2$potassio, verbose = FALSE)

  print(paste("O desvio absoluto medio do potassio de", CULTURA_2, ":", dam_potassio2))

}

desvioPadraoAmostral <- function (vetor, verbose = TRUE){

  assertVetorNumerio(vetor)

  desvio_padrao <- sd(vetor)

  print(desvio_padrao)

  if (verbose){
    #todo formatar
    print(paste('O desvio padrão:', desvio_padrao))
  }

  return(desvio_padrao)

}

desvioPadraoAmostralFromJson <- function (json){

  cultura_1 <- getDadosCultura1(json)

  print(paste("Calculando o desvio padrão amostral da area de plantio de", CULTURA_1))

  desvio_padrao <- desvioPadraoAmostral(cultura_1$area, verbose = FALSE)

  print(paste("O desvio padrão amostral da area de plantio de", CULTURA_1, ":", desvio_padrao))

  desvio_fosforo <- desvioPadraoAmostral(cultura_1$fosforo, verbose = FALSE)

  print(paste("O desvio padrão amostral do fosforo de", CULTURA_1, ":", desvio_fosforo))

  desvio_potassio <- desvioPadraoAmostral(cultura_1$potassio, verbose = FALSE)

  print(paste("O desvio padrão amostral do potassio de", CULTURA_1, ":", desvio_potassio))

  print(paste("Calculando o desvio padrão amostral da area de plantio de", CULTURA_2))

  cultura_2 <- getDadosCultura2(json)

  desvio_padrao2 <- desvioPadraoAmostral(cultura_2$area, verbose = FALSE)

  print(paste("O desvio padrão amostral da area de plantio de", CULTURA_2, ":", desvio_padrao2))

  desvio_fosforo2 <- desvioPadraoAmostral(cultura_2$fosforo, verbose = FALSE)

  print(paste("O desvio padrão amostral do fosforo de", CULTURA_2, ":", desvio_fosforo2))

  desvio_potassio2 <- desvioPadraoAmostral(cultura_2$potassio, verbose = FALSE)

  print(paste("O desvio padrão amostral do potassio de", CULTURA_2, ":", desvio_potassio2))

}

desvioRelativoPercentual <- function (vetor, verbose = TRUE){

  dam <- desvioAbsolutoMedio(vetor, verbose = FALSE)
  media <- calculaMedia(vetor, verbose = FALSE)

  desvio_relativo <- (dam / media) * 100

  if (verbose){
    #todo formatar percentual
    print(paste("O desvio relativo percentual: ", desvio_relativo))
  }

  return(desvio_relativo)

}

desvioRelativoPercentualFromJson <- function (json){

  cultura_1 <- getDadosCultura1(json)

  print(paste("Calculando o desvio relativo percentual da area de plantio de", CULTURA_1))

  desvio_relativo <- desvioRelativoPercentual(cultura_1$area, verbose = FALSE)

  print(paste("O desvio relativo percentual da area de plantio de", CULTURA_1, ":", desvio_relativo))

  desvio_fosforo <- desvioRelativoPercentual(cultura_1$fosforo, verbose = FALSE)

  print(paste("O desvio relativo percentual do fosforo de", CULTURA_1, ":", desvio_fosforo))

  desvio_potassio <- desvioRelativoPercentual(cultura_1$potassio, verbose = FALSE)

  print(paste("O desvio relativo percentual do potassio de", CULTURA_1, ":", desvio_potassio))

  print(paste("Calculando o desvio relativo percentual da area de plantio de", CULTURA_2))

  cultura_2 <- getDadosCultura2(json)

  desvio_relativo2 <- desvioRelativoPercentual(cultura_2$area, verbose = FALSE)

  print(paste("O desvio relativo percentual da area de plantio de", CULTURA_2, ":", desvio_relativo2))

  desvio_fosforo2 <- desvioRelativoPercentual(cultura_2$fosforo, verbose = FALSE)

  print(paste("O desvio relativo percentual do fosforo de", CULTURA_2, ":", desvio_fosforo2))

  desvio_potassio2 <- desvioRelativoPercentual(cultura_2$potassio, verbose = FALSE)

  print(paste("O desvio relativo percentual do potassio de", CULTURA_2, ":", desvio_potassio2))

}


#executa somente se este for o arquivo principal
if (sys.nframe() == 0) {

  x <- c(1, 5, 4.3)

  print(desvioSimples(x))
  print(desvioAbsolutoMedio(x))
  print(desvioPadraoAmostral(x))
  print(desvioRelativoPercentual(x))
}
