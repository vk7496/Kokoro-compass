import streamlit as st
import time
import os
from openai import OpenAI # Import the OpenAI library

# --- 1. PAGE CONFIGURATION AND STYLING ---
st.set_page_config(
    page_title="Kokoro Compass 🧭 | AI Executive Coach", 
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Arabic styling and professional look
st.markdown("""
<style>
    /* General Settings */
    .main {
        background-color: #f8f9fa;
    }
    
    /* Main Button Style */
    .stButton>button {
        background-color: #003366; 
        color: white;
        border-radius: 5px;
        width: 100%;
        font-weight: bold;
    }
    
    /* Arabic Tagline Style (Right-to-Left) */
    .arabic-tagline {
        color: #003366; 
        font-family: 'Amiri', serif; 
        direction: rtl; 
        font-size: 1.5em; 
        margin-top: 5px;
        margin-bottom: 20px;
    }
    
    /* Insight Card Style */
    .insight-card {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 25px;
        border-left: 5px solid #003366; 
    }
</style>
""", unsafe_allow_html=True)

# --- 2. SECRETS LOADING (API KEY MANAGEMENT) ---
# Retrieve API key from st.secrets. Checks for both uppercase and lowercase standards.

# 1. Check for the common UPPERCASE environment variable standard
if "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]
    
# 2. Check for the standard Streamlit lowercase key (as fallback)
elif "openai_api_key" in st.secrets:
    api_key = st.secrets["openai_api_key"]

# 3. If neither is found, run in Demo Mode
else:
    api_key = None
    
# --- 3. SIDEBAR (CONFIGURATION AND ABOUT) ---
with st.sidebar:
    st.title("🧭 Kokoro Compass")
    st.caption("Navigating Leadership in the Technovate Era") 
    
    # Show status based on secret loading
    if api_key:
        st.success("API Key loaded securely. Ready for Live Mode.")
    else:
        st.warning("Key not found in Streamlit Secrets. Running in Demo Mode.")
        
    st.divider()
    # ... (Rest of sidebar code remains the same)

# --- 3. SIDEBAR (CONFIGURATION AND ABOUT) ---
with st.sidebar:
    st.title("🧭 Kokoro Compass")
    st.caption("Navigating Leadership in the Technovate Era") 
    
    # Show status based on secret loading
    if api_key:
        st.success("OpenAI API Key loaded securely.")
    else:
        st.warning("Key not found in Streamlit Secrets. Running in Demo Mode.")
    
    st.divider()
    
    # Project Description (English and Arabic)
    st.markdown("### ℹ️ About This Project")
    st.markdown(
        """
        **Kokoro Compass** is an AI-powered executive partner that transforms complex business challenges into **clear strategic action**.
        
        It is designed to support regional leaders in achieving **Oman Vision 2040** goals by embedding AI wisdom into daily decision-making.
        """
    )
    st.markdown(
        """
        <div style="direction: rtl; font-family: 'Amiri', serif; font-size: 1.1em; color: #495057; margin-top: 10px;">
        **مُوَجِّهك الاستراتيجي الذكي لاتخاذ القرارات الحاسمة.**
        </div>
        """, unsafe_allow_html=True
    )
    
    st.divider()
    
    # Model Configuration
    st.subheader("Coach Configuration")
    methodology = st.selectbox(
        "Consulting Framework:",
        ["GLOBIS Kokorozashi", "Blue Ocean Strategy", "Emotional Intelligence", "Scenario Planning"]
    )
    
# --- 4. MAIN APPLICATION BODY ---

# Header Section
col1, col2 = st.columns([3, 1])
with col1:
    st.header("AI Executive Coach")
    st.markdown(f"**Smart Advisor using Methodology: {methodology}**")
    # Arabic Tagline in Focus
    st.markdown("""
    <p class='arabic-tagline'>
    مستشارك الاستراتيجي الذكي لاتخاذ القرارات
    </p>
    """, unsafe_allow_html=True)
with col2:
    st.metric("Metodology Selected", methodology)
    st.caption("System Status: Ready 🟢")
    

st.divider()

# User Input Section
user_input = st.text_area(
    "Describe your Management Challenge:", 
    height=180, 
    placeholder="Example (Oman Scenario): I'm the operations manager at Sohar Port. Cargo clearance takes a full day while the global standard is 8 hours. My team is demotivated, and productivity is low. How should I approach this using the GLOBIS method?"
)

# Analysis Button
if st.button("Get Consultation & Action Plan"):
    if not user_input:
        st.warning("Please describe your challenge first.")
    else:
        # Spinner to simulate processing
        with st.spinner('Analyzing data and aligning with C-level management frameworks...'):
            
            response_text = ""
            
            # --- AI Logic (Live vs. Mock) ---
            if not api_key:
                # --- DEMO MODE (FALLBACK) ---
                time.sleep(3)
                response_text = f"""
                ### ✅ Strategic Analysis based on {methodology}
                
                **1. Root Cause Diagnosis:**
                The core issue is not simply a process failure, but a **lack of understanding of the national importance** of this process. The team has lost connection with the larger goal (Oman Vision 2040: Global Logistics Hub).
                
                **2. Strategic Recommendation (Cultural Fit):**
                * **Focus on {methodology}:** The **{methodology}** framework suggests aligning the team's personal goals (Kokorozashi) with the national mission.
                * **Data Transparency:** Create a simple dashboard that shows each employee's delay impact in terms of "National Opportunity Cost," not just 'man-hours.'
                
                **3. Action Plan:**
                1.  **Hold an 'Inspirational' Meeting:** Not a technical review, but a **'Majlis'** style meeting to hear team concerns and redefine their vital role in the national economy.
                2.  **Use of AI:** Implement an AI model for automated customs documentation screening to target a clearance time of **6 hours**.
                
                > **✨ Key Takeaway:** *"الاستثمار في الإنسان هو الاستثمار الأنجح لتحقيق رؤية عُمان 2040."* (Investing in people is the most successful investment for achieving Oman Vision 2040.)
                """
            else:
                # --- LIVE API MODE ---
try:
    client = OpenAI(api_key=api_key)

    # Define the Coach's personality (System Prompt) - IMPROVED VERSION
    system_prompt = f"""
    You are an expert AI Executive Coach for C-level leaders and entrepreneurs. 
    
    You MUST use the **{methodology}** framework for your entire analysis. 
    If the user's input mentions a different framework (e.g., if the user wrote 'Kokorozashi' but the selected framework is 'Blue Ocean Strategy'), you MUST **prioritize and use the selected framework: {methodology}**.
    
    The response MUST be primarily in **English**, but you must include one key strategic sentence or quote in **Arabic** or related to **Oman Vision 2040**.
    
    Structure your response with clear Markdown headings: 
    1. Diagnosis (Analyze the core problem).
    2. Strategic Recommendation (Suggest a high-level solution aligned with the {methodology} framework).
    3. Action Plan (Provide 2-3 immediate steps). 
    
    The final takeaway must be a single, impactful, relevant quote.
    """

    completion = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    # ... بقیه کد (استخراج پاسخ و مدیریت خطا)

                    response_text = completion.choices[0].message.content

                except Exception as e:
                    st.error("An API error occurred. Please check your API key or connection.")
                    st.code(f"Error Details: {e}")
                    response_text = "ERROR: Failed to connect to AI server. Please check the error box above for details."
            
            # Display Output
            st.markdown(f'<div class="insight-card">{response_text}</div>', unsafe_allow_html=True)
            
            # Chart Section
            st.subheader("Projected Impact on Efficiency (Est.)")
            chart_data = {"Week 0": 10, "Week 2": 35, "Week 4": 70}
            st.bar_chart(chart_data)

# --- 5. FOOTER ---
st.markdown("---")
st.caption("© 2025 Kokoro Compass | Developed by AI Architect for the GLOBIS Technovate Era Event.")
