import folium
import pandas as pd
print(dir(folium))

map = folium.Map(location=[40.897934, -73.885948], zoom_start = 7)
df = pd.read_csv('Volcanoes.txt')

for lat,lon,name,elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    folium.Marker(location=[lat, lon], popup=name, icon = folium.Icon(color='green' if elev in range(0,1000) else 'orange' if elev in range(1001,1999) else 'blue' if elev in range(2000,2999) else 'red', icon='cloud')).add_to(map)



# folium.Marker(location = [40.897934, -73.885948], popup='I am lost please help...', icon = folium.Icon(icon= 'cloud')).add_to(map)
# folium.Marker(location = [40.897934, -73.9015249], popup='But I can see you', icon = folium.Icon(color= 'green')).add_to(map)


print(dir(folium.Map))
print(map.save('test2.html'))
