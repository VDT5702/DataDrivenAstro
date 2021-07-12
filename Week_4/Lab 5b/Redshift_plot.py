#Lab 5b Task5: Colour-colour redshift plot

import numpy as np
from matplotlib import pyplot as plt

# Complete the following to make the plot
if __name__ == "__main__":
    data = np.load('sdss_galaxy_colors.npy')
    
    # Get a colour map
    cmap = plt.get_cmap('YlOrRd')

    # Define our colour indexes u-g and r-i
    col_index_x=data['u']-data['g']
    col_index_y=data['r']-data['i']
    
    # Make a redshift array
    redshift_ar=data['redshift']
    
    # Create the plot with plt.scatter and plt.colorbar
    plt.scatter(col_index_x, col_index_y, s=1, c=redshift_ar, cmap='YlOrRd')
    plt.colorbar(label='Redshift')
    
    # Define your axis labels and plot title
    plt.xlabel('Colour index u-g')
    plt.ylabel('Colour index r-i')
    plt.title('Redshift (colour) u-g versus r-i')
    
    # Set any axis limits
    plt.xlim([-0.5,2.5])
    plt.ylim([-0.5,1])
    plt.show() 