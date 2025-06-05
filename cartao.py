import streamlit as st
from PIL import Image
from fpdf import FPDF
from io import BytesIO

st.set_page_config(page_title="Cartão de Visita Digital", layout="centered")

st.title("💼 Cartão de Visita Digital Moderno")

st.markdown("Preencha os dados abaixo para gerar seu cartão de visita digital com visual moderno:")

# --- Formulário ---
with st.form("card_form"):
    nome = st.text_input("Nome")
    cargo = st.text_input("Cargo")
    empresa = st.text_input("Empresa")
    whatsapp = st.text_input("WhatsApp (com DDD)")
    email = st.text_input("E-mail")
    instagram = st.text_input("Instagram (sem @)")
    logotipo = st.file_uploader("Logotipo (PNG ou JPG)", type=["png", "jpg", "jpeg"])

    submitted = st.form_submit_button("Gerar Cartão")

# --- Geração de cartão ---
if submitted:
    st.subheader("🔎 Visualização do Cartão")

    # Exibir cartão
    with st.container():
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f"""
                <div style="background-color:#1f2937;padding:20px;border-radius:20px;color:white;">
                    <h2 style="margin-bottom:5px;">{nome}</h2>
                    <p style="margin-top:0;">{cargo} @ {empresa}</p>
                    <hr style="border:0.5px solid #555;">
                    <p>📞 {whatsapp}</p>
                    <p>📧 {email}</p>
                    <p>📸 @{instagram}</p>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            if logotipo:
                st.image(logotipo, caption="Logotipo", width=120)

    # --- Gerar PDF ---
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_fill_color(31, 41, 55)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(200, 10, txt="Cartão de Visita Digital", ln=True, align='C')
    pdf.ln(10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(200, 10, txt=f"Nome: {nome}", ln=True)
    pdf.cell(200, 10, txt=f"Cargo: {cargo}", ln=True)
    pdf.cell(200, 10, txt=f"Empresa: {empresa}", ln=True)
    pdf.cell(200, 10, txt=f"WhatsApp: {whatsapp}", ln=True)
    pdf.cell(200, 10, txt=f"E-mail: {email}", ln=True)
    pdf.cell(200, 10, txt=f"Instagram: @{instagram}", ln=True)

    pdf_bytes = BytesIO()
    pdf.output(pdf_bytes)
    pdf_bytes.seek(0)

    st.download_button("📄 Baixar PDF do Cartão", data=pdf_bytes, file_name="cartao_visita.pdf")

    st.success("Cartão gerado com sucesso!")
