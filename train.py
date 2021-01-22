from lib import *
from model import *
from load_data import *
from normalize import *
from splitdata import *
# Make Train data
X=[]
Z=[]
IMG_SIZE=48
FREE_DIR='data/empty'
FULL_DIR='data/occupied'

#Make Free data
make_train_data(X,Z,'Free',FREE_DIR,IMG_SIZE)
print(len(X))
# Make Full data
make_train_data(X,Z,'Full',FULL_DIR,IMG_SIZE)
print(len(X))

# Ve hinh
fig,ax=plt.subplots(5,2)
fig.set_size_inches(15,15)
for i in range(5):
    for j in range (2):
        l=rn.randint(0,len(Z))
        ax[i,j].imshow(X[l])
        ax[i,j].set_title('Parking: '+Z[l])
        
plt.tight_layout()
plt.show()

# Scale data X va one-hot encoder Y
le=LabelEncoder()
Y=le.fit_transform(Z)
Y=to_categorical(Y,2)
X=np.array(X)
X=X/255.0

# print(Y)
# Seperate Data to Train Test
x_train,x_test,y_train,y_test = tts(X,Y,test_size = 0.25)
print(x_train.shape)

# Train Data 
batch_size=128
epochs=50

red_lr= ReduceLROnPlateau(monitor='val_acc',patience=3,verbose=1,factor=0.1)
# data augmentation to prevent overfitting
datagen = ImageDataGenerator(
        featurewise_center=False,  # set input mean to 0 over the dataset
        samplewise_center=False,  # set each sample mean to 0
        featurewise_std_normalization=False,  # divide inputs by std of the dataset
        samplewise_std_normalization=False,  # divide each input by its std
        zca_whitening=False,  # apply ZCA whitening
        rotation_range=10,  # randomly rotate images in the range (degrees, 0 to 180)
        zoom_range = 0.1, # Randomly zoom image 
        width_shift_range=0.2,  # randomly shift images horizontally (fraction of total width)
        height_shift_range=0.2,  # randomly shift images vertically (fraction of total height)
        horizontal_flip=True,  # randomly flip images
        vertical_flip=False)  # randomly flip images


datagen.fit(x_train)

model = model()
model.compile(optimizer=Adam(lr=0.001),loss='categorical_crossentropy',metrics=['accuracy'])
model.summary()

#Train data
checkpoint_cb = ModelCheckpoint('final.h5', verbose=0, 
                                save_weights_only=True, save_freq='epoch')
History = model.fit_generator(datagen.flow(x_train,y_train, batch_size=batch_size),
                              epochs = epochs, validation_data = (x_test,y_test),
                              verbose = 1, steps_per_epoch=x_train.shape[0] // batch_size,callbacks=[red_lr,checkpoint_cb])

model.save('parkingcar.h5')



# Evaluate model
print(model.evaluate(x_train,y_train))
print(model.evaluate(x_test,y_test))
#Plot Learning_Curve
plt.subplot(1,2,1)
plt.plot(History.history['loss'])
plt.plot(History.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epochs')
plt.legend(['train', 'test'])
plt.subplot(1,2,2)
plt.plot(History.history['accuracy'])
plt.plot(History.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epochs')
plt.legend(['train', 'test'])
plt.show()

# Predict x_val 
pred=model.predict(x_test)
pred_digits=np.argmax(pred,axis=1)
# In nhung anh dung va sai
i=0
prop_class=[]
mis_class=[]
for i in range(len(y_test)):
    if(np.argmax(y_test[i])==pred_digits[i]):
        prop_class.append(i)
    if(len(prop_class)==8):
        break

i=0
for i in range(len(y_test)):
    if(not np.argmax(y_test[i])==pred_digits[i]):
        mis_class.append(i)
    if(len(mis_class)==8):
        break

# Used for displaying the correctly classified images

warnings.filterwarnings('always')
warnings.filterwarnings('ignore')

count=0
fig,ax=plt.subplots(4,2)
fig.set_size_inches(15,15)
for i in range (4):
    for j in range (2):
        ax[i,j].imshow(x_test[prop_class[count]])
        ax[i,j].set_title("Predicted : "+str(le.inverse_transform([pred_digits[prop_class[count]]]))+"\n"+"Actual : "+str(le.inverse_transform([np.argmax([y_test[prop_class[count]]])])))
        plt.tight_layout()
        count+=1

#Used for displaying the misclassified images

warnings.filterwarnings('always')
warnings.filterwarnings('ignore')

count=0
fig,ax=plt.subplots()
# fig.set_size_inches()

ax.imshow(x_test[mis_class[count]])
ax.set_title("Predicted : "+str(le.inverse_transform([pred_digits[mis_class[count]]]))+"\n"+"Actual : "+str(le.inverse_transform([np.argmax([y_test[mis_class[count]]])])))
plt.tight_layout()
plt.show()
count+=1
print("Number of wrong image: ",count)