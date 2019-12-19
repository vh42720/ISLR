import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report


def print_cm(y_test, pred, model):
	cm_df = pd.DataFrame(confusion_matrix(y_test, pred).T, index=model.classes_, columns=model.classes_)
	cm_df.index.name = 'Predicted'
	cm_df.columns.name = 'True'
	print('Confusion Matrix \n', cm_df, '\n\nClassification report \n', classification_report(y_test, pred, digits=3))
