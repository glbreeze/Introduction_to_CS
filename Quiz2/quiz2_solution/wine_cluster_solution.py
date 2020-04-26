import kmeans
import sample
import util
import mean_std_solution as mean_std


"""
1. read and process the data
2. read your data into an array of Sample class objects
3. apply k means to cluster the samples
"""

data = open("wine_data.txt", "r").readlines()
allSamples = [ ]
# IMPLEMENTATION: Read the data
# ---- start your code ---- #
pass
"""
fill the array allSamples to hold the samples, each sample
takes two attributes of an iris instance
"""
for line in data:
    content = line.strip().split(",")
    d = sample.Sample('', [float(content[1]), float(content[3])])
    allSamples.append(d)
# ---- end of your code --- #


verbose = False
k = 3
print("before clustering")
unclustered = [kmeans.Cluster(allSamples)]
util.plot_cluster(unclustered)

clusters = unclustered
print("after clustering")
# IMPLEMENTATION: apply k means to cluster the samples
# ---- start your code ---- #
pass
clusters = kmeans.kmeans(allSamples, 3, verbose)


# ---- end of your code --- #

util.plot_cluster(clusters, verbose)

""" bonus """
normalized_allSamples = allSamples
print("after normalizing")

# IMPLEMENTATION
# ---- start your code ---- #
pass
normalized_allSamples = mean_std.normalization(allSamples)
normalized_clusters = kmeans.kmeans(normalized_allSamples, 3, verbose)



# ---- end of your code --- #
util.plot_cluster(normalized_clusters, verbose)
