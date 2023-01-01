# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Global Variables
theme_plotly = None # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Swapped Assets - Cross Chain Monitoring', page_icon=':bar_chart:', layout='wide')
st.title('💰 Swapped Assets')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Data Sources
@st.cache(ttl=600)
def get_data(data):
    if data == 'Swaps Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b3d90320-3fcb-44f0-b0b9-3f72ee779dcb/data/latest')
    elif data == 'Swaps Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/fed187af-6c8e-49fc-82d1-1975926e3951/data/latest')
    elif data == 'Swaps Heatmap':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3fa50926-77bc-44f8-b190-7bd48d408c85/data/latest')
    elif data == 'Swaps DEXs Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/9e0dace3-69d7-44fb-810c-e3b819b2b8de/data/latest')
    elif data == 'Swaps DEXs Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5563d79a-a937-4e04-a74e-b75f284c57cb/data/latest')
    elif data == 'Swaps Types Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/770cc6a0-bc32-49fb-942b-84c82da5a533/data/latest')
    elif data == 'Swaps Types Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3ec65249-62fe-49e6-bf85-513af7896e34/data/latest')
    elif data == 'Swaps Assets Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/060d6f19-6e02-4be3-b262-05a91e694986/data/latest')
    elif data == 'Swaps Assets Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/0139649d-6c38-4ee6-9e20-fff34e452fe6/data/latest')
    return None

swaps_types_overview = get_data('Swaps Types Overview')
swaps_types_daily = get_data('Swaps Types Daily')
swaps_assets_overview = get_data('Swaps Assets Overview')
swaps_assets_daily = get_data('Swaps Assets Daily')

# Filter the blockchains
options = st.multiselect(
    '**Select your desired blockchains:**',
    options=swaps_types_overview['Blockchain'].unique(),
    default=swaps_types_overview['Blockchain'].unique(),
    key='assets_options'
)

# Selected Blockchain
if len(options) == 0:
    st.warning('Please select at least one blockchain to see the metrics.')

# Single chain Analysis
elif len(options) == 1:
    subtab_types, subtab_assets = st.tabs(['Asset Types', 'Swapped To Assets'])
    
    with subtab_types:
        st.subheader('Overview')
        df = swaps_types_overview.query('Blockchain == @options')
        c1, c2, c3 = st.columns(3)
        with c1:
            fig = px.bar(df, x='Type', y='Volume', color='Type', title='Total Swapped Volume')
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Volume [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.bar(df, x='Type', y='Volume/Day', color='Type', title='Average Swapped Volume/Day')
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Daily Volume [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        with c2:
            fig = px.bar(df, x='Type', y='Swaps', color='Type', title='Total Swaps')
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Swaps', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.bar(df, x='Type', y='Swaps/Day', color='Type', title='Average Swaps/Day')
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Daily Swaps', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        with c3:
            fig = px.bar(df, x='Type', y='Swappers', color='Type', title='Total Swappers')
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Swappers', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.bar(df, x='Type', y='Swappers/Day', color='Type', title='Average Swappers/Day')
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Daily Swappers', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        c1, c2, c3, c4 = st.columns(4)
        with c1:
            fig = px.bar(df, x='Type', y='AmountAverage', color='Type', title='Average Swapped Amount')
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Average [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = px.bar(df, x='Type', y='AmountMedian', color='Type', title='Median Swapped Amount')
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Median [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c3:
            fig = px.bar(df, x='Type', y='Volume/Swapper', color='Type', title='Average Volume/Swapper')
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Volume/Swapper [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c4:
            fig = px.bar(df, x='Type', y='Swaps/Swapper', color='Type', title='Average Swaps/Swapper')
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Swaps/Swapper', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        st.subheader('Market Shares')
        c1, c2, c3 = st.columns(3)
        with c1:
            fig = px.pie(df, values='Volume', names='Type', title='Share of Total Swapped Volume')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = px.pie(df, values='Swaps', names='Type', title='Share of Total Swaps')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c3:
            fig = px.pie(df, values='Swappers', names='Type', title='Share of Total Swappers')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        st.subheader('Activity Over Time')
        c1, c2 = st.columns(2)
        df = swaps_types_daily.query('Blockchain == @options')
        c1, c2 = st.columns(2)
        with c1:
            fig = px.line(df, x='Date', y='Volume', color='Type', title='Daily Swapped Volume', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Volume [USD]')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df, x='Date', y='Swaps', color='Type', title='Daily Swaps', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Swaps')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df, x='Date', y='Swappers', color='Type', title='Daily Swappers', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Swappers')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df, x='Date', y='AmountAverage', color='Type', title='Daily Average Swapped Amount', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Average [USD]')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        with c2:
            fig = go.Figure()
            for i in df['Type'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Type == @i")['Date'],
                    y=df.query("Type == @i")['Volume'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swapped Volume')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = go.Figure()
            for i in df['Type'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Type == @i")['Date'],
                    y=df.query("Type == @i")['Swaps'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swaps')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = go.Figure()
            for i in df['Type'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Type == @i")['Date'],
                    y=df.query("Type == @i")['Swappers'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swappers')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df, x='Date', y='AmountMedian', color='Type', title='Daily Median Swapped Amount', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Median [USD]')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
    with subtab_assets:
        st.subheader('Overview')
        df = swaps_assets_overview.query('Blockchain == @options')

        fig = px.bar(df.sort_values('Volume', ascending=False).head(30), x='Asset', y='Volume', color='Asset', title='Total Swapped Volume', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Volume [USD]', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        c1, c2 = st.columns(2)
        with c1:
            fig = px.bar(df.sort_values('Swaps', ascending=False).head(20), x='Asset', y='Swaps', color='Asset', title='Total Swaps', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Swaps', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.bar(df.sort_values('Swappers', ascending=False).head(20), x='Asset', y='Swappers', color='Asset', title='Total Swappers', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Swappers', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = px.histogram(df.sort_values('AmountAverage', ascending=False).head(20), x='Asset', y='AmountAverage', color='Asset', histfunc='avg', title='Average Swapped Amount', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Average [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.histogram(df.sort_values('AmountMedian', ascending=False).head(20), x='Asset', y='AmountMedian', color='Asset', histfunc='avg', title='Median Swapped Amount', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Median [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        st.subheader('Market Shares')
        c1, c2, c3 = st.columns(3)
        with c1:
            df = swaps_assets_overview.query('Blockchain == @options')
            df['RowNumber'] = df['Volume'].rank(method='max', ascending=False)
            df.loc[df['RowNumber'] > 7, 'Asset'] = 'Other'
            fig = px.pie(df, values='Volume', names='Asset', title='Share of Swapped Volume')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            df = swaps_assets_overview.query('Blockchain == @options')
            df['RowNumber'] = df['Swaps'].rank(method='max', ascending=False)
            df.loc[df['RowNumber'] > 7, 'Asset'] = 'Other'
            fig = px.pie(df, values='Swaps', names='Asset', title='Share of Swaps')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c3:
            df = swaps_assets_overview.query('Blockchain == @options')
            df['RowNumber'] = df['Swappers'].rank(method='max', ascending=False)
            df.loc[df['RowNumber'] > 7, 'Asset'] = 'Other'
            fig = px.pie(df, values='Swappers', names='Asset', title='Share of Swappers')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        st.subheader('Activity Over Time')

        df = swaps_assets_daily.query('Blockchain == @options')
        df['RowNumber'] = df.groupby('Date')['Volume'].rank(method='max', ascending=False)
        df.loc[df['RowNumber'] > 5, 'Asset'] = 'Other'
        df = df.groupby(['Date', 'Asset']).agg(
            {'Swaps': 'sum', 'Swappers': 'sum', 'Volume': 'sum', 'AmountAverage': 'mean', 'AmountMedian': 'mean'}).reset_index()

        c1, c2 = st.columns(2)
        with c1:
            fig = px.bar(df.sort_values(['Date', 'Volume'], ascending=[True, False]), x='Date', y='Volume', color='Asset', title='Daily Swapped Volume of Top Assets By Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Volume [USD]')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.bar(df.sort_values(['Date', 'Swaps'], ascending=[True, False]), x='Date', y='Swaps', color='Asset', title='Daily Swaps of Top Assets By Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Swaps')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = px.bar(df.sort_values(['Date', 'Swappers'], ascending=[True, False]), x='Date', y='Swappers', color='Asset', title='Daily Swappers of Top Assets By Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Swappers')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df.sort_values(['Date', 'AmountAverage'], ascending=[True, False]), x='Date', y='AmountAverage', color='Asset', title='Daily Average Swapped Amount of Top Assets By Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Average Amount [USD]')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = go.Figure()
            for i in df['Asset'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Asset == @i")['Date'],
                    y=df.query("Asset == @i")['Volume'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swapped Volume of Top Assets By Volume')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = go.Figure()
            for i in df['Asset'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Asset == @i")['Date'],
                    y=df.query("Asset == @i")['Swaps'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swaps of Top Assets By Volume')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = go.Figure()
            for i in df['Asset'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Asset == @i")['Date'],
                    y=df.query("Asset == @i")['Swappers'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swappers of Top Assets By Volume')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df.sort_values(['Date', 'AmountMedian'], ascending=[True, False]), x='Date', y='AmountMedian', color='Asset', title='Daily Median Swapped Amount of Top Assets By Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Median Amount [USD]')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Cross Chain Comparison
else:
    subtab_types, subtab_assets = st.tabs(['Asset Types', 'Swapped To Assets'])
    with subtab_types:
        st.subheader('Overview')
        df = swaps_types_overview.query('Blockchain == @options')
        fig = px.bar(df, x='Blockchain', y='Volume', color='Type', title='Swapped Volume of Each Asset Type', log_y=True, barmode='group')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Volume [USD]', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        c1, c2 = st.columns(2)
        with c1:
            fig = px.bar(df, x='Blockchain', y='Swaps', color='Type', title='Swaps of Each Asset Type', log_y=True, barmode='group')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Swaps', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = px.bar(df, x='Blockchain', y='Swappers', color='Type', title='Swappers of Each Asset Type', log_y=True, barmode='group')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Swappers', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        st.subheader('Market Shares')
        df = swaps_types_overview.query('Blockchain == @options')
        c1, c2, c3 = st.columns(3)
        with c1:
            fig = px.pie(df, values='Volume', names='Type', title='Share of Total Swapped Volume')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.histogram(df, x='Blockchain', y='Volume', color='Type', title='Share of Swapped Volume', barnorm='percent')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = px.pie(df, values='Swaps', names='Type', title='Share of Total Swaps')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.histogram(df, x='Blockchain', y='Swaps', color='Type', title='Share of Swaps', barnorm='percent')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c3:
            fig = px.pie(df, values='Swappers', names='Type', title='Share of Total Swappers')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.histogram(df, x='Blockchain', y='Swappers', color='Type', title='Share of Swappers', barnorm='percent')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    with subtab_assets:
        st.subheader('Overview')
        df = swaps_assets_overview.query('Blockchain == @options')

        fig = px.bar(df.sort_values('Volume', ascending=False).head(50), x='Asset', y='Volume', color='Blockchain', title='Total Swapped Volume', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Volume [USD]', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.bar(df.sort_values('Volume', ascending=False).head(50), x='Asset', y='Swaps', color='Blockchain', title='Total Swaps', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Swaps', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.bar(df.sort_values('Volume', ascending=False).head(50), x='Asset', y='Swappers', color='Blockchain', title='Total Swappers', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Swappers', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.histogram(df.sort_values('Volume', ascending=False).head(50), x='Asset', y='AmountAverage', color='Blockchain', histfunc='avg', title='Average Swapped Amount', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Average [USD]', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.histogram(df.sort_values('Volume', ascending=False).head(50), x='Asset', y='AmountMedian', color='Blockchain', histfunc='avg', title='Median Swapped Amount', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Median [USD]', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        st.subheader('Market Shares')
        c1, c2, c3 = st.columns(3)
        with c1:
            df = swaps_assets_overview.query('Blockchain == @options')
            df = df.groupby(['Asset']).agg(
                {'Swaps': 'sum', 'Swappers': 'sum', 'Volume': 'sum', 'AmountAverage': 'mean', 'AmountMedian': 'mean'}).reset_index()
            df['RowNumber'] = df['Volume'].rank(method='max', ascending=False)
            df.loc[df['RowNumber'] > 7, 'Asset'] = 'Other'
            fig = px.pie(df, values='Volume', names='Asset', title='Share of Swapped Volume')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            df = swaps_assets_overview.query('Blockchain == @options')
            df = df.groupby(['Asset']).agg(
                {'Swaps': 'sum', 'Swappers': 'sum', 'Volume': 'sum', 'AmountAverage': 'mean', 'AmountMedian': 'mean'}).reset_index()
            df['RowNumber'] = df['Swaps'].rank(method='max', ascending=False)
            df.loc[df['RowNumber'] > 7, 'Asset'] = 'Other'
            fig = px.pie(df, values='Swaps', names='Asset', title='Share of Swaps')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c3:
            df = swaps_assets_overview.query('Blockchain == @options')
            df = df.groupby(['Asset']).agg(
                {'Swaps': 'sum', 'Swappers': 'sum', 'Volume': 'sum', 'AmountAverage': 'mean', 'AmountMedian': 'mean'}).reset_index()
            df['RowNumber'] = df['Swappers'].rank(method='max', ascending=False)
            df.loc[df['RowNumber'] > 7, 'Asset'] = 'Other'
            fig = px.pie(df, values='Swappers', names='Asset', title='Share of Swappers')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        st.subheader('Activity Over Time')

        df = swaps_assets_daily.query('Blockchain == @options')
        df = df.groupby(['Date', 'Asset']).agg(
            {'Swaps': 'sum', 'Swappers': 'sum', 'Volume': 'sum', 'AmountAverage': 'mean', 'AmountMedian': 'mean'}).reset_index()
        df['RowNumber'] = df.groupby(['Date'])['Volume'].rank(method='max', ascending=False)
        df.loc[df['RowNumber'] > 5, 'Asset'] = 'Other'
        df = df.groupby(['Date', 'Asset']).agg(
            {'Swaps': 'sum', 'Swappers': 'sum', 'Volume': 'sum', 'AmountAverage': 'mean', 'AmountMedian': 'mean'}).reset_index()

        c1, c2 = st.columns(2)
        with c1:
            fig = px.bar(df.sort_values(['Date', 'Volume'], ascending=[True, False]), x='Date', y='Volume', color='Asset', title='Daily Swapped Volume of Top Assets By Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Volume [USD]')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.bar(df.sort_values(['Date', 'Swaps'], ascending=[True, False]), x='Date', y='Swaps', color='Asset', title='Daily Swaps of Top Assets By Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Swaps')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = px.bar(df.sort_values(['Date', 'Swappers'], ascending=[True, False]), x='Date', y='Swappers', color='Asset', title='Daily Swappers of Top Assets By Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Swappers')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df.sort_values(['Date', 'AmountAverage'], ascending=[True, False]), x='Date', y='AmountAverage', color='Asset', log_y=True, title='Daily Average Swapped Amount of Top Assets By Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Average Amount [USD]')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = go.Figure()
            for i in df['Asset'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Asset == @i")['Date'],
                    y=df.query("Asset == @i")['Volume'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swapped Volume of Top Assets By Volume')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = go.Figure()
            for i in df['Asset'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Asset == @i")['Date'],
                    y=df.query("Asset == @i")['Swaps'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swaps of Top Assets By Volume')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = go.Figure()
            for i in df['Asset'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Asset == @i")['Date'],
                    y=df.query("Asset == @i")['Swappers'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swappers of Top Assets By Volume')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df.sort_values(['Date', 'AmountMedian'], ascending=[True, False]), x='Date', y='AmountMedian', color='Asset', log_y=True, title='Daily Median Swapped Amount of Top Assets By Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Median Amount [USD]')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)