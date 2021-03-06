# parking-car

|      | |
| ---------- |-------------------|
| **Author**       | Hoang Duy Loc|
| **Title**        | detect empty (available) parking slots from overhead images |
| **Topics**       | Ứng dụng trong computer vision, sử dụng thuật toán chính là mô hình CNN đơn giản|
| **Descriptions** | Input sẽ là các tấm hình nơi đỗ xe occupied hay free . khi train xong sẽ trả ra output là file trọng số ```weights```. Ta sẽ sử dụng trọng số ```weights``` đã train để predict chỗ đậu xe còn trống trong hình ảnh overhead của một bãi đỗ xe|
| **Links**        | https://github.com/ultralytics/yolov3|
| **Framework**    | Keras|
| **Datasets**     |Mô hình được train với bộ dữ liệu gồm các ảnh được segmentation vị trí đỗ xe có hay không lấp đầy|
| **Level of difficulty**|Sử dụng nhanh và dễ, tùy vào số lượng chỗ đõ xe nhiều hay ít mà ảnh hưởng tới tốc độ đáp ứng|

### Final Project poster
| **Title**      | Detect empty parking slots|
| ---------- |-------------------|
| **Team**       | Hoàng Duy Lộc(loc.hoangduyloc@gmail.com)|
| **Predicting** | Đầu vào là tấm ảnh overhead của một bãi đỗ xe từ đó detect ra số vị trí trống trong bãi đõ xe |
| **Data**       | Là những ảnh được đã được segmentation vị trí đỗ xe free hay occupied. Data được đặt trong file data gồm 96 ảnh free và 198 ảnh occupied|
| **Features**   | |
| **Models**     | Mô hình CNN dùng để classification giữa 2 class free và occupied. Model gồm 4 lớp Conv2D, 1 lớp Dense và đầu ra làm hàm sigmoid  với Loss = Crossentroy và Metrics = 'accuracy', ngoài ra còn sử dụng những kỹ thuật tránh overfitting như augmentation data, cũng như reduce learning rate giúp mô hình tốt hơn  |
| **Results**    | Loss train : 0.027 - accuracy : 1.000 ; Loss val : 0.1055 - accuracy : 0.9682  |
| **Discussion** | |
| **Future**     |Thực hiện bài toán trên bằng object detection model SSD|
|**References**  |[OPENCV tutorial](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)|

### RUN CODE
1. RUn file spot_dcit_test.py để lấy ra vị trí của những ô đỗ xe dạng dictionary lưu vào file pickle
2. Run file train.py lấy ra weights lưu vào file detect.h5 
3. Run file predict.py để predict ảnh trong data/test/
4. Run file video.py để predict video 

### Kết quả thủ được
<img src="https://github.com/DuyLocHoang/parking-car/blob/master/predict.jpg">

### Link Google Colab
[Google Colab](https://colab.research.google.com/drive/1JjrPr5MvfgNE-iEJ319S8Td1BeztObXY?usp=sharing)
### Pipeline xử lý ảnh toàn cảnh đầu vào 
<img src="https://lh4.googleusercontent.com/XitV4hQleXeRDYsHqJHfQbeinaq-arnVHDS4nWqJauMn0HYBRdJonNSQF1v1_dhLKG0kxXHjR6uWtOFNhaqmCHODNXPokG5tQoCvLR0S">

### Deploy
[Dùng Gradio deploy sản phẩm trên webserver](https://www.gradio.app/getting_started)
