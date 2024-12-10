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
        "image": "https://scontent.fdvo2-2.fna.fbcdn.net/v/t39.30808-6/447232820_485701057364609_6882034262964220786_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=a5f93a&_nc_eui2=AeHjriIDTRJC_PcvJAfgIouOFYiAgsWwUSoViICCxbBRKheimFO4y58FaaCHAq9X9ZazI6GTSJfowGXCwAWihCGQ&_nc_ohc=jDH46ugOoaUQ7kNvgGXSlUd&_nc_zt=23&_nc_ht=scontent.fdvo2-2.fna&_nc_gid=ANjCY7y3lFv1N_er1UPRHfZ&oh=00_AYB18OwG02YpXg68YdeYedY15s7Or1VRAN-_NCicimu45g&oe=675DA612"
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
    
