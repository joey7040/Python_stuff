import folium
import pandas as pd
print(dir(folium))

df = pd.read_csv('Volcanoes.txt')


latmean = df['LAT'].mean()
lonmean = df['LON'].mean()


map = folium.Map(location=[latmean, lonmean], zoom_start = 7)


def color(elev):
    if elev in range(0,1000):
        col = 'green'
    elif elev in range(1000,1999):
        col = "blue"
    elif elev in range(2000,2999):
        col = "orange"
    else:
        col = 'red'
    return col


for lat,lon,name,elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    folium.Marker(location=[lat, lon], popup=name, icon = folium.Icon(color = color(elev), icon = 'cloud')).add_to(map)


# folium.Marker(location = [40.897934, -73.885948], popup='I am lost please help...', icon = folium.Icon(icon= 'cloud')).add_to(map)
# folium.Marker(location = [40.897934, -73.9015249], popup='But I can see you', icon = folium.Icon(color= 'green')).add_to(map)


print(dir(folium.Map))
print(map.save('test2.html'))
