from configs import *
# remember that the input data should always be channels last


def voxnet(config, input_shape):
    config['input_shape'] = input_shape
    model = Sequential()
    
    model.add(Conv3D(filters=32, kernel_size=(5, 5, 5), strides=(
        2, 2, 2), padding='valid',activation='relu',input_shape=input_shape))
    model.add(Dropout(config['dropout_rate']))
    model.add(Conv3D(filters=64, kernel_size=(3, 3, 3), strides=(
        1, 1, 1), padding='valid',activation='relu',input_shape=input_shape))
    model.add(Dropout(config['dropout_rate']))
    model.add(MaxPooling3D(pool_size=2, strides=(2, 2, 2), padding='valid'))
    model.add(Flatten())
   
    # Hidden layer
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(config['dropout_rate']))
    # Output layer
    model.add(Dense(config['num_classes'], activation='softmax'))
    model.summary()
    return model

def timo(config,input_shape):
    config['input_shape'] = input_shape
    model = Sequential()
    
    model.add(Conv3D(filters=32, kernel_size=(5, 5, 5), strides=(
        1, 1, 1), padding='same',activation='relu',input_shape=input_shape))
    model.add(Dropout(config['dropout_rate']))
    model.add(MaxPooling3D(pool_size=2, strides=(2, 2, 2), padding='valid'))
    
    model.add(Conv3D(filters=64, kernel_size=(3, 3, 3), strides=(
        1, 1, 1), padding='valid',activation='relu',input_shape=input_shape))
    model.add(Dropout(config['dropout_rate']))
    model.add(MaxPooling3D(pool_size=2, strides=(2, 2, 2), padding='valid'))
    
    model.add(Conv3D(filters=128, kernel_size=(3, 3, 3), strides=(
        1, 1, 1), padding='valid',activation='relu',input_shape=input_shape))
    model.add(Dropout(config['dropout_rate']))
    model.add(MaxPooling3D(pool_size=2, strides=(2, 2, 2), padding='valid'))
    model.add(Flatten())
   
    # Hidden layer
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(config['dropout_rate']))
    # Output layer
    model.add(Dense(config['num_classes'], activation='softmax'))
    model.summary()
    return model