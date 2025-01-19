
import subprocess

# Function to call Ollama and get structured output
def generate_answer(prompt):
   

    # Run the Ollama model and get the result

    
    try:
        result = subprocess.run(
            [ 'ollama','run', 'llama3.2'],input = prompt,
            capture_output=True, text=True, shell=True, check=True
        )
        
        print("Ollama Output:", result.stdout)  # Debugging: print the output from Ollama
        result =result.stdout
        return result
    except subprocess.CalledProcessError as e:
        print("Error during subprocess execution:", e.stderr)
        return {"error": "Failed to execute Ollama subprocess"}
    



