import streamlit as st
import utils
import main_v2 as backend


# Page configuration -----
st.set_page_config(
    page_title="Youtube Video Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- Custom CSS for the Footer ---
# This CSS will fix the footer to the bottom of the page
footer_style = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #0E1117; /* Streamlit's dark theme background color */
    color: #FAFAFA; /* Streamlit's primary text color */
    text-align: center;
    padding: 10px;
    border-top: 1px solid #262730; /* A subtle top border */
}
</style>
"""
st.markdown(footer_style, unsafe_allow_html=True)

# app title ----
st.markdown("<h1 style='color: #D70040;'>▶️ YouTube Video Assistant</h1>", unsafe_allow_html=True)
st.write("Ask questions about any Youtube video with English.....")

# Session state initialization --- 
# This is crucial to maintain state across user interface
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None
if "video_processed" not in st.session_state:
    st.session_state.video_processed = False
if "error_message" not in st.session_state:
    st.session_state.error_message = None

# Main IU for the logic
youtube_url = st.text_input("Enter Youtube URL: ", key="youtube_url_input")
if youtube_url:
    video_id = utils.get_youtube_video_id(youtube_url)

    if video_id is None:
        st.error("Invalid YouTube URL. Please enter a valid URL.")
        # Reset store if URL is invalid
        st.session_state.video_processed = False
        st.session_state.rag_chain = None
        st.session_state.chat_history = []

    else:
        # check if this video has already been processed to avoid reprocessing
        if "processed_video_id" not in st.session_state or st.session_state.processed_video_id != video_id:
            st.session_state.video_processed = False
            st.session_state.rag_chain = None
            st.session_state.chat_history = []
            st.session_state.error_message = None

            with st.status("Processing Video...", expanded=True) as status:
                st.write("✅ URL is valid. Extracting transcript...")
                retriver = backend.process_video_transcript(video_id)

                if retriver:
                    st.write("🧠 Building knowledge base...")
                    st.session_state.rag_chain = backend.create_rag_chain(retrivers=retriver)
                    st.session_state.video_processed = True
                    st.session_state.processed_video_id = video_id
                    status.update(label="Processing Complete! you can ask questions.", state="complete", expanded=False)
                else:
                    st.session_state.error_message = "Sorry, we can't help with this video"
                    status.update(label="Error", state="error", expanded=True)
                    st.error(st.session_state.error_message)


# main Interface style for Chat ---
if st.session_state.video_processed:
    st.success("Video Processed! Ask your question below....")

    # display previous chat messages
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # chat intput for the users
    if prompt := st.chat_input("Ask your question about this video...."):
        # add user message to history and display it 
        st.session_state.chat_history.append({"role":"user", "content":prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # get the assistant's response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.rag_chain.invoke(prompt)
                st.markdown(response)
        
        # add assistant message to history
        st.session_state.chat_history.append({"role":"assistant", "content":response})
elif st.session_state.error_message:
    st.error(st.session_state.error_message)
    pass


st.markdown("---")
st.markdown('<div class="footer">Built with ❤️ using Streamlit and LangChain.</div>', unsafe_allow_html=True)
