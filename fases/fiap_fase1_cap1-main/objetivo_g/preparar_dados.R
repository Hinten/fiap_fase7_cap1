library(dplyr)

getDadosCultura1 <- function(json){

  cultura_1 <- data.frame(json$cultura_1)

  cultura_1$area <- ifelse(cultura_1$tipo == 1, cultura_1$base * cultura_1$altura, cultura_1$base * cultura_1$altura / 2)

  cultura_1$fosforo <- cultura_1$area /10000 * 120
  cultura_1$potassio <- cultura_1$area /10000 * 200



  return(cultura_1)
}

getDadosCultura2 <- function(json){
  cultura_2 <- data.frame(json$cultura_2)

  cultura_2$area <- ifelse(cultura_2$tipo == 1, cultura_2$base * cultura_2$altura, cultura_2$base * cultura_2$altura / 2)

  cultura_2$fosforo <- cultura_2$area /10000 * 100
  cultura_2$potassio <- cultura_2$area /10000 * 120


  return(cultura_2)
}