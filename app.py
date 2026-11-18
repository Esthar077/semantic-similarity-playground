
import io

import matplotlib.pyplot as plt
import streamlit as st

from similarity import calculate_similarity
from visualization import plot_similarity_angle


st.set_page_config(
    page_title="Semantic Similarity Playground",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Reduce unnecessary vertical spacing
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1rem;
        max-width: 1400px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧠 Semantic Similarity Playground")

st.caption(
    "Discover how AI compares the meaning of two sentences "
    "using embeddings and cosine similarity."
)

st.divider()

# Two-column layout
left_col, right_col = st.columns(
    [1, 1.1],
    gap="large",
    vertical_alignment="top"
)

with left_col:
    st.subheader("Compare Sentences")

    sentence_a = st.text_area(
        "Sentence A",
        value="How do I reset my password?",
        height=80
    )

    sentence_b = st.text_area(
        "Sentence B",
        value="I forgot my login credentials.",
        height=80
    )

    if sentence_a.strip() and sentence_b.strip():

        similarity, angle = calculate_similarity(
            sentence_a,
            sentence_b
        )

        metric_col1, metric_col2 = st.columns(2)

        with metric_col1:
            st.metric(
                "Cosine Similarity",
                f"{similarity:.4f}"
            )

        with metric_col2:
            st.metric(
                "Angle Between Vectors",
                f"{angle:.2f}°"
            )

        st.info(
            "A smaller angle indicates that the embedding "
            "vectors point in more similar directions. "
            "This often suggests greater semantic similarity."
        )

    else:
        similarity = None
        angle = None

        st.warning("Please enter both sentences.")


with right_col:
    st.subheader("Vector Visualization")

    if angle is not None:

        fig = plot_similarity_angle(angle)

        # Display the graph
        st.pyplot(fig, width="stretch")

        # Export graph as PNG
        image_buffer = io.BytesIO()

        fig.savefig(
            image_buffer,
            format="png",
            dpi=200,
            bbox_inches="tight",
            facecolor="white"
        )

        image_buffer.seek(0)

        st.download_button(
            label="📥 Download Graph as PNG",
            data=image_buffer.getvalue(),
            file_name="semantic_similarity_graph.png",
            mime="image/png",
            use_container_width=True
        )

        plt.close(fig)

        st.caption(
            "The graph illustrates the angle calculated "
            "from the actual 384-dimensional embeddings. "
            "It is not a 2D projection of those vectors."
        )

    else:
        st.info(
            "Enter two sentences to generate the graph."
        )
