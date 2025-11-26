import streamlit as st
import time
import os

# --- ۱. PAGE CONFIGURATION AND STYLING ---
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

# --- ۲. SIDEBAR (CONFIGURATION AND ABOUT) ---
with st.sidebar:
    st.title("🧭 Kokoro Compass")
    st.caption("Navigating Leadership in the Technovate Era") 
    
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
    
    api_key = st.text_input("OpenAI API Key", type="password", help="Enter your key. Demo mode will activate if left blank.")
    
# --- ۳. MAIN APPLICATION BODY ---

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
    st.caption("System Status: Online 🟢")
    

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
            time.sleep(3) 
            
            # --- AI Logic (Mock Response) ---
            response_text = ""
            
            if not api_key:
                # Demo response (English/Arabic)
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
                # Actual OpenAI integration code would go here
                response_text = "API connection is disabled in the demo version. The default text was displayed."

            # Display Output
            st.markdown(f'<div class="insight-card">{response_text}</div>', unsafe_allow_html=True)
            
            # Chart Section
            st.subheader("Projected Impact on Efficiency (Est.)")
            chart_data = {"Week 0": 10, "Week 2": 35, "Week 4": 70}
            st.bar_chart(chart_data)

# --- 4. FOOTER ---
st.markdown("---")
st.caption("© 2025 Kokoro Compass | Developed by AI Architect for the GLOBIS Technovate Era Event.")
