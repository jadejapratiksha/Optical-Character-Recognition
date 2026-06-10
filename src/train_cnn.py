def tran():
    from keras.models import Sequential
    from keras.layers import Dense, Dropout, Flatten
    from keras.layers import Conv2D, MaxPooling2D
    from keras.utils import np_utils
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    # set the matplotlib backend so figures can be saved in the background
    import cv2
    import os
    import numpy as np
    
    # the list of data (i.e., images) and class images
    print("[INFO] loading images...")
    k=1
    data=[]
    x=os.listdir('nhcd/')
    labels=[]
    aa=-1
    k=-1
    for filename in x:
        y=os.listdir('nhcd/'+filename+'/')
        aa=aa+1
        k=k+1
        for file in y:
            img=cv2.imread('nhcd/'+filename+'/'+file,0)
            ret,seg = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
            data.append(seg)
            labels.append(k)
            print(k)
            
    data = np.array(data)
    labels = np.array(labels) 
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.10,random_state = 50) 
    
    
    #Reshape input data 
    X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
    X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
    
    #Normalize inputs from 0-255 to 0-1 
    X_train = X_train.astype('float32') / 255
    X_test = X_test.astype('float32') / 255
    
    #One hot encoding of outputs
    y_train = np_utils.to_categorical(y_train, 58)
    y_test = np_utils.to_categorical(y_test, 58)
    
    #Build CNN model
    
    model = Sequential()
    
    model.add(Conv2D(64, (2,2), input_shape=(28,28,1), activation = "relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))
    
    model.add(Conv2D(32, (2,2), activation = "relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))
    
    model.add(Flatten())
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(58,activation="softmax"))
    
    model.summary()
    
    
    #Compile the model
    model.compile(loss='categorical_crossentropy',
                 optimizer='adam',
                 metrics=['accuracy'])
    #Fit the model
    history = model.fit(X_train,y_train, epochs=5,batch_size=128,verbose=1)
    
    scores = model.evaluate(X_test,y_test)
    
    print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    print("\n%s: %.2f%%" % (model.metrics_names[0], scores[0]*100))
    
    # Plot accuracy result
    plt.plot(history.history['accuracy'])
    plt.title('model accuracy plot')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='lower right')
    plt.show()
    plt.savefig('plot1.png',  bbox_inches='tight')
    # Plot loss result
    plt.plot(history.history['loss'])
    plt.title('model loss plot')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper right')
    plt.show()
    plt.savefig('plot2.png', bbox_inches='tight')
    model.save("Model/model.h5")
    return scores[1]*100
