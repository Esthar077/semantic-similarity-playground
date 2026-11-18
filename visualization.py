
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc


def plot_similarity_angle(angle):
    """Draw a 2D illustration of the angle between vectors."""

    theta = np.radians(angle)

    # Unit vectors with the requested angle between them
    vector_a = np.array([1.0, 0.0])
    vector_b = np.array([
        np.cos(theta),
        np.sin(theta)
    ])

    fig, ax = plt.subplots(figsize=(7, 5))

    # Draw both vectors
    ax.quiver(
        0, 0, *vector_a,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="#16a34a",
        width=0.008,
        label="Sentence A"
    )

    ax.quiver(
        0, 0, *vector_b,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="#2563eb",
        width=0.008,
        label="Sentence B"
    )

    # Draw angle arc
    arc = Arc(
        (0, 0),
        width=0.6,
        height=0.6,
        theta1=0,
        theta2=angle,
        color="gray",
        linestyle="--"
    )

    ax.add_patch(arc)

    # Label the angle
    midpoint = theta / 2

    ax.text(
        0.42 * np.cos(midpoint),
        0.42 * np.sin(midpoint),
        f"{angle:.1f}°",
        fontsize=12
    )

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect("equal")

    ax.axhline(0, color="gray", alpha=0.3)
    ax.axvline(0, color="gray", alpha=0.3)

    ax.grid(alpha=0.15)
    ax.legend(loc="upper right")

    ax.set_title("Cosine Similarity: Vector Angle")

    return fig
