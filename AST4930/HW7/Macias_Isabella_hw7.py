import numpy as np
from astropy import units as u 
from matplotlib import pyplot as plt

data = np.loadtxt("/home/maciasi/AST4930/HW7/sed.txt", delimiter= ',', skiprows=3)
print(data)

#separating the data
luminosity_data = data[:,1]
wavelength_data = data[:,0]

#plot
plt.plot(wavelength_data, luminosity_data)
plt.loglog(wavelength_data, luminosity_data)
plt.ylabel("Luminosity")
plt.xlabel("Wavelength")
plt.title("Wavelength vs Luminosity Plot")
plt.show()
plt.savefig("Macias_Isabella_HW7", dpi=300)

#setting bounds
lower_limit = np.where(wavelength_data <10)
print("10", lower_limit)

#units
wavelength_data *= u.micron
luminosity_data *= u.Lsun/u.micron

#integration
integral = (np.trapz(luminosity_data[0:833], x= -wavelength_data[0:833])).to(u.erg/u.s)
print("SED Integral:", integral)



