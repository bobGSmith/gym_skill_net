# Plot Function Network 
## use plotly for interactive "tooltip" hoverbox

library(ggnet)
library(ggnetwork)
library(Rgraphviz)
library(sna)
library(network)


adjacency = read.csv("./skill_matrix2.csv")
rownames(adjacency) = adjacency$X
adjacency$X = NULL

labels = c()
labels[colnames(adjacency)] = colnames(adjacency)
labels = labels[labels != "X"]


make_network_obj = function (adjacency, labels) {
    net = network (adjacency, directed = TRUE);
    net %v% "label" = as.character(labels)
    return (net); 
}

make_plot = function (net) {
    ggnetwork_net = ggnetwork(net,arrow.gap=0.02)
    plt = ggplot(ggnetwork_net, aes(x=x, y=y, xend=xend, yend=yend)) +
        geom_edges(color = "darkgray", arrow = arrow(length = unit(0.8, "lines"), type = "closed")) +
        geom_point(size=12,alpha=0.2,color = "lightgreen") +
        geom_point(size=4, color = "lightgreen") +
        geom_text(aes(label=label), color = "black") +
        theme_blank () 
    return (plt)
}

net = make_network_obj(adjacency, labels)

plt = make_plot(net)

ggsave("./skillnet.png", plot=plt,limitsize=FALSE,dpi=400, units="cm",width=40,height=40)


# arrow workaround https://github.com/plotly/plotly.R/issues/469 use plot_ly directly?
pltl = plotly::ggplotly(plt)
pltl
htmlwidgets::saveWidget(pltl,file="skillnet.html")
