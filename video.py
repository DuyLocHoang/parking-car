from lib import *

class_dictionary = {}
class_dictionary[0] = 'empty'
class_dictionary[1] = 'occupied'
def load_data(path) :
    files = open(path,'rb')
    return pickle.load(files)

final_spot_dict = load_data('spot_dict.pickle')
model = load_model('parkingcar.h5')
print(final_spot_dict)

def make_prediction(image):
    #Rescale image
    img = image/255.

    #Convert to a 4D tensor
    image = np.expand_dims(img, axis=0)
    #print(image.shape)

    # make predictions on the preloaded model
    
    class_predicted = model.predict(image)
    
    
    inID = np.argmax(class_predicted[0])
    label = class_dictionary[inID]
    return label

video_name = 'parking_video.mp4'
cap = cv2.VideoCapture(video_name)
ret = True
count = 0

while ret:
        ret, image = cap.read()
        count += 1
        if count == 5:
            count = 0
            
            new_image = np.copy(image)
            overlay = np.copy(image)
            cnt_empty = 0
            all_spots = 0
            color = [0, 255, 0] 
            alpha=0.5
            start_time = time.time()
            for spot in final_spot_dict.keys():
                all_spots += 1
                (x1, y1, x2, y2) = spot
                (x1, y1, x2, y2) = (int(x1), int(y1), int(x2), int(y2))
                #crop this image
                spot_img = image[y1:y2, x1:x2]
                spot_img = cv2.resize(spot_img, (48, 48)) 
                
                label = make_prediction(spot_img)
        #         print(label)
                if label == 'empty':
                    cv2.rectangle(overlay, (int(x1),int(y1)), (int(x2),int(y2)), color, -1)
                    cnt_empty += 1
            end_time = time.time()
            print("Time Predict: {}".format(end_time-start_time))
            cv2.addWeighted(overlay, alpha, new_image, 1 - alpha, 0, new_image)

            cv2.putText(new_image, "Available: %d spots" %cnt_empty, (30, 95),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7, (255, 255, 255), 2)

            cv2.putText(new_image, "Total: %d spots" %all_spots, (30, 125),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7, (255, 255, 255), 2)
            cv2.imshow('frame', new_image)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        #out.write(image)

cv2.destroyAllWindows()
cap.release()