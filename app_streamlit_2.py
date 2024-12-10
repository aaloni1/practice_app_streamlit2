import streamlit as st 
st.markdown(
    """
    <h1 style="text-align: center; background: linear-gradient(to right, purple, black); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Ady's Blog</h1>
    """,
    unsafe_allow_html=True
 )

blog_posts = [
    {
        "content": [
            ("Name", "Adam Rey G. Aloni"),  # Included name in content
            ("Age", "19 years old"),
            ("Gender", "Male"),
            ("Birthdate", "October 27, 2005"),
            ("Birthplace", "Quiapo, Manila"),
            ("Permanent Address", "Purok 4 Bonifacio, Ritaglenda, Basilisa, Dinagat Islands"),
            ("Current Address", "Brg. Taft Surigao City, Surigao Del Norte"),
        ],
        "image": "464679687_1714119689444 094_2948848053646144781_n.jpg"
    }
]

for post in blog_posts:
    # Display the image
    if "image" in post:
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center;">
                <img src="{post['image']}" style="width: 350px; height: 350px; object-fit: cover;" />
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    # Title for the content section
    st.subheader("About Me")  # Added title for the content section
    
    # Display content in a structured format
    for item in post["content"]:
        st.write(f"**{item[0]}:** {item[1]}")
    
    st.markdown("---")
    
