# Web AI Agent

Welcome to the **Web AI Agent** repository! This project showcases an AI-powered web agent capable of operating a computer by autonomously opening a web browser, searching for information online, and summarizing the results. The project combines advanced AI frameworks and user-friendly frontend design to deliver an interactive experience.

![Banner](assets/image.png)
---

## Key Features

1. **Automated Web Browsing:** The AI agent can open a web browser, perform online searches, and retrieve relevant information autonomously.
2. **Summarization:** The agent processes the search results and provides concise summaries for easy understanding.


---

## Demo

Check out the demo video to see the Web AI Agent in action:

![Demo Video](<link to the demo video>)

---

## Installation

Follow these steps to set up the Web AI Agent on your local machine:



1. Clone the repository:
   ```bash
   git clone https://github.com/trojrobert/web_agent.git
   cd web_agent
   ```
2. Rename the `.env_dev` file to `.env` and add your OpenAI API key to the file.

3. Create a virtual environment with any tool of your choice. Ensure the python version is 3.12.5

4. Install the required dependencies with pip or poetry:
   ```bash
   pip install -r requirements.txt
   ```
   or
   ```bash
   poetry install
   ```
5. playwright install

6. Run the Streamlit application:
   ```bash
   streamlit run src/interface.py
   ```


4. Open your web browser and navigate to interact with the Web AI Agent.

---

## Usage

1. Launch the Streamlit application.
2. Enter a task (e.g., "Current Price of Nvidia Stock").
3. Click the "Run Task" button.
4. The AI agent will:
   - Open a web browser.
   - Search for your query online.
   - Summarize the results and display them on the interface.

---

## Project Structure

- **`src/`**: contains all the code for the project
- **`src/interface.py`**: The main entry point for the Streamlit application.
- **`src/agent/`**: Contains the implementation of the Web AI Agent using the Autogen framework.
- **`requirements.txt`**: List of dependencies required for the project.

---

## Technologies Used

- **Frontend:** [Streamlit](https://streamlit.io)
- **AI Framework:** [Autogen](https://github.com/microsoft/autogen)

---

## Contributing

Contributions are welcome! Feel free to fork the repository, create a new branch, and submit a pull request with your improvements or bug fixes.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

This project was developed by [John Robert](https://github.com/trojrobert).

---

## Feedback and Support

For any questions or feedback, please open an issue in this repository or contact the author directly.

Happy coding!

