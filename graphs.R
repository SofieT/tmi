algo1 = read.table("times1.txt")
algo2 = read.table("times2.txt")
algo3 = read.table("times3.txt")
ni1 = read.table("numberOfIntersections1")
ni2 = read.table("numberOfIntersections2")
ni3 = read.table("numberOfIntersections3")

x = seq(20, length(algo1$V1) * 20, 20)
y = range(algo1)

plot(x, algo1$V1, type="n", ylab="Uitvoeringstijd (ms)", xlab="Aantal cirkels")
colors <- rainbow(3)

lines(x, algo1$V1, col=colors[1]) 
lines(x, algo2$V1, col=colors[2])
lines(x, algo3$V1, col=colors[3])

plot(x, ni1$V1, ylab="aantal snijpunten", xlab="Aantal cirkels")