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
