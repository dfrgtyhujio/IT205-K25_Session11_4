#  1. PHÂN TÍCH INPUT/OUTPUT
# Input:
# - Lựa chọn menu: Chuỗi ký tự (str)
# - Mã sản phẩm: Chuỗi ký tự (str)
# - Số lượng mua / Số lượng nhập thêm: Chuỗi ký tự (str), sau đó ép kiểu sang số nguyên (int)
# Output:
# - Danh sách sản phẩm kèm trạng thái tồn kho chi tiết (Còn hàng, Sắp hết hàng, Hết hàng)
# - Tổng tiền khách cần thanh toán hoặc các thông báo lỗi tương ứng với từng bẫy dữ liệu
# - Báo cáo doanh thu chi tiết từng sản phẩm, tổng doanh thu và tên sản phẩm bán chạy nhất
#
# 2. ĐỀ XUẤT GIẢI PHÁP
# - Quản lý luồng: Dùng vòng lặp 'while True' để hiển thị menu liên tục
# - Chuẩn hóa chuỗi: Dùng phương thức '.strip().upper()' xử lý khoảng trắng và chữ hoa của mã sản phẩm
# - Kiểm tra số hợp lệ: Dùng '.isdigit()' kết hợp so sánh '> 0' để đảm bảo số lượng nhập vào là số nguyên dương
# - Kiểm tra tồn tại sản phẩm: Áp dụng cấu trúc vòng lặp 'for-else' tối giản của Python để tìm kiếm sản phẩm theo mã
# - Thống kê doanh thu: Tính toán trực tiếp dựa trên trường 'sold' và 'price', dùng thuật toán tìm Max để xác định sản phẩm bán chạy
#
# 3. THIẾT KẾ THUẬT TOÁN
# Bước 1: Khởi tạo danh sách 'product_list' chứa 3 sản phẩm ban đầu đầy đủ thông tin tồn kho và số lượng đã bán
# Bước 2: Vào vòng lặp menu, nhận lựa chọn từ người dùng
# Bước 3: Rẽ nhánh xử lý theo lựa chọn (1-5):
#   - Chức năng 1: Duyệt danh sách; xét điều kiện 'quantity' (==0: Hết hàng, <=5: Sắp hết hàng, >5: Còn hàng) để hiển thị
#   - Chức năng 2: Nhập mã -> Dùng 'for-else' tìm kiếm; Nhập số lượng mua -> Kiểm tra số nguyên dương và số lượng tồn kho -> Trừ 'quantity', cộng 'sold'
#   - Chức năng 3: Nhập mã -> Dùng 'for-else' tìm kiếm; Nhập số lượng nhập thêm -> Kiểm tra số nguyên dương -> Cộng dồn vào 'quantity'
#   - Chức năng 4: Kiểm tra nếu tổng số lượng đã bán bằng 0 thì báo chưa có doanh thu; ngược lại duyệt danh sách tính doanh thu và tìm sản phẩm bán chạy nhất
#   - Chức năng 5: In thông báo thoát và gọi lệnh 'break'
#   - Lựa chọn sai: In thông báo yêu cầu nhập lại


product_list = [
    {"product_id": "SP001", "product_name": "Áo polo nam", "price": 299000, "quantity": 20, "sold": 5},
    {"product_id": "SP002", "product_name": "Quần kaki nam", "price": 399000, "quantity": 8, "sold": 3},
    {"product_id": "SP003", "product_name": "Váy công sở nữ", "price": 459000, "quantity": 3, "sold": 7}
]

while True:
    print("\n===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")
    
    choice = input("Nhập lựa chọn (1-5): ")
    
    if choice == "1":
        if not product_list:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("Danh sách sản phẩm hiện tại:")
            for index, p in enumerate(product_list, start=1):
                if p["quantity"] == 0:
                    status = "Hết hàng"
                elif p["quantity"] <= 5:
                    status = "Sắp hết hàng"
                else:
                    status = "Còn hàng"
                print(f"{index}. Mã SP: {p['product_id']} | Tên: {p['product_name']} | Giá: {p['price']} | Tồn kho: {p['quantity']} | Đã bán: {p['sold']} | Trạng thái: {status}")
                
    elif choice == "2":
        product_id = input("Nhập mã sản phẩm khách muốn mua: ").strip().upper()
        
        for i in product_list:
            if i["product_id"] == product_id:
                break
        else:
            print("Không tìm thấy sản phẩm cần bán")
            continue
            
        quantity = input("Nhập số lượng khách mua: ").strip()
        if not quantity.isdigit() or int(quantity) <= 0:
            print("Số lượng mua không hợp lệ")
            continue
            
        quantity_to_buy = int(quantity)
        if quantity_to_buy > i["quantity"]:
            print("Số lượng trong kho không đủ để bán")
            continue
            
        i["quantity"] -= quantity_to_buy
        i["sold"] += quantity_to_buy
        print(f"Bán hàng thành công! Khách cần thanh toán: {quantity_to_buy * i['price']} VND")
        
    elif choice == "3":
        product_id = input("Nhập mã sản phẩm cần nhập thêm: ").strip().upper()
        
        for i in product_list:
            if i["product_id"] == product_id:
                break
        else:
            print("Không tìm thấy sản phẩm cần Nhập kho")
            continue
            
        quantity = input("Nhập số lượng nhập thêm: ").strip()
        if not quantity.isdigit() or int(quantity) <= 0:
            print("Số lượng Nhập kho không hợp lệ")
            continue
            
        i["quantity"] += int(quantity)
        print("Nhập thêm hàng thành công!")
        

    elif choice == "4":
        total_revenue = 0
        best_seller = None
        max_sold = 0
        
        for index, p in enumerate(product_list, start=1):
            product_revenue = p["price"] * p["sold"]
            total_revenue += product_revenue
            
            if p["sold"] > max_sold:
                max_sold = p["sold"]
                best_seller = p["product_name"]
                
            print(f"{index}. {p['product_name']} | Đã bán: {p['sold']} | Doanh thu: {product_revenue}")
            
        if total_revenue == 0:
            print("Chưa có doanh thu phát sinh.")
        else:
            print(f"\nTổng doanh thu: {total_revenue}")
            print(f"Sản phẩm bán chạy nhất: {best_seller}")
        
    elif choice == "5":
        print("Thoát chương trình.")
        break
        
    else:
        print('Lựa chọn không hợp lệ, vui lòng nhập lại!')
