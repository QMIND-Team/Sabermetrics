

#Credit to the Nhl-Player-Point-Predictions for these funcions

def scatter_plot(X_var, Y_var, colour, x_label, y_label, title):
    plt.scatter(Y_var, X_var, c=colour, marker='.')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
    return

# distribution function
def histogram(column):
    plt.hist(column)

# good to visualize the range of an attribute
def boxplot(column):
    plt.boxplot(column)

