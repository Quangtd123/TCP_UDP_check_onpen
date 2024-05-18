import socket
import concurrent.futures

def check_port(ip, port):
    # Tạo một socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Thiết lập timeout để tránh bị chặn vô thời hạn
    sock.settimeout(0.1)  # Thời gian timeout ngắn để giảm thời gian thử nghiệm

    try:
        # Thử kết nối tới địa chỉ IP và cổng đã chỉ định
        result = sock.connect_ex((ip, port))
        # Nếu kết nối thành công, trả về số cổng
        if result == 0:
            return port
    except socket.error:
        # Nếu kết nối thất bại, trả về None
        pass
    finally:
        # Luôn luôn đóng socket
        sock.close()

    return None

def check_all_ports(ip):
    open_ports = []  # Danh sách các cổng mở


    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
      
        future_to_port = {executor.submit(check_port, ip, port): port for port in range(1, 65536)}
        
 
        for future in concurrent.futures.as_completed(future_to_port):
            port = future_to_port[future]
       
            if future.result():
                open_ports.append(future.result())
                print(f"Port {future.result()} is open on IP {ip}")

    return open_ports


ip  = input(str("Nhập ip Cần check :"))


open_ports = check_all_ports(ip)


print("Open ports:", open_ports)
