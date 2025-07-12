import gradio as gr

def get_states():
    import requests
    response = requests.get("http://localhost:8000/states")
    states = response.json()
    return [state["name"] for state in states]

states = get_states()

gr.Interface(title="US States", inputs=[gr.Dropdown(label="States", values=states)], outputs=gr.Text()).launch()
