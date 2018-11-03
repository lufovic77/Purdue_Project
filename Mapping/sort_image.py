from operator import itemgetter, attrgetter

class Image(object):
    def __init__(self, filename, latitude, longitude) :
        self.filename = filename
        self.latitude = latitude
        self.longitude = longitude
    '''
    def __repr__(self) :
        return repr((self.filename, self.latitude, self.longitude))
    '''
if __name__ == "__main__" :

    image = [
        Image("A", 1, 2),
        Image("B", 2, 1),
        Image("C", 2, 3),
        Image("D", 1, 4),
        Image("E", 1, 3)
    ]

    sorted_image = sorted(image, key=attrgetter('latitude','longitude'))
    for index, n in enumerate(sorted_image) :
        sorted_image[index].filename = str(index)
        print(index, n)