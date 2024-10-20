import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
#################
massiv = np.array([[6,1,7],[6,13,1000000],[99,100,78]])
massiv[0:] = 1000000
print(massiv)
#################
test_img = Image.open('nintendo_logo.jpg')
new_img_name = ('nintendo_logo.png')
test_img.save(new_img_name)

new_img_name = Image.open('nintendo_logo.png')
print('во второй картинке до изменений:', new_img_name.format, new_img_name.size, new_img_name.mode)
new_img_name = new_img_name.resize((1000,1000))

print('в первой картинке: ', test_img.format, test_img.size, test_img.mode)
print('во второй картинке после изменений: ', new_img_name.format, new_img_name.size, new_img_name.mode)


#########
plt.plot([1,2,3,1], [2,6,2,2])
plt.plot([1.5,2,2.5,1.5],[4,2,4,4])
plt.show()
