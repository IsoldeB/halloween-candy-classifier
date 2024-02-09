from joblib import load
import numpy as np
class HalloweenCandy:
    def __init__(self, filename):
        self.filename = filename
        self.model = None
        self.__features = ["fruity", "caramel", "peanutyalmondy", "nougat", "crispedricewafer", 
                    "hard", "bar", "pluribus", "sugarpercent", "pricepercent", "winpercent"]
    def load_model(self):
        self.model = load(self.filename)
    def is_chocolate(self, **features):
        X = np.array([features[feature] for feature in self.__features], dtype=float)
        return self.model.predict(X[np.newaxis, :]).astype(bool).item()  
        
    