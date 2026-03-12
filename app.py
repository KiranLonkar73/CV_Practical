import streamlit as st
from detector import count_people
from PIL import Image

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Crowd Counter Dashboard",
    page_icon="👥",
    layout="wide"
)

# -----------------------------
# Custom CSS Styling
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }

[data-testid="stAppViewContainer"] {
    background: #F0F5FF;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stHeader"] {
    background: #F0F5FF !important;
}

[data-testid="stSidebar"] {
    background: #FFFFFF !important;
    border-right: 1px solid rgba(0,0,0,0.07) !important;
}

[data-testid="stFileUploader"] {
    background: transparent;
}

.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    max-width: 1200px !important;
}

/* Hero Header */
.hero-wrap {
    position: relative;
    padding: 48px 0 36px;
    text-align: center;
    overflow: hidden;
}

.hero-glow {
    position: absolute;
    top: -60px; left: 50%;
    transform: translateX(-50%);
    width: 500px; height: 300px;
    background: radial-gradient(ellipse at center, rgba(0,120,255,0.10) 0%, transparent 70%);
    pointer-events: none;
}

.hero-badge {
    display: inline-block;
    background: rgba(0,112,243,0.10);
    border: 1px solid rgba(0,112,243,0.25);
    color: #0070F3;
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 5px 14px;
    border-radius: 100px;
    margin-bottom: 18px;
}

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 52px;
    font-weight: 800;
    color: #0F172A;
    line-height: 1.1;
    letter-spacing: -1px;
    margin: 0 0 12px;
}

.hero-title span {
    background: linear-gradient(90deg, #0070F3, #7B61FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-sub {
    font-size: 15px;
    color: #64748B;
    font-weight: 300;
    letter-spacing: 0.3px;
}

/* Divider */
.section-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,0,0,0.08), transparent);
    margin: 10px 0 32px;
}

/* Upload Zone */
.upload-label {
    font-family: 'Syne', sans-serif;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #475569;
    margin-bottom: 10px;
    display: block;
}

[data-testid="stFileUploader"] > div {
    background: #FFFFFF !important;
    border: 1.5px dashed rgba(0,112,243,0.35) !important;
    border-radius: 16px !important;
    transition: border-color 0.2s, background 0.2s;
}

[data-testid="stFileUploader"] > div:hover {
    background: rgba(0,112,243,0.03) !important;
    border-color: rgba(0,112,243,0.7) !important;
}

/* Panel Cards */
.panel {
    background: #FFFFFF;
    border: 1px solid rgba(0,0,0,0.07);
    border-radius: 20px;
    padding: 28px;
    height: 100%;
    box-shadow: 0 2px 16px rgba(0,0,0,0.05);
}

.panel-title {
    font-family: 'Syne', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #94A3B8;
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.panel-title::before {
    content: '';
    display: inline-block;
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #0070F3;
}

/* Big Counter */
.counter-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 32px 0;
    gap: 6px;
}

.counter-ring {
    position: relative;
    width: 160px; height: 160px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
}

.counter-ring::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 50%;
    background: conic-gradient(#0070F3 0%, #7B61FF 60%, rgba(0,0,0,0.06) 60%);
    padding: 3px;
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
}

.counter-ring::after {
    content: '';
    position: absolute;
    inset: 6px;
    border-radius: 50%;
    background: #FFFFFF;
    box-shadow: inset 0 0 20px rgba(0,112,243,0.06);
}

.counter-num {
    font-family: 'Syne', sans-serif;
    font-size: 56px;
    font-weight: 800;
    color: #0F172A;
    line-height: 1;
    position: relative;
    z-index: 2;
}

.counter-label {
    font-size: 13px;
    color: #64748B;
    font-weight: 400;
    letter-spacing: 0.5px;
    text-align: center;
}

.counter-sublabel {
    font-size: 11px;
    color: #94A3B8;
    font-weight: 400;
    letter-spacing: 1px;
    text-transform: uppercase;
    text-align: center;
}

/* Status Badge */
.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 20px;
    border-radius: 100px;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    font-weight: 500;
    letter-spacing: 0.3px;
    margin-top: 8px;
}

.status-normal {
    background: rgba(16,185,129,0.10);
    border: 1px solid rgba(16,185,129,0.30);
    color: #059669;
}

.status-high {
    background: rgba(245,158,11,0.10);
    border: 1px solid rgba(245,158,11,0.30);
    color: #D97706;
}

.status-dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    animation: pulse-dot 1.8s ease-in-out infinite;
}

.dot-green { background: #10B981; box-shadow: 0 0 6px #10B981; }
.dot-amber { background: #F59E0B; box-shadow: 0 0 6px #F59E0B; }

@keyframes pulse-dot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.7); }
}

/* Stat Pills */
.stat-row {
    display: flex;
    gap: 10px;
    margin-top: 28px;
    flex-wrap: wrap;
}

.stat-pill {
    flex: 1;
    min-width: 80px;
    background: #F8FAFF;
    border: 1px solid rgba(0,112,243,0.10);
    border-radius: 12px;
    padding: 14px 12px;
    text-align: center;
}

.stat-pill-num {
    font-family: 'Syne', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #1E293B;
}

.stat-pill-lbl {
    font-size: 10px;
    color: #94A3B8;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 3px;
}

/* Sidebar styles */
.sidebar-logo {
    font-family: 'Syne', sans-serif;
    font-size: 18px;
    font-weight: 800;
    color: #0F172A;
    padding: 8px 0 20px;
    letter-spacing: -0.5px;
}

.sidebar-logo span {
    color: #0070F3;
}

.sidebar-section {
    font-family: 'Syne', sans-serif;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #CBD5E1;
    margin: 20px 0 10px;
}

.sidebar-info-card {
    background: #F8FAFF;
    border: 1px solid rgba(0,112,243,0.10);
    border-radius: 12px;
    padding: 14px;
    margin-bottom: 10px;
}

.sidebar-info-label {
    font-size: 10px;
    color: #94A3B8;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 4px;
}

.sidebar-info-value {
    font-family: 'Syne', sans-serif;
    font-size: 15px;
    font-weight: 700;
    color: #1E293B;
}

.sidebar-tip {
    background: rgba(0,112,243,0.06);
    border-left: 3px solid #0070F3;
    border-radius: 0 8px 8px 0;
    padding: 10px 12px;
    font-size: 12px;
    color: #475569;
    line-height: 1.5;
    margin-top: 8px;
}

/* Footer */
.footer {
    text-align: center;
    padding: 28px 0 10px;
    font-size: 12px;
    color: #94A3B8;
    letter-spacing: 0.5px;
}

.footer span {
    color: #64748B;
}

/* Subheader override */
h2, h3 { color: #64748B !important; font-family: 'Syne', sans-serif !important; }

/* Streamlit image */
[data-testid="stImage"] img {
    border-radius: 12px !important;
    border: 1px solid rgba(0,0,0,0.07) !important;
}

/* Hide streamlit branding */
#MainMenu, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.markdown("<div class='sidebar-logo'>👥 Crowd<span>Counter</span></div>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("<div class='sidebar-section'>📤 Upload Image</div>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")

    st.markdown("<div class='sidebar-section'>⚙️ Settings</div>", unsafe_allow_html=True)
    threshold = st.slider("High crowd threshold", min_value=5, max_value=50, value=10, step=1)
    confidence = st.slider("Detection confidence", min_value=0.1, max_value=1.0, value=0.5, step=0.05)

    st.markdown("<div class='sidebar-section'>ℹ️ About</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='sidebar-tip'>
        Upload any crowd image and the model will automatically count people using YOLOv8 object detection.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class='sidebar-info-card'>
        <div class='sidebar-info-label'>Model</div>
        <div class='sidebar-info-value'>YOLOv8</div>
    </div>
    <div class='sidebar-info-card'>
        <div class='sidebar-info-label'>Supported Formats</div>
        <div class='sidebar-info-value'>JPG · PNG · JPEG</div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Hero Header
# -----------------------------
st.markdown("""
<div class="hero-wrap">
    <div class="hero-glow"></div>
    <div class="hero-badge">⚡ YOLOv8 Powered</div>
    <div class="hero-title">Smart Crowd<br><span>Counter</span></div>
    <div class="hero-sub">Real-time people detection powered by computer vision</div>
</div>
<div class="section-divider"></div>
""", unsafe_allow_html=True)

# -----------------------------
# Main Content
# -----------------------------
if uploaded_file:
    image = Image.open(uploaded_file)

    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Analyzing image..."):
        people_count = count_people("temp.jpg")

    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    col1, col2 = st.columns([3, 2], gap="large")

    # -----------------------------
    # Image Panel
    # -----------------------------
    with col1:
        st.markdown("<div class='panel'>", unsafe_allow_html=True)
        st.markdown("<div class='panel-title'>Uploaded Image</div>", unsafe_allow_html=True)
        st.image(image, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # -----------------------------
    # Results Panel
    # -----------------------------
    with col2:
        is_high = people_count > threshold

        status_class = "status-high" if is_high else "status-normal"
        dot_class = "dot-amber" if is_high else "dot-green"
        status_text = "High Density" if is_high else "Normal Level"
        status_icon = "⚠" if is_high else "✓"

        density = round((people_count / (threshold * 2)) * 100) if people_count < threshold * 2 else 100
        avg_spacing = round(10 / people_count, 1) if people_count > 0 else "—"

        st.markdown(f"""
        <div class="panel">
            <div class="panel-title">Detection Result</div>
            <div class="counter-wrap">
                <div class="counter-ring">
                    <span class="counter-num">{people_count}</span>
                </div>
                <div class="counter-label" style="font-size:15px; color:#475569; font-weight:500;">People Detected</div>
                <div class="counter-sublabel" style="margin-top:4px;">in uploaded frame</div>
                <div class="status-badge {status_class}">
                    <span class="status-dot {dot_class}"></span>
                    {status_icon} {status_text}
                </div>
            </div>
            <div class="stat-row">
                <div class="stat-pill">
                    <div class="stat-pill-num">{density}%</div>
                    <div class="stat-pill-lbl">Density</div>
                </div>
                <div class="stat-pill">
                    <div class="stat-pill-num">{'Low' if people_count <= threshold//2 else 'Med' if people_count <= threshold else 'High'}</div>
                    <div class="stat-pill-lbl">Level</div>
                </div>
                <div class="stat-pill">
                    <div class="stat-pill-num">{avg_spacing}m</div>
                    <div class="stat-pill-lbl">Avg Gap</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div style="text-align:center; padding: 60px 20px; color: #94A3B8;">
        <div style="font-size: 48px; margin-bottom: 16px;">🖼️</div>
        <div style="font-family: 'Syne', sans-serif; font-size: 18px; font-weight: 600; color: #CBD5E1;">No image uploaded yet</div>
        <div style="font-size: 14px; margin-top: 8px;">Upload an image from the sidebar to get started</div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Footer
# -----------------------------
st.markdown("""
<div class="footer">
    <span>Computer Vision Project</span> &nbsp;·&nbsp; YOLOv8 + Streamlit &nbsp;·&nbsp; Real-time Detection
</div>
""", unsafe_allow_html=True)