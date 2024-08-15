import folium
import pandas

class PlotFolium:
    def __init__(self, dataframe, routes):
        self.dataframe = dataframe
        self.routes = routes

    def mapping(self):
        filtered_routes = [route for route in self.routes if len(route) > 2]
        routes_coordinates = {}
        for i, route in enumerate(filtered_routes):
            coordinates = []
            for path in route:
                coordinates.append([self.dataframe.iloc[path]['lat'], self.dataframe.iloc[path]['lon']])
            routes_coordinates[i] = coordinates
        
        return routes_coordinates
    
    def starter(self, zoom, map_name):
        map_center = [self.dataframe['lat'].mean(), self.dataframe['lon'].mean()]
        custom = "cartodb positron"
        self.map = folium.Map(location=map_center, zoom_start=zoom, tiles=custom)

        # Save the initial map
        self.map_name = f"./maps/{map_name}.html"
        self.map.save(self.map_name)

    def add_marker(self):
        destination = self.dataframe.drop(index=0)

        for _, row in destination.iterrows():
            folium.Circle(
                location=[row['lat'], row['lon']],
                radius=10000,  # Radius in pixels
                color='red',
                fill=True,
                fill_color='red',
                fill_opacity=0.6,
                tooltip=row['name'],
            ).add_to(self.map)

        folium.Circle(
            location=[self.dataframe.iloc[0]['lat'], self.dataframe.iloc[0]['lon']],
            radius=10000,  # Radius in pixels
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6,
            tooltip=self.dataframe.iloc[0]['name']
        ).add_to(self.map)

        # Save the updated map
        self.map.save(self.map_name)
    
    def add_polyline(self):
        routes_coordinates = self.mapping()

        for i, coordinates in routes_coordinates.items():
            color = "#ff6f00" if i == 0 else "#5B99C2"
            folium.PolyLine(
                locations=coordinates,
                color=color,
                weight=1,
                tooltip="TSP"
            ).add_to(self.map)

        # Save the final map
        self.map.save(self.map_name)
