# Tổng quan về ElasticSearch 
ElasticSearch là công cụ tìm kiếm phân tích phân tán ở trung tâm Elastic Stack. Logstash và Beats tạo điều kiện cho việc thu thập và làm phong phú dữ liệu của bạn và lưu trữ dữ liệu đó trong ElasticSearch. ElasticSearch là nơi xảy ra phép lập chỉ mục , tìm kiếm và phân tích   
ElasticSearch cũng cấp tìm kiếm và phân tích thời gian thực cho tất cả các loại dữ liệu. Cho dù văn bản có cấu trúc và không cấu trúc, dữ liệu số hoặc dữ liệu không gian địa lý. ElasticSearch có thể lưu trữ và lập chỉ mục một cách hiệu quả theo cách hỗ trợ tìm kiếm nhanh. Bạn có thể vượt xa thông tin truy xuất dữ liệu đơn giản và tổng hợp khám phá các xu hướng mà mẫu dữ liệu của bạn. Và khi dữ liệu và khối lượng truy vấn của bạn tăng lên , tính chất phân tánh của ElasticSearch cho phép triển khai của bạn phát triển liền mạch cùng với nó.  
ElasticSearch cung cấp tốc độ và tính linh hoạt để xử lý dữ liệu trong nhiều trường hợp sử dụng khác nhau:
- Thêm ô tìm kiếm vào app hoặc trang web
- Lưu trữ và phân tích nhật ký, số liệu và dữ liệu sự kiện bảo mật
- Sử dụng Machine Learning để tự động mô hình hóa hành vi dữ liệu của bạn trong thời gian thực
- Tự động hóa quy trình làm việc bằng cạc sử dụng ElasticSearch làm công cụ lưu trữ
- Quản lý tích hợp và phân tích thông tin không gian bằng cách sử dụng ElasticSearch làm hệ thống thông tin địa lý(GIS)
- Lưu trữ dữ liệu di truyền bằng cách sử dụng ElasticSearch làm công cụ nghiên cứu tin sinh học


### Dữ liệu trong : Tài liệu và chỉ số
 ElasticSearch là một cửa hàng tài liệu phân phối. Thay vì lưu trữ thông tin dưới dạng các hàng dữ liệu cột. ElastichSearch lưu trữ các cấu trúc dữ liệu phức tạp đã được tuần tự hoá dưới dạng tài liệu JSON.Khi bạn có nhiều node ElasticSearch trong một cụm , các tài liệu được lưu trữ sẽ được phân phối trên toàn cụm và có thể được truy cập ngay lập tức từ bất kì node nào  
 ElasticSearch sử dụng cấu trúc dữ liệu được gọi là chỉ mục đảo ngược hỗ trợ tìm kiếm văn bản rất nhanh. Một chỉ mục đảo ngược liệt kê mọi từ duy nhất xuất hiện trong bất kì tài liệu nào và xác định tất cả các tài liệu mà mỗi từ xuất hiện  
Cuối cùng, Tuy nhiên bạn biết nhiều hơn về dữ liệu của mình và cách mà bạn muốn sử dụng dữ liệu đó so với ElasticSearch có thể. Bạn có thể xác định rõ ràng ánh xạ để kiểm soát hoàn toàn cách các trường hợp được lưu trữ và lập chỉ mục

