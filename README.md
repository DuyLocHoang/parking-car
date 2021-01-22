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
| **Team**       | Hoàng Duy Lộc(loc.hoangduyloc@gmail.com|
| **Predicting** | Đầu vào là tấm ảnh overhead của một bãi đỗ xe từ đó detect ra số vị trí trống trong bãi đõ xe |
| **Data**       | Là những ảnh được đã được segmentation vị trí đỗ xe free hay occupied. Data được đặt trong file data gồm 96 ảnh free và 198 ảnh occupied|
| **Features**   | How many features do you have and which features are the raw input data (ex. color, weight, location, etc) vs. features you have derived (ex. ICA, Gaussian Kernel)? Why they are appropriate for this task? **(3-4 sentences max)**|
| **Models**     | Exactly which model(s) are you using? Write out the basic math formulas and clearly note any modifications or additions. If you have more than one model, make subsections for each. **(3-4 sentences max)**|
| **Results**    | Make a compact table of results. Each row should be a different model. The columns should be the training error and the test error. List how many samples are in each of the training and testing data sets. Obviously, these sets should be different. **(1-2 sentences max + 1 table max)**|
| **Discussion** | This is where you share your thoughts about your project. (Hopefully you have a few interesting interpretations!) Briefly summarized what just happened. Briefly explain whether or not you expected your results. If your results were good, explain why. If they were not good, explain why. **(6 sentences max)**|
| **Future**     | If you had another 6 months to work on this, what would you do first? **(2-3 sentences max)**|
|**References**  |[IEEE style](https://ctan.org/topic/bibtex-sty?lang=en) is fine|
