from lib import *
from utils.preprocessing import *
import gradio as gr
class_dictionary = {}
class_dictionary[0] = 'empty'
class_dictionary[1] = 'occupied'

def load_data(path) :
    files = open(path,'rb')
    return pickle.load(files)

final_spot_dict = load_data('spot_dict.pickle')
model = load_model('parkingcar.h5')

def make_prediction(image,model):
    #Rescale image
    img = image/255.
    #Convert to a 4D tensor
    image = np.expand_dims(img, axis=0)
#     print(image.shape)

    # make predictions on the preloaded model
    class_predicted = model.predict(image)
    inID = np.argmax(class_predicted[0])
    label = class_dictionary[inID]
    return label

def predict_on_image(image, spot_dict = final_spot_dict, make_copy=True, color = [0, 255, 0], alpha=0.5):
    if make_copy:
        new_image = np.copy(image)
        print(image.shape)
        overlay = np.copy(image)
    cnt_empty = 0
    all_spots = 0
    for spot in spot_dict.keys():
        all_spots += 1
        (x1, y1, x2, y2) = spot
        (x1, y1, x2, y2) = (int(x1), int(y1), int(x2), int(y2))
        #crop this image
        spot_img = image[y1:y2, x1:x2]
        spot_img = cv2.resize(spot_img, (48, 48)) 
        
        label = make_prediction(spot_img,model)
#         print(label)
        if label == 'empty':
            cv2.rectangle(overlay, (int(x1),int(y1)), (int(x2),int(y2)), color, -1)
            cnt_empty += 1
            
    cv2.addWeighted(overlay, alpha, new_image, 1 - alpha, 0, new_image)
            
    cv2.putText(new_image, "Available: %d spots" %cnt_empty, (30, 95),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7, (255, 255, 255), 2)
    
    cv2.putText(new_image, "Total: %d spots" %all_spots, (30, 125),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7, (255, 255, 255), 2)
    # save = True
    
    # if save:
    #     filename = 'predict.jpg'
    #     cv2.imwrite(filename, new_image)
    
    return new_image
def detect(test_images):
# test_images = [plt.imread(path) for path in glob.glob('data/test/*.jpg')]
    print(test_images.shape)
    predicted_images = list(map(predict_on_image, test_images))
    return predicted_images
    # show_images(predicted_images)

# iface = gr.Interface(predict_on_image, gr.inputs.Image(), "image")
# iface.launch()

test_images = [plt.imread(path) for path in glob.glob('data/test/*.jpg')]
predicted_images = list(map(predict_on_image, test_images))
show_images(predicted_images)