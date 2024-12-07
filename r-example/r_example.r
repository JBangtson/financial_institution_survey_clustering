# Repeating the clustering code from class in R
library(cluster)
library(dplyr)
library(readr)

d <- read_tsv("survey_responses.txt")

names(d) <- c("time","name","born_dist",
              "dist_15","post_sec_yrs",
              "mkt","biz","hh_size")

d <- d %>%
  mutate(mkt = ifelse(mkt=="Yes",1,0),
         biz = ifelse(biz=="Yes",1,0))

data.for.clust <- d %>% select(born_dist:hh_size)

clust1 <- 
  pam(x=data.for.clust,
    k=3)

summary(clust1)
table(clust1$clustering)

# rescale all vars. Not exactly the same as 
# what we do in the Python code
data.for.clust <- d %>% 
  select(born_dist:hh_size) %>%
  mutate_all(.funs=scale)

clust2 <- 
  pam(x=data.for.clust,
      k=3)

summary(clust2)
table(clust2$clustering)
# Much more even splitting

