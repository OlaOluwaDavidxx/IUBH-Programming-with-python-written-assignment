class Data(object):
    """Store y input as object"""
    def __init__(self, x, y_label=None, ideal_label=None):
        self.ideal_label = ideal_label
        self.y_label = y_label
        self.x = x

    def sign_y_train(self, train):
        self.y_train = train[self.y_label]

    def sign_y_ideal(self, ideal):
        self.y_ideal = ideal[self.ideal_label]


