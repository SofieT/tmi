algo1 = read.table("times1.txt")
algo2 = read.table("times2.txt")
algo3 = read.table("times3.txt")

x = seq(10, length(algo1$V1) * 10, 10)
y = range(algo1)

plot(x, algo1$V1, type="n", ylab="Uitvoeringstijd (ms)", xlab="Aantal cirkels")
colors <- rainbow(3)

lines(x, algo1$V1, col=colors[1]) 
lines(x, algo2$V1, col=colors[2])
lines(x, algo3$V1, col=colors[3])

