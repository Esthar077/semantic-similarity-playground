
import streamlit as st
from similarity import calculate_similarity
from visualization import plot_similarity_angle
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Semantic Similarity Playground",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Semantic Similarity Playground")

st.write(
    "Ever wondered how AI understands two sentences "
    "with different words but similar meanings?"
)

st.write(
    "Enter two sentences and see how closely "
    "their embedding vectors align."
)

# User inputs
sentence_a = st.text_area(
    "Sentence A",
    value="How do I reset my password?"
)

sentence_b = st.text_area(
    "Sentence B",
    value="I forgot my login credentials."
)

# Calculate similarity
if sentence_a.strip() and sentence_b.strip():

    similarity, angle = calculate_similarity(
        sentence_a,
        sentence_b
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Cosine Similarity",
            f"{similarity:.4f}"
        )

    with col2:
        st.metric(
            "Angle Between Vectors",
            f"{angle:.2f}°"
        )

    st.info(
        "A smaller angle means the vectors point "
        "in more similar directions. This often "
        "indicates greater semantic similarity."
    )


    st.subheader("Visualizing the Similarity")

    fig = plot_similarity_angle(angle)

    st.pyplot(fig)

    # Release the figure after rendering
    plt.close(fig)

    st.caption(
        "This is a 2D illustration of the angle "
        "calculated from the actual 384-dimensional "
        "sentence embeddings. It is not a projection "
        "of the original vectors."
    )

else:
    st.warning("Please enter both sentences.")
