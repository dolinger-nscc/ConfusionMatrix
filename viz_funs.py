from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def sns_cm(y, y_hat, size=(6,4), cols=['silver', 'green'], 
        y_lab='y', y_hat_lab='y-hat', title='Confusion Matrix'):
    '''
    Enter the y values as a series, and the y-hat values as a series to return a confusion matrix.
    You may also configure the following:
    size -> size of the confusion matrix, default is (6,4), enter as a tuple
    cols -> colours, default is ['silver', 'green'], enter as a list
    y_lab -> y (actual) label, default is 'y', enter as a string
    y_hat_lab -> y-hat (prediction) label, default is 'y-hat', enter as a string
    title -> confusion matrix title, default is 'Confusion Matrix', enter as a string
    '''
    labs = y.unique().tolist()
    cm = confusion_matrix(y, y_hat, labels=labs)
    plt.figure(figsize=size)
    sns.heatmap(data=cm, annot=True, xticklabels=labs, yticklabels=labs, 
                     cbar=False, linewidths=.6, cmap=cols)
    plt.xlabel(y_hat_lab)
    plt.ylabel(y_lab)
    plt.title(title)
    plt.show()