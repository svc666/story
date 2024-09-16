import streamlit as st
import requests

st.title('Children Story App')

# Form for story generation
with st.form(key='story_form'):
    prompt = st.text_input('Enter a story prompt:')
    submit_button = st.form_submit_button(label='Generate Story')

    if submit_button:
        response = requests.post('http://your-ec2-public-dns/generate_story', json={'prompt': prompt})
        if response.status_code == 200:
            story = response.json().get('story', '')
            st.write(story)
        else:
            st.error('Error generating story.')

# Recommendations section
st.header('Recommended Stories')
response = requests.get('http://your-ec2-public-dns/recommend_story')
if response.status_code == 200:
    recommendations = response.json().get('recommendations', [])
    for rec in recommendations:
        st.write(f'- {rec}')
else:
    st.error('Error fetching recommendations.')
