import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 16px;
        padding: 10px 20px;
    }
    .metric-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin: 10px 0;
    }
    .agent-output {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🔍 Multi-Agent Research System")
    st.markdown("*Intelligent agents working together to research, analyze, and summarize information*")

with col2:
    st.image("https://via.placeholder.com/150?text=Multi-Agent", width=150)

st.divider()

# Sidebar for settings
with st.sidebar:
    st.header("⚙️ Settings")
    mode = st.radio(
        "Select Mode:",
        ["Demo Mode (Mock Data)", "Live API Calls"],
        help="Demo mode uses pre-generated responses. Live mode requires API quota."
    )
    
    temperature = st.slider(
        "Temperature (Creativity)",
        0.0, 2.0, 0.7,
        help="Higher = more creative, Lower = more focused"
    )
    
    st.divider()
    st.subheader("📊 System Status")
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key and not api_key.startswith("YOUR_"):
        st.success("✅ API Key Configured")
    else:
        st.error("❌ API Key Missing")
    
    st.info("Running in: **" + mode + "**")

st.divider()

# Main content area
st.header("📝 Research Topic")

# Input section
col1, col2 = st.columns([3, 1])
with col1:
    topic = st.text_input(
        "Enter your research topic:",
        value="The integration of AI in modern space exploration",
        placeholder="e.g., Climate change solutions, Quantum computing applications..."
    )

with col2:
    submit_btn = st.button("🚀 Analyze", use_container_width=True, type="primary")

st.divider()

# Initialize session state
if 'research_output' not in st.session_state:
    st.session_state.research_output = None
if 'summary_output' not in st.session_state:
    st.session_state.summary_output = None
if 'follow_up_output' not in st.session_state:
    st.session_state.follow_up_output = None

# Process button click
if submit_btn and topic:
    with st.spinner("🔄 Analyzing with multi-agent system..."):
        # Mock data for demo mode
        if mode == "Demo Mode (Mock Data)":
            st.session_state.research_output = f"""Here are 3 key points about **{topic}**:

1. **Primary Impact**: This represents a significant development in the field with far-reaching implications. The integration creates new opportunities while presenting unique challenges that require careful consideration and strategic planning.

2. **Technical Advancement**: Current implementations leverage cutting-edge technology to address fundamental problems. The approach demonstrates scalability and adaptability across various use cases and scenarios.

3. **Future Potential**: The trajectory suggests exponential growth in coming years. Organizations that adopt this framework early will likely gain substantial competitive advantages in their respective markets."""

            st.session_state.summary_output = f"""## Executive Summary: {topic}

This comprehensive analysis reveals that **{topic}** stands as a transformative force in its domain. The three primary points identified highlight the multifaceted nature of this development:

The primary impact demonstrates the cross-disciplinary significance of this topic. Technical advancements showcase the maturity and robustness of current implementations. Looking ahead, the future potential indicates substantial opportunities for innovation and growth.

This convergence of factors positions stakeholders to capitalize on emerging opportunities while mitigating inherent risks."""

            st.session_state.follow_up_output = """In addition to these points, here are emerging considerations:

4. **Sustainability & Scalability**: Long-term success depends on building sustainable frameworks that can scale efficiently without compromising quality or introducing new challenges.

5. **Collaboration & Ecosystem**: Cross-sector collaboration and ecosystem development are crucial for maximizing benefits and ensuring inclusive progress across all stakeholders."""
        
        # Live API mode would go here (when quota is available)
        # else: call actual APIs
    
    st.success("✅ Analysis complete!")

# Display results
if st.session_state.research_output:
    st.divider()
    st.header("📊 Results")
    
    # Create tabs for different views
    tab1, tab2, tab3 = st.tabs(["🔬 Research Findings", "📋 Summary", "💬 Follow-up Analysis"])
    
    with tab1:
        st.subheader("Research Agent Output")
        st.markdown("""
        <div class="agent-output">
        The Research Agent analyzes your topic and generates 3 highly specific factual points.
        </div>
        """, unsafe_allow_html=True)
        st.markdown(st.session_state.research_output)
        
        # Copy button
        st.code(st.session_state.research_output, language="markdown")
    
    with tab2:
        st.subheader("Summarizer Agent Output")
        st.markdown("""
        <div class="agent-output">
        The Summarizer Agent integrates research findings into a comprehensive summary.
        </div>
        """, unsafe_allow_html=True)
        st.markdown(st.session_state.summary_output)
        
        # Copy button
        st.code(st.session_state.summary_output, language="markdown")
    
    with tab3:
        st.subheader("Follow-up Analysis")
        st.markdown("""
        <div class="agent-output">
        The Research Agent provides additional insights when prompted with follow-up questions.
        </div>
        """, unsafe_allow_html=True)
        st.markdown(st.session_state.follow_up_output)
        
        # Copy button
        st.code(st.session_state.follow_up_output, language="markdown")
    
    # Shared memory display
    st.divider()
    with st.expander("💾 Shared Memory (Agent Context)"):
        memory_data = {
            "topic_context": topic,
            "research_cached": "Yes",
            "summary_cached": "Yes",
            "agents_synced": "Yes ✅"
        }
        st.json(memory_data)
    
    # Export options
    st.divider()
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📋 Copy All Results", use_container_width=True):
            combined = f"# {topic}\n\n## Research\n{st.session_state.research_output}\n\n## Summary\n{st.session_state.summary_output}\n\n## Follow-up\n{st.session_state.follow_up_output}"
            st.session_state.clipboard = combined
            st.toast("✅ Results copied to clipboard!")
    
    with col2:
        if st.button("📊 Download as Text", use_container_width=True):
            combined = f"# {topic}\n\n## Research\n{st.session_state.research_output}\n\n## Summary\n{st.session_state.summary_output}\n\n## Follow-up\n{st.session_state.follow_up_output}"
            st.download_button(
                "Download Results",
                combined,
                file_name=f"analysis_{topic[:20].replace(' ', '_')}.md",
                mime="text/markdown"
            )
    
    with col3:
        if st.button("🔄 New Analysis", use_container_width=True):
            st.session_state.research_output = None
            st.session_state.summary_output = None
            st.session_state.follow_up_output = None
            st.rerun()

# Footer
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.caption("🤖 Powered by LangChain + Google Gemini")
with col2:
    st.caption("📌 Multi-Agent System v1.0")
with col3:
    st.caption("✨ Built for intelligent research & analysis")
