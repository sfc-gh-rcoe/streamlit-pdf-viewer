import streamlit as st
import cv2
from PyPDF2 import PdfReader
from PIL import Image

st.write("Welcome!")

m_cont = st.container()

t_file = st.sidebar.file_uploader("Pick a PDF File")

if (t_file != None):
   t_contents = PdfReader(t_file)
   num_pages = len(t_contents.pages)
   if (num_pages > 0):
      page_one = t_contents.pages[0]
      page_one_text = page_one.extract_text()
      with m_cont:
         st.write("Number of pages in the .PDF: " + str(num_pages))
         for i in range(num_pages):
            curr_page_content = t_contents.pages[i]
            curr_page_txt = curr_page_content.extract_text()
            st.write(curr_page_txt)
      st.write(t_contents.pages)
