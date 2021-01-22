# parking-car

|      | |
| ---------- |-------------------|
| **Author**       | Ultralytics LLC|
| **Title**        | YOLO v.3 real time object detection |
| **Topics**       | Ứng dụng trong computer vision, sử dụng thuật toán chính là CNN|
| **Descriptions** | Input sẽ là các tấm hình và file .txt có tên tương ứng và chứa 5 thông số của object. đầu tiên là ```<class object>``` và ```<x, y, width, height>``` của bounding box chứa vật. khi train xong sẽ trả ra output là file trọng số ```weights```. Ta sẽ sử dụng trọng số ```weights``` đã train để predict bounding box và class của các object trong hình|
| **Links**        | https://github.com/ultralytics/yolov3|
| **Framework**    | PyTorch|
| **Pretrained Models**  | sử dụng weight đã được train sẵn https://pjreddie.com/media/files/yolov3.weights|
| **Datasets**     |Mô hình được train với bộ dữ liệu cocodataset.org. Ngoài ra còn có các tập dữ liệu có thể sử dụng: PASCAL VOC, Open Images Dataset V4,..v.v.,|
| **Level of difficulty**|Sử dụng nhanh và dễ, có thể train lại với tập dữ liệu khác tốc độ tùy thuộc vào phần cứng và hình ảnh input|
