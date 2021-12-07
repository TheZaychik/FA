
tab <- table(dat$Sector)
tab

perc <- tab / sum(tab) * 100
perc
perc_round <- round(perc, 2)
perc_labs <- paste0(perc_round, "%")
perc_labs

sects <- names(tab)
sects

sect_cols <- c("thistle1", "red", "yellow", "maroon4", 
               "purple2", "paleturquoise",
               "cornflowerblue", "green", "royalblue1",
               "blue", "navy")

dev.copy(jpeg, "S&P500.jpeg")
pie(tab, main = "S&P 500", col = sect_cols, labels = perc_labs)
legend(x=-1.2, y =-0.7, sects, cex = 0.7, 
       fill = sect_cols, ncol = 3, bty = "n")
dev.off()

