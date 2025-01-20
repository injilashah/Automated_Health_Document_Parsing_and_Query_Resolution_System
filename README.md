# Automated_Health_Document_Parsing_and_Query_Resolution_System

 

The system is designed to process medical documents that include both textual and visual data. It employs OCR to extract critical information from the documents. Utilizing the Ollama Llama 3.2 model, it facilitates query-based information retrieval, enabling users to ask questions and receive precise answers derived from the extracted content.

# DEMO
<div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
  <img src="demo/demo.png" alt="DEMO" style="width: 1000px; height: 460px; border-radius: 100%;">
</div>

# Running the System:
To run the system use the following commands:
'''bash
python -m pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py


 




