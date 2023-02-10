
# This is our simulation of the database
# We have two products here.
# The students must create their own productList when working on their eCommerce site
# Product images are loaded into static/images/product-images/
# Done in array instead of dictionaries to portray the differences
productList = [['1', 'Travel Scope', 'Celestron', 'description', 'Refractor', 'Altazimutal', '70', '400', 'TravelScope.png', '5', 'Active', '86', '86'],

            ['2', 'Astromaster', 'Celestron', 'description', 'Reflector', 'Ecuatorial', '130', '650', 'AstroMaster.png', '3', 'Active', '300', '300'],

            ['3', 'Advanced VX', 'Celestron', 'description', 'Catadioptrico', 'Ecuatorial', '235', '2359', 'AdvancedVX.jpg', '1', 'Active', '3,699', '3,699'],

            ['4', 'Skyscanner 10012', 'Orion', 'description', 'Reflector', 'Altazimutal', '100', '400', 'Skyscanner.jpg', '2', 'Active', '130', '130'],

            ['5', 'Maksutov-Cassegrain Starmax', 'Orion', 'description', 'Catadioptrico', 'Altazimutal', '90', '1250', 'Starmax.jpg', '1', 'Active', '180', '180'],

            ['6', 'Astroview  9024', 'Orion', 'description', 'Refractor', 'Ecuatorial', '90', '910', 'AstroView.jpg', '4', 'Active', '250', '250']]


def getProductsModel():
    return productList


def getBrandsModel():
    # Simulating grabbing these filters via SQL from the database
    brands = ["Celestron", "Orion"]
    return brands

def getMountModel():
    Mount = ['Altazimutual', 'Ecuatorial']
    return Mount


def getFocalDistanceModel():
    FocalDistance = ['400', '650', '2350', '1250', '910']
    return FocalDistance


def getApertureModel():
    Aperture = ['70', '90', '100', '130', '235']
    return Aperture

def getTipeModel():
    Model = ['Reflector', 'Refractor']
    return Model
