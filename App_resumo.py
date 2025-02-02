import streamlit as st
import pandas as pd
import numpy as np
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

nltk.download('punkt', quiet=True)

def summarize_text(text, sentence_count=3):
    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, sentence_count)
        return " ".join([str(sentence) for sentence in summary])
    except LookupError as e:
        st.error(f"Ocorreu um erro ao processar o texto: {e}")
        return "Erro ao processar o texto."

st.title("App de Resumo de Textos com IA")

st.header("Digite o texto que você deseja resumir:")
text = st.text_area("", height=200)

if st.button("Gerar Resumo"):
    if text:
        summary = summarize_text(text)
        st.subheader("Resumo:")
        st.write(summary)
    else:
        st.write("Por favor, insira o texto que você deseja resumir.")

st.markdown(
    "Este app usa a biblioteca [sumy](https://github.com/miso-belica/sumy) para sumarização de texto.")


