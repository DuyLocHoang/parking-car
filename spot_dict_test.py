from utils.preprocessing import *
from lib import *
test_images = [plt.imread(path) for path in glob.glob('data/test/*.jpg')]

# Show anh goc
show_images(test_images)

# Filter nhung vung co mau trang va mau vang
white_yellow_images = list(map(select_rgb_white_yellow, test_images))
show_images(white_yellow_images)

# Convert to grayscale
gray_images = list(map(convert_gray_scale, white_yellow_images))
show_images(gray_images)

# Detect cac canh
edge_images = list(map(lambda image: detect_edges(image), gray_images))
show_images(edge_images)

# Chon ra nhung vung quan trong dung polygon de ve
roi_images = list(map(select_region, edge_images))
show_images(roi_images)

# Xac dinh cac duong line thang dung Houghline
list_of_lines = list(map(hough_lines, roi_images))
line_images = []
for image, lines in zip(test_images, list_of_lines):
    line_images.append(draw_lines(image, lines))
    
show_images(line_images)

# Chia va ve cac lanes dau xe dang co tren hinh 
rect_images = []
rect_coords = []
for image, lines in zip(test_images, list_of_lines):
    new_image, rects = identify_blocks(image, lines)
    rect_images.append(new_image)
    rect_coords.append(rects)
    
show_images(rect_images)

# Draw va luu cac toa do cua nhung vi tri do xe co the co tren hinh dua tren cac line va lane
delineated = []
spot_pos = []
for image, rects in zip(test_images, rect_coords):
    new_image, spot_dict = draw_parking(image, rects)
    delineated.append(new_image)
    spot_pos.append(spot_dict)
    
show_images(delineated)

# Draw anh cuoi da duoc chia lane
final_spot_dict = spot_pos[1]
def assign_spots_map(image, spot_dict = final_spot_dict, make_copy = True, color=[255, 0, 0], thickness=2):
    if make_copy:
        new_image = np.copy(image)
    for spot in spot_dict.keys():
        (x1, y1, x2, y2) = spot
        cv2.rectangle(new_image, (int(x1),int(y1)), (int(x2),int(y2)), color, thickness)
    return new_image
marked_spot_images =  list(map(assign_spots_map, test_images))
show_images(marked_spot_images)

# Luu vao file pickle cho qua trinh predict tiep theo 
import pickle

with open('spot_dict_test.pickle', 'wb') as handle:
    pickle.dump(final_spot_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

