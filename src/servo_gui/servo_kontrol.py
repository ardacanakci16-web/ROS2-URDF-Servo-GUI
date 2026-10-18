#!/usr/bin/env python3
import rospy
from std_msgs.msg import UInt16
import tkinter as tk

class ServoKontolPaneli:
    def __init__(self, root):
        self.root = root
        self.root.title("Servo Kontrol Paneli")
        
        self.pub = rospy.Publisher('/servo_aci', UInt16, queue_size=10)
        rospy.init_node('servo_mouse_panel', anonymous=True)
        
        self.label = tk.Label(root, text="Servo Açısı: 90", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.slider = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, 
                               length=300, command=self.aci_gonder)
        self.slider.set(90)
        self.slider.pack(pady=20)

    def aci_gonder(self, deger):
        aci = int(deger)
        self.label.config(text=f"Servo Açısı: {aci}")
        
        msg = UInt16()
        msg.data = aci
        self.pub.publish(msg)

if __name__ == '__main__':
    try:
        pencere = tk.Tk()
        uygulama = ServoKontolPaneli(pencere)
        pencere.mainloop()
    except rospy.ROSInterruptException:
        pass
