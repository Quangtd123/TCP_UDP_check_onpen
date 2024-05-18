import socket

kamiip = input(str("Nhập ip Cần check :"))
def check_udp_port(host, port):
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.settimeout(1)  # Thiết lập timeout cho kết nối UDP
        
        # Kết nối đến cổng UDP
        udp_socket.connect((host, port))
        udp_socket.close()
        
        return True
    except:
        return False

def scan_udp_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        if check_udp_port(host, port):
            open_ports.append(port)
    return open_ports

if __name__ == "__main__":
    target_host = kamiip  # Thay đổi thành địa chỉ IP hoặc tên miền của máy bạn muốn kiểm tra
    start_port = 1  # Cổng bắt đầu
    end_port = 65535  # Cổng kết thúc
    
    open_udp_ports = scan_udp_ports(target_host, start_port, end_port)
    
    if open_udp_ports:
        print("Cổng UDP mở trên", target_host, ":", open_udp_ports)
    else:
        print("Không có cổng UDP nào mở trên", target_host)
