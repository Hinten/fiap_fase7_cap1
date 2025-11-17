source("objetivo_g/utils.R")
source("objetivo_g/preparar_dados.R")

calculaModafunc <- function(vetor) {
  uniqv <- unique(vetor)
  freq <- tabulate(match(vetor, uniqv))
  max_freq <- max(freq)
  uniqv[freq == max_freq]
}

calcularModa <- function(vetor, verbose = TRUE) {
  assertVetorNumerio(vetor)

  moda <- calculaModafunc(vetor)

  if (verbose) {
    print(paste('A moda:', paste(moda)))
  }

  return(moda)
}

calcularModaFromJson <- function(json) {
  cultura_1 <- getDadosCultura1(json)

  print(paste("Calculando a moda da area de plantio de", CULTURA_1))

  moda <- calcularModa(cultura_1$area)

  print(paste("A moda da area de plantio de", CULTURA_1, ":", moda, "m2"))

  moda_fosfor <- calcularModa(cultura_1$fosforo)

  print(paste("A moda do fosforo de", CULTURA_1, ":", moda_fosfor, "kg"))

  moda_potassio <- calcularModa(cultura_1$potassio)

  print(paste("A moda do potassio de", CULTURA_1, ":", moda_potassio, "kg"))

  print(paste("Calculando a moda da area de plantio de", CULTURA_2))

  cultura_2 <- getDadosCultura2(json)

  moda2 <- calcularModa(cultura_2$area)

  print(paste("A moda da area de plantio de", CULTURA_2, ":", moda2, "m2"))

  moda_fosfor2 <- calcularModa(cultura_2$fosforo)

  print(paste("A moda do fosforo de", CULTURA_2, ":", moda_fosfor2, "kg"))

  moda_potassio2 <- calcularModa(cultura_2$potassio)

  print(paste("A moda do potassio de", CULTURA_2, ":", moda_potassio2, "kg"))
}


if (sys.nframe() == 0) {
  # Exemplo de uso
  vetor <- c(1, 2, 2, 2, 3, 4, 4, 4, 5)
  moda <- calculaModa(vetor)
  print(paste("A moda:", moda))
}
