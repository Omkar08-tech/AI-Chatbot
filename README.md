
# AI Chatbot with Phi-2 Model

This project implements an AI-powered chatbot using the **Phi-2** language model by Microsoft. The chatbot is designed to handle conversational interactions and can be integrated into various applications. It uses **Gradio** for the graphical user interface (GUI), allowing users to interact with the chatbot via a web interface.

## Features
- **Chatbot powered by Phi-2**: An advanced language model trained for general-purpose language tasks.
- **Gradio GUI**: Easy-to-use interface for interaction.
- **Modular design**: Code is organized into modules for ease of maintenance and extension.
- **Input handling**: User input is tokenized and processed using the Phi-2 model, generating human-like responses.
- **User-friendly interface**: The interface allows users to type messages and receive responses in real-time.

## Requirements

Install dependencies using pip:

```bash
pip install -r requirements.txt
```

Make sure your `requirements.txt` includes:

- transformers
- gradio
- torch

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/AI-Chatbot.git
cd AI-Chatbot
```

2. Run the chatbot:

```bash
python main.py
```

This will launch a Gradio interface in your browser where you can interact with the chatbot.

## Project Structure

- `chatbot.py` - Contains the chatbot model and response generation logic using Phi-2.
- `interface.py` - Defines the user interface using Gradio.
- `main.py` - Starts the application and initializes the chatbot and GUI.

## Contributing

Contributions are welcome! Fork the repository and submit a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).
