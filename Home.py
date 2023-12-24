# Libraries
import streamlit as st
from PIL import Image

# Confit
st.set_page_config(page_title='Cross Chain Monitoring Tool', page_icon=':bar_chart:', layout='wide')

# Outlier warning
st.warning("""
    The data within this app is no longer being updated. Feel free to check out the same author's
    new tool called the [Outlier](https://outlier.streamlit.app/) for a more modern UI/UX in
    presenting the same set of data.
""")

# Title
st.title('Cross Chain Monitoring Tool')

# Blockchains
c1, c2, c3, c4, c5, c6 = st.columns(6)
c1.image(Image.open('images/arbitrum-logo.png'))
c2.image(Image.open('images/avalanche-logo.png'))
c3.image(Image.open('images/bsc-logo.png'))
c4.image(Image.open('images/ethereum-logo.png'))
c5.image(Image.open('images/optimism-logo.png'))
c6.image(Image.open('images/polygon-logo.png'))

# Introduction
st.write(
    """
    The crypto industry continues to progress and its development has never stopped. Contributors
    of each blockchain keep developing each segment of the industry and the whole crypto ecosystem.
    This tool is designed to allow viewers to journey into the world of crypto ecosystems of some
    of the major blockchains, and compare their performance.

    This tool is designed and structured in multiple **Pages** that are accessible using the sidebar.
    Each of these Pages addresses a different segment of the crypto industry. Within each segment
    (Macro, Transfers, Swaps, NFTs, etc.) you are able to filter your desired blockchains to
    narrow/expand the comparison. By selecting a single blockchain, you can observe a deep dive
    into that particular network.

    All values for amounts, prices, and volumes are in **U.S. dollars** and the time frequency of the
    analysis is limited to December 2023.
    """
)

# Methodology
st.subheader('Methodology')
st.write(
    """
    The data for this cross-chain comparison were extracted from the [**Flipside Crypto**](https://flipsidecrypto.xyz)
    data platform by using its **REST API**. These queries are currently set to return data for only December 2023
    and are imported as a JSON file directly to each page. Due to the heavy computational power required to execute
    the queries, and also the size of the raw data being too large, it was not feasible to cover data for a longer
    period, or by downloading the data and loading it from the repository itself. Therefore, the REST API was
    selected as the proper form of loading data for the time being. The codes for this tool are saved and accessible
    in its [**GitHub Repository**](https://github.com/alitaslimi/cross-chain-monitoring).
    """
)

# Divider
st.divider()

# Credits
c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Data Analyst: [@AliTslm](https://twitter.com/AliTslm)**', icon="💡")
with c2:
    st.info('**GitHub: [@alitaslimi](https://github.com/alitaslimi)**', icon="💻")
with c3:
    st.info('**Data: [Flipside Crypto](https://flipsidecrypto.xyz)**', icon="🧠")