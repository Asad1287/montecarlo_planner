import matplotlib.pyplot as plt
def chart_output(results,save_location=".",chart_title="chart"):
 # Create the PDF and CDF
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.hist(results, bins=50, density=True, alpha=0.6, color='b', label='PDF')
    plt.title('Probability Density Function (PDF)')
    plt.xlabel('Result')
    plt.ylabel('Frequency')

    plt.subplot(1, 2, 2)
    plt.hist(results, bins=50, density=True, alpha=0.6, color='b', cumulative=True, label='CDF')
    plt.title('Cumulative Distribution Function (CDF)')
    plt.xlabel('Result')
    plt.ylabel('Frequency')
    plt.savefig(f"{save_location}/{chart_title}.png")
    plt.show()