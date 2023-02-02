# Libraries
import streamlit as st
import pandas as pd

# Data Sources
@st.cache(ttl=1000)
def get_data(query):
    if query == 'Transactions Overview':
        arbitrum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/f06a4840-9310-41c7-b2b2-1c812884d728/data/latest')
        avalanche = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/d543922f-c8b6-4dc9-9caf-91954b3573d4/data/latest')
        axelar = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/4ff35680-e680-45c0-b6e9-2c63e6f92156/data/latest')
        bsc = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/97d2d421-ebda-4dae-87da-6f27b4478e52/data/latest')
        cosmos = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/8cac9410-e4de-4cbe-b146-c6f7f1f053dc/data/latest')
        ethereum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/572f2d6e-4b65-47b7-9dd6-be0710c6e024/data/latest')
        flow = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/8a0d84a3-bb18-4815-a36e-850c719b10c3/data/latest')
        gnosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/e26eeb64-7bf2-42cb-9222-2e6d6483d053/data/latest')
        near = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/314e9e48-52ef-466c-a848-3e95957ee9fc/data/latest')
        optimism = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/72c31b05-ec16-4533-a2ec-409a49bbe492/data/latest')
        osmosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/20a3e7ff-fcf5-43f6-bc12-90a9544b55a0/data/latest')
        polygon = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/8ea10e70-c838-4a94-b1ef-0cb282e5ced1/data/latest')
        solana = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/e01d82cc-9b5d-4166-af72-6110f4947140/data/latest')
        return pd.concat(
            [arbitrum, avalanche, axelar, bsc, cosmos, ethereum, flow, gnosis, near, optimism, osmosis, polygon, solana]
                ).sort_values('Blockchain').reset_index(drop=True)

    elif query == 'Transactions Daily':
        arbitrum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/7b550fd2-39be-465d-9191-a45d8eb2678b/data/latest')
        avalanche = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/b076d022-c0a5-4556-abdb-4b993d04d4a4/data/latest')
        axelar = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/c9574cb4-1b02-4141-a52c-3a68475adf33/data/latest')
        bsc = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/16aa6493-8602-483e-b691-a5067ca47595/data/latest')
        cosmos = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/2c7806ff-70db-40e5-832e-35ec080a60e0/data/latest')
        ethereum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/22f763f9-f927-4875-b3e2-8cd750aae442/data/latest')
        flow = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/bf921f59-fe45-4e1d-9bc1-3ddea006fd19/data/latest')
        gnosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/70395b58-ba81-49a5-90fe-6412786e0293/data/latest')
        near = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/a8e2c436-327d-4a89-a829-76d3574ef16f/data/latest')
        optimism = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/dc627865-c013-49be-bb1f-648bd62c59d1/data/latest')
        osmosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/d4a7ec49-4e64-4aa2-a378-87104c8a9521/data/latest')
        polygon = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/19453ea9-c03f-48e5-b1e9-13742190d551/data/latest')
        solana = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/e584be47-893a-460d-94a0-f217efe14fda/data/latest')
        return pd.concat(
            [arbitrum, avalanche, axelar, bsc, cosmos, ethereum, flow, gnosis, near, optimism, osmosis, polygon, solana]
                ).sort_values(['Date', 'Blockchain']).reset_index(drop=True)

    elif query == 'Transactions Heatmap':
        arbitrum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/c6e9e418-1bba-401e-8275-ff71401e9ae2/data/latest')
        avalanche = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/ae43bcac-4cfe-4e9d-9eb9-8413e623f544/data/latest')
        axelar = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/a8041ee1-5d59-4105-a493-981c392e9e83/data/latest')
        bsc = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/2b03f2a3-c48e-41d0-9507-f6dbac69b6ce/data/latest')
        cosmos = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/5de98199-0a6e-4062-bf5e-5e1e41ce5696/data/latest')
        ethereum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/3461c085-6949-4822-8eaf-1660ec80faeb/data/latest')
        flow = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/90219f8f-7700-4083-9db0-99a3047bca95/data/latest')
        gnosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/1bd8d28e-ff39-462c-8d0f-7f68143a0e35/data/latest')
        near = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/eae96499-833b-4fd0-ac41-2e12d2cfc84a/data/latest')
        optimism = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/767aeab2-6af9-4896-81d5-f3c76e0a4092/data/latest')
        osmosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/040ca9ec-c5e5-4f93-b35f-40a9e365aabc/data/latest')
        polygon = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/d84043fc-fc53-4db3-9607-80fec40eae81/data/latest')
        solana = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/852b71d4-c08c-4eea-9b11-38ac7cc8a63c/data/latest')
        return pd.concat(
            [arbitrum, avalanche, axelar, bsc, cosmos, ethereum, flow, gnosis, near, optimism, osmosis, polygon, solana]
                ).sort_values(['Day', 'Hour', 'Blockchain']).reset_index(drop=True)

    elif query == 'New Users Daily':
        arbitrum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/ff167b88-3f93-416f-a145-8dd899473ba4/data/latest')
        avalanche = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/478ca10d-e45f-4ef4-bd82-eda76b08911d/data/latest')
        axelar = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/27409124-5c7d-4b79-a20d-2c3e6e47af60/data/latest')
        bsc = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/37e21782-f2c0-4e58-86e0-97d60fbb2b40/data/latest')
        cosmos = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/a71d9d01-661d-4b1e-be7d-f26af9722e09/data/latest')
        ethereum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/6654b8bc-b684-42ef-90bf-0395b8e571dd/data/latest')
        flow = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/e2b8e7f6-b19f-4ff6-b16e-d383b9c4df53/data/latest')
        gnosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/5667daa1-496e-4068-adb3-1b03aa5f8642/data/latest')
        near = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/8524fa45-f475-4811-b3ec-e48b65261c48/data/latest')
        optimism = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/3f4a8c40-79e2-4667-9fc8-86a04ed34d4f/data/latest')
        osmosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/4fa61bb5-aae5-4d58-92ef-5a39af629ac2/data/latest')
        polygon = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/e1455d7a-ab1f-4b30-834f-85dca80a7d88/data/latest')
        solana = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/73306514-dd1f-4a18-8c55-e1c024520130/data/latest')
        return pd.concat(
            [arbitrum, avalanche, axelar, bsc, cosmos, ethereum, flow, gnosis, near, optimism, osmosis, polygon, solana]
                ).sort_values(['Date', 'Blockchain']).reset_index(drop=True)

    return None