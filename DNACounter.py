# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:49:31 2021

@author: irem
"""

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image=Image.open('C:/Users/irem/Desktop/dna.png')

st.image(image,width=180)
st.write("""
         # DNA Nucleotide Count Web App
         
         This app counts the nucleotide composition of query DNA
         
         ***
         """)
st.header('Enter DNA sequence')
sequence_input=">DNA Query\nGAATTCAAAGTTCTTGGATGTGGTTAGGCCTT"    

sequence=st.text_area("Sequence input",sequence_input,height=250 )    
sequence=sequence.splitlines()
sequence=sequence[1:] #skips the sequence name (first line)
sequence=''.join(sequence) #concatenates list to string

st.write("""
         ***
         """)
st.header('Input (DNA Query)')  
sequence     

st.header('OUTPUT(DNA Nucleotide Count)')

st.subheader('1.Print dictionary')
def DNA_nucleotide_count(seq):
  d=dict([
          ('A',seq.count('A')),
          ('T',seq.count('T')),
          ('G',seq.count('G')),
          ('C',seq.count('C')),
            
            ])
  return d  

X=DNA_nucleotide_count(sequence)
X_label=list(X)
X_values=list(X.values())

X

st.subheader('2.Print text')
st.write('There are '+ str(X['A']) + ' adenine (A)') 
st.write('There are '+ str(X['G']) + ' guanine (G)')  
st.write('There are '+ str(X['C']) + ' cytosine (C)')  
st.write('There are '+ str(X['T']) + ' thymine (T)')  

st.subheader('3.Display Data Frame')
df=pd.DataFrame.from_dict(X, orient='index')
df=df.rename({0:'count'}, axis='columns')
df.reset_index(inplace=True)
df=df.rename(columns={'index':'nucleotide'})

st.table(df)


st.subheader('4.Display Bar Chart')
p=alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p=p.properties(
    width=alt.Step(80) #controls the width of bar
)

st.write(p)