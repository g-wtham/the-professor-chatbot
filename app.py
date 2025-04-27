from flask import Flask, request, render_template
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

app = Flask(__name__, template_folder='templates', static_folder='assets')

def explanation_level(slider_input):
    if slider_input == 1:
        return "Explain this as if you're talking to a 5-year-old child. Use simple words, short sentences, and fun comparisons to things they already know. Avoid technical terms completely, and focus on making the concept friendly."
    elif slider_input == 2:
        return "Provide a simplified explanation suitable for beginners with no background knowledge. Use everyday language, clear analogies that connect to common experiences. Introduce only the most essential concepts, and explain any necessary terminology in straightforward terms."
    elif slider_input == 3:
        return "Explain this at an intermediate level with moderate technical detail. Balance accessibility with accuracy by introducing key technical concepts and terms (with explanations)."
    elif slider_input == 4:
        return "Provide an advanced explanation appropriate for someone with solid background knowledge in this field. Include specific technical terminology, underlying principles, and nuanced details. Discuss relationships between concepts, edge cases, and real-world applications. Use precise language while still being thorough in your explanations."
    elif slider_input == 5:
        return "Explain this at an expert level with comprehensive technical detail. Assume specialized knowledge in this field, use precise technical vocabulary without simplification, discuss underlying mechanisms and theoretical frameworks, address complexities and exceptions, reference relevant academic concepts, and explore advanced implications and applications."

def example_level(slider_input):
    if slider_input == 1:
        return "Based on this explanation, provide a simple, concrete example that a young child would understand. Use colorful, familiar scenarios with characters or objects they recognize. Make the example fun, visual, and interactive if possible. Avoid any complexity or abstraction."
        
    elif slider_input == 2:
        return "Based on this explanation, provide an everyday example that a beginner would recognize. Use common situations or objects from daily life to illustrate the concept clearly. Keep the example straightforward with minimal variables or complications."
        
    elif slider_input == 3:
        return "Based on this explanation, provide a practical example that demonstrates the concept in action. Balance simplicity with some meaningful detail. Include relevant context that shows how this applies in a real-world scenario that someone with general knowledge would appreciate."
        
    elif slider_input == 4:
        return "Based on this explanation, provide a detailed example that demonstrates the concept's application in a specific context. Include relevant technical parameters, show cause-and-effect relationships, and illustrate how this works in practice for someone with subject knowledge. You may include simplified code, formulas, or technical specifications if applicable."
        
    elif slider_input == 5:
        return "Based on this explanation, provide a sophisticated example that fully demonstrates the technical complexity of this concept. Include specific technical parameters, edge cases, or limitations. You may incorporate actual code, formulas, technical diagrams, or industry-standard applications. The example should be precise enough for expert implementation or analysis."

@app.route("/")
def index():
    return render_template("index.html", slider_value=3)

@app.route("/submit", methods=['POST'])
def submit():
    query = request.form['query'].strip()
    if not query:
        return render_template("index.html", explanation="Please enter some question before pressing EXPLAIN :)", example="")
    slider_value = int(request.form.get("slider", 3))
    
    explanation_level_prompt = explanation_level(slider_value)
    example_level_prompt = example_level(slider_value)
    
    model = genai.GenerativeModel("gemini-2.0-flash")
    query_response = model.generate_content(f"Don't use bold. Query: {query} - {explanation_level_prompt}")
    query_example = model.generate_content(f"Don't use bold. {query_response.text} - {example_level_prompt}")
    
    return render_template("index.html", explanation=query_response.text, example=query_example.text, slider_value=slider_value)

# return f"Your query has been received: {response.text}"
# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Write a story about a magic backpack.")
# print(response.text)

if __name__ == '__main__':
    app.run()