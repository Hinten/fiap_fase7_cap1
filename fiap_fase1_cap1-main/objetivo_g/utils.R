
assertVetorNumerio <- function (vetor){
  stopifnot(is.vector(vetor))
  stopifnot(is.integer(vetor) || is.double(vetor))

  return(TRUE)

}
