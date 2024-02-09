# In deze module wordt het k_nearest neighboor algoritme toegepast
# import statements
import inlezen_file as read
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score, precision_score, f1_score, fbeta_score
from sklearn.neighbors import KNeighborsClassifier as KNN
from joblib import dump, load
# de file inlezen en in een pandas dataframe stoppen
candy = read.read_file("candy-data.csv")   

# feature extraction
candy["winpercent"] /= 100
X = candy.drop(["chocolate", "competitorname"], axis=1).values
Y = candy.chocolate.values.astype(float)
# knn variabele aanmaken
knn = KNN(n_neighbors=3)  
knn.fit(X, Y)
yp = knn.predict(X)
# het model evalueren
print("De nauwkeurigheid is")
print(accuracy_score(Y, yp))
print("De confusion matrix is")
print(confusion_matrix(Y, yp))
print("De recall is")
print(recall_score(Y, yp))
print("De precision is")
print(precision_score(Y, yp))
print("de f1-score is")
print(f1_score(Y, yp))
print("De fbeta-scorre is")
print(fbeta_score(Y, yp, 1))
# finale model opslaan met joblib
dump(knn, 'model_halloween_candy.joblib');
