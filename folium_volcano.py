import folium
import pandas as pd
import io

# map=folium.Map(location=[12,77.744033],zoom_start=300,tiles="Mapbox Bright")
# fg=folium.FeatureGroup(name="Volcanoes")
# fg.add_child(folium.Marker(location=[12.9596,77.744033],popup="Hello",icon=folium.Icon(color="green")))
# map.add_child(fg)
# map.save("folium.html")
#
# print(map)

data=pd.read_csv("volcano.csv")

# print(data)
# print(type(data))

lon=list(data["Longitude"])
lat=list(data["Latitude"])
pei=list(data["PEI"])

def color_prod(elevation):
    if(elevation<3):
        return ("green")
    elif(3<=elevation<5):
        return ("orange")
    else:
        return ("red")

map=folium.Map(location=[32.58,-99.09],zoom_start=6,tiles="Mapbox Bright")
fgv=folium.FeatureGroup(name="Volcanoes")

for lt,ln,pe in zip(lat,lon,pei):
    print(pe,color_prod(pe))
    fgv.add_child(folium.Marker(location=[lt,ln],popup=str(pe)+"m",icon=folium.Icon(color=color_prod(pe))))

fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=io.open('world.json',r,encoding='utf-8-sig').read(),
                             style_function=lamda x:{'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 10000000<=x['properties']['POP2005'],20000000 else 'red'}))


map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save("map2.html")




