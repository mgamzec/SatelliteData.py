from pystac_client import Client
from odc.stac import load
import matplotlib.pyplot as plt

client = Client.open("http://earth-search.aws.element84.com/v1")
collection = "sentinel-2-l2a"
ant_bbox = [30.444946, 36.804887, 30.933837, 37.059561]
search = client.search(collections=[collection], bbox=ant_bbox, datetime="2023-12")

data = load(search.items(), bbox=ant_bbox, groupby="solar_day", chunks={})

data_slice = data.isel(time=0)

# Plotting the "red," "green," and "blue" bands individually
plt.figure(figsize=(12, 4))
plt.subplot(131)
data_slice["red"].plot.imshow(robust=True)
plt.title("Red Band")
plt.subplot(132)
data_slice["green"].plot.imshow(robust=True)
plt.title("Green Band")
plt.subplot(133)
data_slice["blue"].plot.imshow(robust=True)
plt.title("Blue Band")
plt.show()
