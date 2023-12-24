# Libraries
import streamlit as st
import pandas as pd

# Data Sources
# @st.cache(ttl=1000, allow_output_mutation=True)
def get_data(query):
    storage_options = {'User-Agent': 'Mozilla/5.0'}

    if query == 'Transactions Overview':
        return pd.read_json('https://flipsidecrypto.xyz/api/v1/queries/9aa15f9c-d52a-4744-92dc-a6c0acb3e856/data/latest', storage_options=storage_options)

    elif query == 'Transactions Daily':
        return pd.read_json('https://flipsidecrypto.xyz/api/v1/queries/a466d059-dc51-4562-93c3-ce597108d792/data/latest', storage_options=storage_options)

    elif query == 'Transactions Heatmap':
        return pd.read_json('https://flipsidecrypto.xyz/api/v1/queries/ddfd570d-3f48-4a07-a746-b6da1a938dd3/data/latest', storage_options=storage_options)

    elif query == 'Fee Payers':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7eae69ea-2387-420d-b4b9-6eceeb5ef22d/data/latest')
        # arbitrum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/fa2e6071-6c07-4efd-a765-99a002b77821/data/latest')
        # avalanche = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/6429c5d5-e630-44b2-ad38-10c166a7939a/data/latest')
        # axelar = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/ef7485a3-b99a-4ed1-a9fe-f8b7dc237e98/data/latest')
        # bsc = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/2520e7d9-8529-4938-b155-51ffa65952e5/data/latest')
        # cosmos = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/1ba5412c-50aa-458f-8bdd-dbab0118855d/data/latest')
        # ethereum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/75234e0e-851b-413c-b76a-367209f0f907/data/latest')
        # flow = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/ffd908f4-8596-4810-88b4-498bf1fad2f7/data/latest')
        # gnosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/fd5da965-939d-48a6-9459-9d8f40a684e8/data/latest')
        # near = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/0b30976a-25a8-4b79-8fcd-07b6901d6a5c/data/latest')
        # optimism = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/6686a6d9-5eb0-4c34-86bc-46cdb949202f/data/latest')
        # osmosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/2b1e0d17-0eb5-4235-bf5f-63b0408dc98b/data/latest')
        # polygon = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/0765116e-4a51-4853-b3f6-af21c1f6aedf/data/latest')
        # solana = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/bfbeafa1-6cd1-4680-a8fb-b7246df70b84/data/latest')
        # return pd.concat(
        #     [arbitrum, avalanche, axelar, bsc, cosmos, ethereum, flow, gnosis, near, optimism, osmosis, polygon, solana]
        #         ).sort_values('Blockchain').reset_index(drop=True)

    elif query == 'Swaps Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b3d90320-3fcb-44f0-b0b9-3f72ee779dcb/data/latest')
        # arbitrum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/e0379ed9-44e9-4cad-8a5b-885bf08836a5/data/latest')
        # avalanche = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/642c87d9-461e-40c4-b904-f3d1fc5ee349/data/latest')
        # bsc = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/18c33d5b-9dd5-403f-95a0-c562ca61736f/data/latest')
        # ethereum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/bba010dd-b5ce-4682-a04c-ab30282b07ff/data/latest')
        # flow = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/025ca622-5f5a-4aa8-bc0c-794d49e5e651/data/latest')
        # gnosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/7b78d096-8e7a-4a8a-bd58-aa23ea963d9e/data/latest')
        # near = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/89e9448d-1562-44ac-9afe-86d70a53de31/data/latest')
        # optimism = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/139e40ba-ebde-4be6-afc9-31a6c984d720/data/latest')
        # osmosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/0dfb8d98-b739-4145-adea-ea5c3e739a1d/data/latest')
        # polygon = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/1a236b32-9cd4-4cba-a57a-cdb273d90d61/data/latest')
        # solana = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/12eb8a6c-af55-4b84-9b8c-c7cf132f33fd/data/latest')
        # thorchain = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/fb99ddc5-0570-4219-89e3-3ac4d9e236b7/data/latest')
        # return pd.concat(
        #     [arbitrum, avalanche, bsc, ethereum, flow, gnosis, near, optimism, osmosis, polygon, solana, thorchain]
        #         ).sort_values('Blockchain').reset_index(drop=True)

    elif query == 'Swaps Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/fed187af-6c8e-49fc-82d1-1975926e3951/data/latest')
        # arbitrum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/0d131400-82a0-4fb8-9032-b548da63f9b1/data/latest')
        # avalanche = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/53313b42-f68a-41ea-95d3-c37878d8b025/data/latest')
        # bsc = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/c4112917-9a2e-4055-bf96-c624de286149/data/latest')
        # ethereum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/8d4ebda0-697d-4310-8611-095555c25dad/data/latest')
        # flow = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/be80508e-f217-42fa-b0ef-47f49a3526b2/data/latest')
        # gnosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/7f37184a-f731-405b-9f4d-3b7cd49a4779/data/latest')
        # near = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/ae24a06b-c590-4d44-81f3-223fd8ba4163/data/latest')
        # optimism = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/dc073155-1bde-4607-b766-2d3e402cacf1/data/latest')
        # osmosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/2b30893a-cfec-4341-8091-6b601cd80ea0/data/latest')
        # polygon = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/d6cc6941-c6f3-4a98-b2a2-03397ed7c930/data/latest')
        # solana = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/d56ebd12-2f0d-4ca1-8226-71450c2a2b20/data/latest')
        # thorchain = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/457c96a4-db5c-47ee-939a-9d5af8fdf414/data/latest')
        # return pd.concat(
        #     [arbitrum, avalanche, bsc, ethereum, flow, gnosis, near, optimism, osmosis, polygon, solana, thorchain]
        #         ).sort_values(['Date', 'Blockchain']).reset_index(drop=True)

    elif query == 'Swaps Heatmap':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3fa50926-77bc-44f8-b190-7bd48d408c85/data/latest')
        # arbitrum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/dd45ef88-7d17-43ef-8cd4-a6f3eba37cb0/data/latest')
        # avalanche = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/ab6a2adf-a410-4bc3-9a84-d530d8f34cf0/data/latest')
        # bsc = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/4211617f-263f-44f2-b2ae-6c25fb024ede/data/latest')
        # ethereum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/07957cc6-6543-4e85-9432-7281d44230ad/data/latest')
        # flow = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/dccbbe78-3d61-4c75-a7c9-8b86b24bb4a4/data/latest')
        # gnosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/53fe4557-6d1b-4f7a-81c3-4f3df5ba2972/data/latest')
        # near = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/caccd7b2-8e7f-443b-a869-e835200c600c/data/latest')
        # optimism = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/889af633-47fd-4bf6-81ea-8337710b1f33/data/latest')
        # osmosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/ead43212-59f5-4507-ab97-5dce45707d74/data/latest')
        # polygon = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/6eaa530c-bce3-441c-b0d0-58ca7397ddde/data/latest')
        # solana = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/6e67fc7b-ade7-4463-9d84-1a965c2ab440/data/latest')
        # thorchain = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/d3ba2a17-4c2f-4127-b01e-7c7f839f55fb/data/latest')
        # return pd.concat(
        #     [arbitrum, avalanche, bsc, ethereum, flow, gnosis, near, optimism, osmosis, polygon, solana, thorchain]
        #         ).sort_values(['Day', 'Hour', 'Blockchain']).reset_index(drop=True)

    elif query == 'Swaps DEXs Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/9e0dace3-69d7-44fb-810c-e3b819b2b8de/data/latest')
        # arbitrum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/28304b7b-ef53-4593-982b-236f8433f08d/data/latest')
        # avalanche = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/3df68b21-6bb1-4784-a729-d847ec4b2c5a/data/latest')
        # bsc = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/39db7d11-998a-45b0-bfa7-4beed1cc637a/data/latest')
        # ethereum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/ef86688e-e670-4009-8382-97bc2d604d4f/data/latest')
        # flow = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/290cd087-a044-4b91-a632-2db4b980a0b0/data/latest')
        # gnosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/25c8e842-68d6-40da-84b9-d1aced72fbe3/data/latest')
        # near = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/ed17a9ad-3553-472f-91e9-10e8a3821081/data/latest')
        # optimism = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/f763bcd2-00ec-4232-92c9-950732454812/data/latest')
        # osmosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/d98bf978-d2aa-4f25-a6cf-94948bf7946e/data/latest')
        # polygon = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/d3c91e0e-9c4f-4684-9f44-41edfff2837d/data/latest')
        # solana = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/9c2ed132-4431-4ad5-b699-eb1914047aac/data/latest')
        # thorchain = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/e77c2584-eda8-4fca-8603-9b6b43dd4b74/data/latest')
        # return pd.concat(
        #     [arbitrum, avalanche, bsc, ethereum, flow, gnosis, near, optimism, osmosis, polygon, solana, thorchain]
        #         ).sort_values('Blockchain').reset_index(drop=True)

    elif query == 'Swaps DEXs Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5563d79a-a937-4e04-a74e-b75f284c57cb/data/latest')
        # arbitrum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/f85c62de-fa93-48ab-9bdb-a817240a6f33/data/latest')
        # avalanche = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/a51e0d19-8bf4-4ca5-be42-ce7e9a0bfcd8/data/latest')
        # bsc = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/4b70f072-d01d-449d-ae4e-924680ac204c/data/latest')
        # ethereum = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/9d1a9b9d-f267-416f-bc1a-ad9374d213c6/data/latest')
        # flow = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/b24cd36f-2198-48f8-9b7e-5a0cb4765c5b/data/latest')
        # gnosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/4ce90e06-4f10-4191-8681-2c684ff505b8/data/latest')
        # near = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/b7f36f44-39dc-486e-8632-c7b9a44a2874/data/latest')
        # optimism = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/c5aaacca-08bb-424b-ad21-aa7b588acccb/data/latest')
        # osmosis = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/7512923d-4d62-497f-a3c5-1a16b815877e/data/latest')
        # polygon = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/d517eab7-ed00-46f0-9c5c-18d4af6254de/data/latest')
        # solana = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/6c3f1328-bd77-4000-8b6b-504c2d0f2189/data/latest')
        # thorchain = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/7fbba281-a095-43c4-82d7-98a685e71ef7/data/latest')
        # return pd.concat(
        #     [arbitrum, avalanche, bsc, ethereum, flow, gnosis, near, optimism, osmosis, polygon, solana, thorchain]
        #         ).sort_values(['Date', 'Blockchain']).reset_index(drop=True)

    # elif query == 'Swaps Overview':
    #     arbitrum = pd.read_json('')
    #     avalanche = pd.read_json('')
    #     axelar = pd.read_json('')
    #     bsc = pd.read_json('')
    #     cosmos = pd.read_json('')
    #     ethereum = pd.read_json('')
    #     flow = pd.read_json('')
    #     gnosis = pd.read_json('')
    #     near = pd.read_json('')
    #     optimism = pd.read_json('')
    #     osmosis = pd.read_json('')
    #     polygon = pd.read_json('')
    #     solana = pd.read_json('')
    #     return pd.concat(
    #         [arbitrum, avalanche, axelar, bsc, cosmos, ethereum, flow, gnosis, near, optimism, osmosis, polygon, solana]
    #             ).sort_values('Blockchain').reset_index(drop=True)

    elif query == 'Transfers Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/41eb418f-d231-4a1f-a1c8-e7cc0ff2fddb/data/latest')

    elif query == 'Transfers Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/76276234-81ba-44fd-8341-7cde62d30abc/data/latest')

    elif query == 'Transfers Heatmap':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/933b930f-b611-469e-9e03-b0d5c5b0242b/data/latest')

    elif query == 'Transfers Distribution':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a17c8548-2834-4600-bc78-a0efb6d12de4/data/latest')

    elif query == 'Transfers Transferring Users':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/2f9e94d0-79b9-49a5-be9a-eb289e9890d4/data/latest')

    elif query == 'Transfers Wallet Types':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/cc07b022-fd08-459f-a9a3-cf8082221414/data/latest')

    elif query == 'Swaps Types Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/770cc6a0-bc32-49fb-942b-84c82da5a533/data/latest')

    elif query == 'Swaps Types Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3ec65249-62fe-49e6-bf85-513af7896e34/data/latest')

    elif query == 'Swaps Assets Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/060d6f19-6e02-4be3-b262-05a91e694986/data/latest')

    elif query == 'Swaps Assets Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/0139649d-6c38-4ee6-9e20-fff34e452fe6/data/latest')
        
    elif query == 'NFTs Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a9dee9b9-bfd8-4fed-b49b-a03767306d89/data/latest')

    elif query == 'NFTs Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6ec4aca1-3d25-4233-bec2-0443b27d3e6c/data/latest')

    elif query == 'NFTs Heatmap':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/62fa2182-ca1b-4648-a363-8d1ce591253e/data/latest')

    elif query == 'NFTs Marketplaces Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8f4e8520-52af-4d57-b29e-e513f62f8fa9/data/latest')

    elif query == 'NFTs Marketplaces Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8fcca211-4bc6-444d-8696-0a583e2966a6/data/latest')

    elif query == 'NFTs Collections Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/eaa5902c-0206-4fd7-8eb4-b15ecf9a71b4/data/latest')

    elif query == 'NFTs Collections Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3cb9e6f6-849b-47e6-8c7e-b454e1394d6b/data/latest')

    return None