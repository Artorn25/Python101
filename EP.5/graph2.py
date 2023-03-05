import matplotlib.pyplot as plt

# สร้างข้อมูลที่จะนำมาพล็อตกราฟ
x = [1,2,3,4]
y = [1,2,3,4]

# พล็อตกราฟแบบเส้น
plt.plot(x, y , color='blue' , marker='o' , linestyle='dashed' , linewidth=2 , markersize=2)

plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Graph')

# เเสดงกราฟ
plt.show()


