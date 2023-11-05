from keras.models import Sequential
from keras.layers import Dense
import numpy as np


class Neural_Keras:
    def __init__(
            self,
            path_dataset='data.txt',
            input_dim=8,
            num_epochs=15,
            batch_size=10
    ):
        self.BATCH_SIZE = batch_size
        self.NUM_EPOCHS = num_epochs
        self.INPUT_DIM = input_dim
        self.path_dataset = path_dataset
        self.dataset = []
        self.X_train = []
        self.Y_train = []
        self.model = Sequential()

    def data_preparation(self):
        np.set_printoptions(precision=2, floatmode='fixed', suppress=True)
        self.dataset = np.genfromtxt(self.path_dataset, dtype=float, delimiter=',')

        for i in range(len(self.dataset[0]) - 1):
            self.dataset = self.dataset[~np.isnan(self.dataset[:, i])]

        self.dataset = np.around(self.dataset, 2)

        dt_sh = self.dataset.shape[1] - 1
        self.Y_train = self.dataset[:, -1]
        self.X_train = self.dataset[:, :dt_sh]

        self.model.add(Dense(12, input_dim=self.INPUT_DIM, activation='relu'))
        self.model.add(Dense(8, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))

    def training_ker(self):
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.model.fit(self.X_train, self.Y_train, epochs=self.NUM_EPOCHS, batch_size=self.BATCH_SIZE, verbose=2)

    def inference_ker(self):
        return self.model.predict(np.array(self.X_train[:3]))


nn = Neural_Keras()
nn.data_preparation()
nn.training_ker()
print(nn.inference_ker())
