import random
import numpy as np
import matplotlib.pyplot as plt

arr = [2,5,10,30,50,100]


theo_var = []

exp_mean = []
exp_var = []

for n in arr:
    sample_mean = []
    for i in range(1000):
        sample = []
        for j in range(n):
            res = random.random()*10
            sample.append(res)
        mean = sum(sample)/n
        sample_mean.append(mean)

    fig, ax = plt.subplots()

    ax.hist(
        sample_mean,
        bins=30,
        range=(1, 10),
        density=True
    )

    mu = 5
    variance = 25 / (3 * n)
    sigma = np.sqrt(variance)

    x = np.linspace(1, 10, 500)

    normal_pdf = (
        1 / (sigma * np.sqrt(2 * np.pi))
        * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    )

    ax.plot(x, normal_pdf, linewidth=2)

    ax.set_xlabel("Sample Mean")
    ax.set_ylabel("Density")
    ax.set_title(f"Sampling Distribution of Sample Mean (n={n})")
    ax.set_xticks(range(1, 11))

    fig.savefig(
        f"uniform_n_{n}.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

    theo_var.append(25/(3*n))
    exp_mean.append(np.mean(sample_mean))
    exp_var.append(np.var(sample_mean))


for k in range(len(arr)):
    print(f"Value of n : {arr[k]} | Theoretical Mean : 5 | Experimental Mean : {np.array(exp_mean[k])} | Theoretical Variance : {np.array(theo_var[k])} | Experimental Variance : {np.array(exp_var[k])} \n")





