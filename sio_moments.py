"""
Loops over a pre-defined velocity range to generate integrated intensity maps.
"""

from astropy import units as u
from spectral_cube import SpectralCube

file            = 'C_SiO_full_field_K.fits'
mol             = 'SiO'
v_start         = -110
v_end           = 190
cube            = SpectralCube.read(file)
cube            = cube.with_mask(cube > 0*u.K)

i = 0
v = v_start
while v <= v_end:
    subcube         = cube.spectral_slab(v*u.km/u.s, (v+10)*u.km/u.s)
    mom0            = subcube.moment(order=0)
    mom0.write('./Moments/'+mol+'_mom0_'+str(v)+'_to_'+str((v+10))+'.fits',
                overwrite=True)

    v = v + 10
    i = i + 1
