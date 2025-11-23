install.packages("jsonlite", lib= 'objetivo_g/lib', repos = "https://cloud.r-project.org/")
install.packages("readr", lib= 'objetivo_g/lib', repos = "https://cloud.r-project.org/")

library(jsonlite)
library(readr)

loadData <- function(){

  file_path <- "culturas.json"
  if (file.exists(file_path) == FALSE) {
    stop("File not found")
  }

  data <- fromJSON(file_path)

  return(data)

}

if (sys.nframe() == 0) {
  loadData()
}

