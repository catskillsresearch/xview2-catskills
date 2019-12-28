import glob

def disaster_images():
    return glob.glob('/home/catskills/Desktop/dataxv2/xBD/*/images/*_post_*.png')

if __name__=="__main__":
    print(disaster_images()[0:10])
