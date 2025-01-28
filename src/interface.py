import asyncio
import streamlit as st
from agents import run_multi_agent_task  # Import the agent logic
from utils import extract_sources_and_contents, parse_last_content

def main():
    # Set up Streamlit page configuration
    st.set_page_config(page_icon='assets/banner.png',
                page_title='Web Surfer AI Agent',
                initial_sidebar_state="auto",
                layout="centered")
    
    # st.set_page_config(page_title="Web Surfer AI Agent", layout="centered")
    st.image('/Users/robert/Projects/web_agent/assets/banner.png')

    # Initialize session state for tracking the task
    if "task_running" not in st.session_state:
        st.session_state.task_running = False
    if "result" not in st.session_state:
        st.session_state.result = None

    # st.title("Web AI Agent")
    st.markdown("This agent will browse the web, verify information, and summarize the results.")

    # Input: User task
    user_task = st.text_input(
        "Enter your task",
        disabled=st.session_state.task_running,
    )

    # Button: Run Task
    if st.button("Run Task", disabled=st.session_state.task_running):
        if not user_task.strip():
            st.error("Please enter a valid task.")
        else:
            st.session_state.task_running = True
            st.session_state.result = None

            with st.spinner("Agents are working on your task..."):
                try:
                    # Run the task asynchronously
                    result = asyncio.run(run_multi_agent_task(user_task))
                    formatted_result = parse_last_content(result)
                    st.session_state.result = formatted_result
                except Exception as e:
                    st.session_state.result = f"An error occurred: {e}"

            st.session_state.task_running = False

    # Display result if available
    if st.session_state.result is not None:
        if "error" in st.session_state.result.lower():
            st.error(st.session_state.result)
        else:
            st.success("Task completed!")
            st.markdown("### Result:")
            st.write(st.session_state.result)

        # Button to reset the interface
        if st.button("Run Another Task"):
            st.session_state.result = None
            st.session_state.task_running = False
            st.experimental_rerun()


if __name__ == "__main__":
    main()