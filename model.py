from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import perplexity
import burstiness
from data import data
import joblib
import features

X = [] # -> text
Y = [] # -> label

for item in data:
    features = features.extract(item["text"])
    X.append(features)
    Y.append(item["label"])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, Y_train)

accuracy = model.score(X_test, Y_test)
print(f"accuracy: {accuracy}")

joblib.dump(model, "modelDB.pkl")