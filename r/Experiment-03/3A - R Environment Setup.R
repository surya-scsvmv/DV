# Experiment 3A: install and load the R packages used in this lab.
packages<-c("ggplot2","tidyr","dplyr","RColorBrewer"); missing<-packages[!vapply(packages,requireNamespace,logical(1),quietly=TRUE)]; if(length(missing))install.packages(missing,repos="https://cloud.r-project.org"); invisible(lapply(packages,library,character.only=TRUE)); cat("R environment ready.\n")
