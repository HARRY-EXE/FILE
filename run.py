import platform,os
bit = platform.architecture()[0]
print(' CHECKING FOR UPDATES');os.system('git pull')
if bit == '32bit':
    import FILE32
elif bit == '64bit':
    import FILE64
else: exit(" SORRY YOUR DEVICE DOESN'T SUPPORT THIS TOOL USE 32/64 BIT PHONE");exit()
