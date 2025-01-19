import os
import gradio as gr
from werkzeug.utils import secure_filename
from extract import extract_text_from_pdf
from generate import generate_answer

# Configure upload folder
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)



# Function to handle file upload, extraction, and JSON generation

import gradio as gr

# Function to extract text from uploaded file
def process_file(file):
    if not file:
        return "No file uploaded!", None
    
    # file is already a file path when type="filepath"
    filepath = file  # 'file' is a path to the uploaded PDF file

    # Extract text from the PDF
    extracted_text = extract_text_from_pdf(filepath)
    
    

    # Return extracted text and generated answer
    return extracted_text

# Function to process query and generate output
def generate_text(query, extracted_text):
    if not query or not extracted_text:
        return "No query or extracted text provided!"
    prompt = f"Given the medical record: \n{extracted_text} \nanswer: \n{query}"
    
    # Generate JSON using the LLM
    answer = generate_answer(prompt)

    # Return extracted text and generated answer
    return answer

# Gradio Interface

with gr.Blocks() as demo:
    gr.Markdown("<h1 style='text-align: center;'>Medical Document Parser</h1>")
    with gr.Row():  # Create two columns
        # First column
        with gr.Column():
            file_input = gr.File(label="Upload Your Medical Report", type="filepath", file_types=[".pdf"])
            extracted_output = gr.Textbox(label="Extracted Text", lines=10, interactive=False)
            # Extracted text will be updated upon file upload
            file_input.change(process_file, inputs=file_input, outputs=extracted_output)

        # Second column
        with gr.Column():
            query_input = gr.Textbox(label="Enter Your Query")
            query_output = gr.Textbox(label="Generated Answer", lines=10, interactive=False)
            # Generated answer will be updated upon query submission
            query_input.submit(
                generate_text,
                inputs=[query_input, extracted_output],
                outputs=query_output
            )

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch(debug = True)

