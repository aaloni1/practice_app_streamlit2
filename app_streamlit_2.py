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
        "image": "https://scontent.fcgy2-4.fna.fbcdn.net/v/t39.30808-6/447232820_485701057364609_6882034262964220786_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=a5f93a&_nc_eui2=AeHjriIDTRJC_PcvJAfgIouOFYiAgsWwUSoViICCxbBRKheimFO4y58FaaCHAq9X9ZazI6GTSJfowGXCwAWihCGQ&_nc_ohc=BKxVkhXz20EQ7kNvgHPdImd&_nc_zt=23&_nc_ht=scontent.fcgy2-4.fna&_nc_gid=Ai8oJezuBIWDV3zOmo6nf18&oh=00_AYC8O_UH06Ya04GiX9_yRbtBH9FcVgi15JusViQXFAD3pQ&oe=674B3112"
    }
]
