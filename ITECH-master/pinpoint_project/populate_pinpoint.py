import os



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pinpoint_project.settings')



import django



import static.images







django.setup()







from pinpoint.models import Destination











def read_file(fileName):



    fileName = "static/Descriptions/" + fileName



    file = open(fileName,'r',encoding='utf-8', errors='ignore')



    text = file.read()



    file.close()



    return text



def populate():

    

    print('Adding Islands...')

    add_island('Iceland','Europe',read_file("iceland.txt"),"../../static/images/iceland.jpg", 64.9631, 19.0208, 'cold', '_££_', "outdoors nightlife ", "https://forecast7.com/en/64d13n21d82/reykjavik/")

    add_island('Galapagos', 'Americas', read_file("galapagos.txt"),"../../static/images/galapagos.jpg", -0.757951, -91.120064, 'sunny', '_£££_', "outdoors beach","https://forecast7.com/en/n0d95n90d97/galapagos-islands/")

    add_island('Hong Kong', 'Asia', read_file("hongkong.txt"),"../../static/images/hongkong.jpg", 22.28552, 114.15769 , 'sunny', '_££_', "nightlife culture ", "https://forecast7.com/en/22d40114d11/hong-kong/")

    add_island('Isle of Skye', 'Europe', read_file("isleofskye.txt"),"../../static/images/isleofskye.jpg", 57.610708, -6.171944, 'mild', '_£_', "outdoors", "https://forecast7.com/en/57d41n6d20/portree/")

    add_island('Malta', 'Europe', read_file("malta.txt"),"../../static/images/malta.jpg", 35.9375, 14.3754, 'sunny', '_££_', "culture beach", "https://forecast7.com/en/35d9414d38/malta/")

    add_island('Mauritius', 'Africa', read_file("mauritius.txt"),"../../static/images/mauritius.jpg", -20.434121, 57.457160, 'sunny', '_£££_', "outdoors beach", "https://forecast7.com/en/n20d3557d55/mauritius/")

    add_island('Raja Ampat', 'Asia', read_file("rajaampat.txt"),"../../static/images/rajaampat.jpg", 0.167419, 130.040467, 'sunny', '_£_', "sports beach outdoors", "https://forecast7.com/en/n1d09130d88/raja-ampat-regency/")

    add_island('St. Lucia', 'Americas', read_file("stlucia.txt"),"../../static/images/stlucia.jpg", 13.950665, -61.036044, 'sunny', '_£££_', "sports beach outdoors", "https://forecast7.com/en/13d91n60d98/saint-lucia/")

    add_island('Svalbard', 'Europe', read_file("svalbard.txt"),"../../static/images/svalbard.jpg", -79.004959, 17.666016, 'cold', '_££_', "outdoors sports", "https://forecast7.com/en/77d8720d98/svalbard/")

    add_island('Sri Lanka', 'Asia', read_file("srilanka.txt"),"../../static/images/srilanka.jpg", 78.583161, 15.217368,  'sunny', '_£_', "culture outdoors beach", "https://forecast7.com/en/7d8780d77/sri-lanka/")

    print('Done! All Islands added.')


def add_island(name, location, description, image, long, lat, climate, budget, activities, weather):



    c = Destination.objects.get_or_create(name=name, location=location,



                                          description=description, image=image,



                                          long=long, lat=lat,



                                          climate=climate,



                                          budget=budget,



                                          activities=activities, weather=weather)[0]



    c.save()



    return c



















if __name__ == '__main__':



    print("Starting Pinpoint population script...")



    populate()