# CodeRoaster

CodeRoaster, where code meets humor! 🚀

CodeRoaster is a web application that analyzes and roasts code snippets, providing a touch of humor and insightful critiques. Whether you're a seasoned developer or a coding enthusiast, CodeRoaster is here to add a bit of fun to your coding journey.

## Features

- **Roasting Expertise:** Let CodeRoaster analyze your code and deliver a humorous and insightful roast.
- **Language Agnostic:** CodeRoaster supports various programming languages. Bring on your Python, JavaScript, Java, and more!
- **Output Representation:** CodeRoaster allows you to select you preferred output representation - either Markdown or code-like comments!
  
## Technologies Used

- **Backend:** Flask (Python)
- **Frontend:** React with Vite
- **Other Technologies:** LangChain (Using mainly [openchat-3.5-0106](https://huggingface.co/openchat/openchat-3.5-0106) for chains)

## Getting Started

Follow these steps to run CodeRoaster locally:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/djordje34/PY-Code-Roaster.git
    cd PY-Code-Roaster
    ```
   
2. **Set up Python virtual environment:**
    ```bash
    python -m venv $envname
    source $envname/bin/activate
    ```
    
3. **Install Python dependencies:**
    ```py
    pip install -r requirements.txt
    ```
4. **Install React dependencies:**
    ```bash
    cd frontend
    npm install
    ```
5. **Run the backend:**
    ```bash
    cd backend
    flask run
    ```
6. **Run the frontend:**
    ```bash
    cd frontend
    npm run dev
    ```
