import matplotlib.pyplot as plt


def main(output_file: str):
    # Data to plot
    labels = "MVK", "Ours", "vimeo", "shutterstock"
    sizes = [1378, 1365, 8405, 171835]
    colors = ["gold", "yellowgreen", "lightcoral", "lightskyblue"]
    explode = (0.1, 0, 0, 0)  # explode 1st slice

    # Custom function to display both number and percentage
    def autopct_format(values):
        def my_format(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return f"{pct:.1f}%)"

        return my_format

    # Plot
    fig, ax = plt.subplots(figsize=(6, 6))  # Adjust the figsize to reduce whitespace
    ax.pie(
        sizes,
        explode=explode,
        labels=labels,
        colors=colors,
        autopct=autopct_format(sizes),
        shadow=True,
        startangle=140,
    )

    ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.tight_layout()  # Adjusts the padding between and around subplots
    plt.savefig(output_file)


if __name__ == "__main__":
    output_file = "figures/source_distribution.png"
    main(output_file)
