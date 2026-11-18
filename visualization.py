
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc


def plot_similarity_angle(angle):
    theta = np.radians(angle)

    vector_a = np.array([1.0, 0.0])
    vector_b = np.array([
        np.cos(theta),
        np.sin(theta)
    ])

    # Compact, landscape-oriented figure
    fig, ax = plt.subplots(figsize=(7, 2.8))

    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    # Draw vectors
    ax.annotate(
        "",
        xy=vector_a,
        xytext=(0, 0),
        arrowprops=dict(
            arrowstyle="-|>",
            color="#16a34a",
            lw=2.5,
            mutation_scale=18
        )
    )

    ax.annotate(
        "",
        xy=vector_b,
        xytext=(0, 0),
        arrowprops=dict(
            arrowstyle="-|>",
            color="#2563eb",
            lw=2.5,
            mutation_scale=18
        )
    )

    # Angle arc
    arc = Arc(
        (0, 0),
        width=0.55,
        height=0.55,
        theta1=0,
        theta2=angle,
        linestyle="--",
        color="#64748b",
        linewidth=1.5
    )

    ax.add_patch(arc)

    # Angle label
    midpoint = theta / 2

    ax.text(
        0.42 * np.cos(midpoint),
        0.42 * np.sin(midpoint),
        f"{angle:.1f}°",
        fontsize=11,
        color="#334155",
        ha="center",
        va="center"
    )

    # Labels
    ax.text(
        vector_a[0] + 0.05,
        vector_a[1],
        "Sentence A",
        fontsize=10,
        color="#16a34a"
    )

    ax.text(
        vector_b[0] + 0.05,
        vector_b[1] + 0.04,
        "Sentence B",
        fontsize=10,
        color="#2563eb"
    )

    # Keep equal scaling for accurate angles
    ax.set_aspect("equal", adjustable="box")

    # Compact plot area
    ax.set_xlim(-1.15, 1.55)
    ax.set_ylim(-1.15, 1.15)

        
    # Restore coordinate axes
    ax.set_axis_on()

    # Light grid lines
    ax.grid(
        True,
        color="#CBD5E1",
        linestyle="-",
        linewidth=0.7,
        alpha=0.5
    )

    # Display X and Y axes through the origin
    ax.axhline(
        0,
        color="#94A3B8",
        linewidth=1.0,
        alpha=0.8
    )

    ax.axvline(
        0,
        color="#94A3B8",
        linewidth=1.0,
        alpha=0.8
    )

    # Restore plot border
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color("#94A3B8")
        spine.set_linewidth(0.9)

    # Coordinate ticks
    ax.set_xticks(np.arange(-1.0, 1.6, 0.5))
    ax.set_yticks(np.arange(-1.0, 1.6, 0.5))

    ax.tick_params(
        axis="both",
        labelsize=8,
        colors="#64748B",
        length=3
    )

    # Keep grid behind vectors
    ax.set_axisbelow(True)

    fig.subplots_adjust(
        left=0.02,
        right=0.98,
        top=0.98,
        bottom=0.02
    )

    return fig