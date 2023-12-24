# Libraries
import pandas as pd

# Data Sources
def get_data(query):
    storage_options = {'User-Agent': 'Mozilla/5.0'}

    if query == 'Transactions Overview':
        return pd.read_json('https://flipsidecrypto.xyz/api/v1/queries/9aa15f9c-d52a-4744-92dc-a6c0acb3e856/data/latest', storage_options=storage_options)

    elif query == 'Transactions Daily':
        return pd.read_json('https://flipsidecrypto.xyz/api/v1/queries/a466d059-dc51-4562-93c3-ce597108d792/data/latest', storage_options=storage_options)

    elif query == 'Transactions Heatmap':
        return pd.read_json('https://flipsidecrypto.xyz/api/v1/queries/ddfd570d-3f48-4a07-a746-b6da1a938dd3/data/latest', storage_options=storage_options)

    elif query == 'Transfers Overview':
        return pd.read_json('https://flipsidecrypto.xyz/api/v1/queries/9353f576-acb7-463c-a7e0-4fea4e878902/data/latest', storage_options=storage_options)

    elif query == 'Transfers Daily':
        return pd.read_json('https://flipsidecrypto.xyz/api/v1/queries/eeede796-95e5-4b60-8f23-d8768b58c54f/data/latest', storage_options=storage_options)

    elif query == 'Transfers Heatmap':
        return pd.read_json('https://flipsidecrypto.xyz/api/v1/queries/f1703b63-5901-4c03-9de2-17e3dd08127c/data/latest', storage_options=storage_options)
    
    elif query == 'Swaps Overview':
        return pd.read_json('https://flipsidecrypto.xyz/api/v1/queries/befae122-271c-4f53-aadb-e183c8dc3f6e/data/latest', storage_options=storage_options)

    elif query == 'Swaps Daily':
        return pd.read_json('https://flipsidecrypto.xyz/api/v1/queries/a35e12a9-033a-4f72-86bc-3aa6e568d4cc/data/latest', storage_options=storage_options)

    elif query == 'Swaps Heatmap':
        return pd.read_json('https://flipsidecrypto.xyz/api/v1/queries/ebc0ebba-0486-47d9-ae44-4f260e15c216/data/latest', storage_options=storage_options)

    elif query == 'NFTs Overview':
        return pd.read_json('https://flipsidecrypto.xyz/api/v1/queries/168b4bfa-81cc-45ed-ba05-a7f4e14d57f3/data/latest', storage_options=storage_options)

    elif query == 'NFTs Daily':
        return pd.read_json('https://flipsidecrypto.xyz/api/v1/queries/903a9144-f58b-4876-a00d-3724b20f7d75/data/latest', storage_options=storage_options)

    elif query == 'NFTs Heatmap':
        return pd.read_json('https://flipsidecrypto.xyz/api/v1/queries/3520b68e-ce6f-4140-b7ba-5eadd4112ebc/data/latest', storage_options=storage_options)

    return None