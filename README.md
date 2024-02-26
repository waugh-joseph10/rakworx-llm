# rakworx-llm
LLM using Llama2 and Embeddings for Rakworx product details.

## Setup

### Clone the Repository

First, clone the repo using the GitHub CLI:

```bash
git clone https://github.com/waugh-joseph10/rakworx-llm.git
```

### Download the Llama2-13B Model
Run the following command from CMD to save the LLama2-13B chat GGUF file to the local folder:

```bash
curl -L "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/blob/main/llama-2-13b-chat.Q4_K_M.gguf" -o llama-2-13b-chat.Q4_K_M.gguf
```
### Create a Virtual Environment
To isolate and manage the project's dependencies, create a virtual environment in the project directory:

```bash
python -m venv venv
```

### Activate the Virtual Environment
On Windows:
```bash
.\venv\Scripts\activate
```

On macOS and Linux:

```bash
source venv/bin/activate
```

### Installing Dependencies
With the virtual environment actiated, install the required dependencies:

```bash
pip install -r requirements.txt
```

### Run the Application
Finally, you can run `python test.py` to initiate the chat bot:

```bash
python test.py
```