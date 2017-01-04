from histogram_hash import *
import matplotlib.pyplot as plt

if __name__ == '__main__':
    num_bins = 16

    # result = histogram_matrix("data/red.jpg", num_bins=num_bins)
    # result = histogram_matrix("data/green.jpg", num_bins=num_bins)
    # result = histogram_matrix("data/blue.jpg", num_bins=num_bins)
    result = histogram_matrix("data/lake.jpg", num_bins=num_bins)
    result_corrupted = histogram_matrix("data/lakeCorrupted.jpg", num_bins=num_bins)

    hash_result = histogram_hash(result, 32*32)
    hash_result_corrupted = histogram_hash(result_corrupted, 32 * 32)
    print(hash_result)
    print(hash_result_corrupted)
    print(hamming_distance(hash_result, hash_result_corrupted))

    color = ('b', 'g', 'r')
    fig = plt.figure()

    for i, col in enumerate(color):
        ax1 = fig.add_subplot(131+i)
        histr = result[i]
        hist_array = histr.T[0].astype(int)
        plt.bar(range(num_bins), result[i], 0.66, color=col, alpha=0.8)
        plt.xlim([0, num_bins])
        plt.xlabel(col.upper() + " Band")
        plt.ylabel("Frequency")
    plt.tight_layout()
    fig = plt.gcf()
    plt.show()
