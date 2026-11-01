# Shared helpers for R visualisation exercises.
args<-commandArgs(trailingOnly=FALSE); file_arg<-grep("^--file=",args,value=TRUE); script_path<-if(length(file_arg))normalizePath(sub("^--file=","",file_arg[1]),mustWork=TRUE) else normalizePath("r/common.R",mustWork=TRUE)
root<-dirname(dirname(script_path)); data_file<-file.path(root,"data","student_scores.csv"); output_dir<-file.path(root,"output"); subjects<-c("Math","Science","English")
load_students<-function(){if(!file.exists(data_file))stop("Dataset missing; run 3B.R first."); d<-read.csv(data_file); req<-c("Student",subjects,"Age","Hours_Studied"); miss<-setdiff(req,names(d)); if(length(miss)||!nrow(d))stop(paste("Invalid dataset; missing:",paste(miss,collapse=", "))); d}
save_plot_path<-function(name){dir.create(output_dir,recursive=TRUE,showWarnings=FALSE); file.path(output_dir,name)}
