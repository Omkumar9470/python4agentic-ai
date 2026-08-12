import streamlit as st

from config  import GEMINI_API_KEY, COMMANDS
from memory  import ConversationMemory
from chat    import get_response_stream
from logger  import export_conversation

st.set_page_config(page_title="Aria — AI Engineering Tutor", page_icon="🎓", layout="centered")

if not GEMINI_API_KEY:
    st.error("⚠️ GEMINI_API_KEY not found. Add it to `.env` or Streamlit secrets.")
    st.stop()

if "memory" not in st.session_state:
    st.session_state.memory = ConversationMemory()
if "display_messages" not in st.session_state:
    st.session_state.display_messages = []
if "last_tool_call" not in st.session_state:
    st.session_state.last_tool_call = None
if "export_path" not in st.session_state:
    st.session_state.export_path = None

with st.sidebar:
    st.title("🎓 Aria")
    st.caption("Phase 2: LLM Engineering")
    st.divider()
    st.metric("Turns", st.session_state.memory.turn_count)
    st.caption(st.session_state.memory.summary())
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear", use_container_width=True):
            st.session_state.memory.clear()
            st.session_state.display_messages = []
            st.session_state.export_path = None
            st.rerun()
    with col2:
        if st.button("💾 Export", use_container_width=True,
                      disabled=len(st.session_state.memory.messages) == 0):
            st.session_state.export_path = export_conversation(
                st.session_state.memory.messages, st.session_state.memory.turn_count
            )

    if st.session_state.export_path:
        with open(st.session_state.export_path, "rb") as f:
            st.download_button("⬇️ Download chat log", f,
                                file_name=st.session_state.export_path.split("/")[-1],
                                mime="application/json", use_container_width=True)

st.title("Aria — AI Engineering Tutor")

for msg in st.session_state.display_messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])

if prompt := st.chat_input("Ask Aria anything..."):
    st.session_state.memory.add_user(prompt)
    st.session_state.display_messages.append({"role": "user", "text": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        tool_slot = st.empty()
        full_reply = st.write_stream(get_response_stream(st.session_state.memory))
        if st.session_state.last_tool_call:
            tool_slot.caption(f"🔧 used tool: `{st.session_state.last_tool_call}`")

    st.session_state.memory.add_model(full_reply)
    st.session_state.display_messages.append({"role": "assistant", "text": full_reply})
    st.rerun()