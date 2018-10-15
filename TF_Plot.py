import matplotlib.pyplot as plt
import numpy as np

acc = [0.9727216713905334, 0.9822700041453044, 0.9836183380126953]

def f(acc):
	t = []
	for i in range(len(acc)):
		t.append(i+1)
	return t

plt.figure(figsize=(8,5))
plt.plot(f(acc), acc)
#plt.xlim(1, 3) 
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.show()

##################################################
# subplot example
##################################################

# import matplotlib.pyplot as plt
# import numpy as np

# np.random.seed(19680801)
# data = np.random.randn(2, 100)

# fig, axs = plt.subplots(2, 2, figsize=(5, 5))
# axs[0, 0].hist(data[0])
# axs[1, 0].scatter(data[0], data[1])
# axs[0, 1].plot(data[0], data[1])
# axs[1, 1].hist2d(data[0], data[1])

# plt.show()