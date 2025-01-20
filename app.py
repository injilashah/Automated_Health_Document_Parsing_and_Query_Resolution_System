import os
import gradio as gr
from werkzeug.utils import secure_filename
from extract import extract_text_from_pdf
from generate import generate_answer


UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)





import gradio as gr


def process_file(file):
    if not file:
        return "No file uploaded!", None

    filepath = file 

    # Extract text from the PDF
    extracted_text = extract_text_from_pdf(filepath)
    
    

    # Return extracted text and generated answer
    return extracted_text

# Function to process query and generate output
def generate_text(query, extracted_text):
    if not query or not extracted_text:
        return "No query or extracted text provided!"
    prompt = f"Given the medical record: \n{extracted_text} \nanswer: \n{query}"
    
   
    answer = generate_answer(prompt)

   
    return answer

# Gradio Interface

with gr.Blocks() as demo:
    gr.Markdown("<h1 style='text-align: center;'>Medical Document Parser</h1>")
    with gr.Row():  # Create two columns
        # First column
        with gr.Column():
            file_input = gr.File(label="Upload Your Medical Report", type="filepath", file_types=[".pdf"])
            
            extracted_output = gr.Textbox(label="Extracted Text", lines=10, interactive=False)
           
            file_input.change(process_file, inputs=file_input, outputs=extracted_output)

        # Second column
        with gr.Column():
            query_input = gr.Textbox(label="Enter Your Query")
            query_output = gr.Textbox(label="Generated Answer", lines=10, interactive=False)
            query_input.submit(
                generate_text,
                inputs=[query_input, extracted_output],
                outputs=query_output )

# Launch the  app
if __name__ == "__main__":
    demo.launch(debug = True)

