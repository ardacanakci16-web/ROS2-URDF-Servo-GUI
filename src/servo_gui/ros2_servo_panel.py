#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import tkinter as tk
import serial
import threading

class ServoControlNode(Node):
    def __init__(self, tcl_app):
        super().__init__('ros2_servo_mouse_panel')
        self.app = tcl_app
        
        # ROS 2 Publisher (Açı verisini yayınlamak için)
        self.publisher_ = self.create_publisher(Int32, 'servo_aci', 10)
        
        # Arduino Seri Bağlantısı (Portunu kontrol et: /dev/ttyACM0 veya /dev/ttyUSB0)
        try:
            self.serial_port = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.1)
            self.get_logger().info("Arduino'ya başarıyla bağlanıldı!")
        except Exception as e:
            self.get_logger().error(f"Arduino'ya bağlanılamadı: {e}\nLütfen portu kontrol edin!")
            self.serial_port = None

    def aci_gonder(self, deger):
        aci = int(deger)
        self.app.label.config(text=f"Servo Açısı: {aci}")
        
        # 1. ROS 2 üzerinden veriyi yayınla
        msg = Int32()
        msg.data = aci
        self.publisher_.publish(msg)
        
        # 2. Arduino'ya seri port üzerinden gönder
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.write(f"{aci}\n".encode())

class PanelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ROS 2 Servo Kontrol Paneli")
        
        self.label = tk.Label(root, text="Servo Açısı: 90", font=("Arial", 14))
        self.label.pack(pady=10)
        
        # Açı kaydırma çubuğu
        self.slider = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, 
                               length=300, command=self.aci_degisti)
        self.slider.set(90)
        self.slider.pack(pady=20)
        
        # ROS 2 Başlatılıyor
        rclpy.init()
        self.node = ServoControlNode(self)
        
        # ROS 2'nin arka planda kilitlenmeden çalışması için bir thread (iş parçacığı) başlatıyoruz
        self.ros_thread = threading.Thread(target=lambda: rclpy.spin(self.node), daemon=True)
        self.ros_thread.start()

    def aci_degisti(self, deger):
        self.node.aci_gonder(deger)

    def on_closing(self):
        if self.node.serial_port:
            self.node.serial_port.close()
        self.node.destroy_node()
        rclpy.shutdown()
        self.root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = PanelApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
