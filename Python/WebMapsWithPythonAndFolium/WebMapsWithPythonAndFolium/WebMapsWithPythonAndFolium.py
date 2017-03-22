import folium 

map = folium.Map(location = [45.372,-121.697] , zoom_start = 12, tiles = "Stamen Terrain")

map.simple_marker(location = [45.3288,-121.6625], popup = "Bertug'nun yeri",marker_color = "red")

map.simple_marker(location = [45.311,-121.7311], popup = "Mete's Place", marker_color = "green")

map.save("test.html")
