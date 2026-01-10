import gradio as gr
from src.rag import generate_answer


def ask_question(user_query):
    """
    Handles user interaction:
    - Runs RAG pipeline
    - Formats answer and sources
    """
    if not user_query.strip():
        return "Please enter a question.", ""

    answer, docs = generate_answer(user_query)

    # Format sources
    sources_text = ""
    for i, doc in enumerate(docs, 1):
        sources_text += f"\n--- Source {i} ---\n"
        sources_text += doc.page_content[:300] + "\n"
        sources_text += f"Metadata: {doc.metadata}\n"

    return answer, sources_text


with gr.Blocks(title="Intelligent Complaint Analysis") as demo:
    gr.Markdown("# 🏦 Intelligent Complaint Analysis System")
    gr.Markdown(
        "Ask a question about consumer financial complaints. "
        "The AI will answer using real complaint data."
    )

    with gr.Row():
        question_input = gr.Textbox(
            label="Your Question",
            placeholder="e.g. Why are customers complaining about unauthorized credit card charges?",
            lines=2
        )

    with gr.Row():
        submit_btn = gr.Button("Ask")
        clear_btn = gr.Button("Clear")

    answer_output = gr.Textbox(
        label="AI Answer",
        lines=6
    )

    sources_output = gr.Textbox(
        label="Sources Used",
        lines=12
    )

    submit_btn.click(
        fn=ask_question,
        inputs=question_input,
        outputs=[answer_output, sources_output]
    )

    clear_btn.click(
        fn=lambda: ("", "", ""),
        outputs=[question_input, answer_output, sources_output]
    )


if __name__ == "__main__":
    demo.launch()
