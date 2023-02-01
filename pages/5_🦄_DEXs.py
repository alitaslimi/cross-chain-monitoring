# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Global Variables
theme_plotly = None # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='DEXs - Cross Chain Monitoring', page_icon=':bar_chart:', layout='wide')
st.title('🦄 DEXs')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Google Analytics
st.components.v1.html("""
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-PQ45JJR2R7"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-PQ45JJR2R7');
    </script>
""", height=1, scrolling=False)

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
    return None

swaps_dexs_overview = get_data('Swaps DEXs Overview')
swaps_dexs_daily = get_data('Swaps DEXs Daily')

# Filter the blockchains
options = st.multiselect(
    '**Select your desired blockchains:**',
    options=swaps_dexs_overview['Blockchain'].unique(),
    default=swaps_dexs_overview['Blockchain'].unique(),
    key='dexs_options'
)

# Selected Blockchain
if len(options) == 0:
    st.warning('Please select at least one blockchain to see the metrics.')

# Single chain Analysis
elif len(options) == 1:
    st.subheader('Overview')
    df = swaps_dexs_overview.query('Blockchain == @options')
    c1, c2, c3 = st.columns(3)
    with c1:
        fig = px.bar(df, x='DEX', y='Volume', color='DEX', title='Total Swapped Volume')
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Volume [USD]', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.bar(df, x='DEX', y='Volume/Day', color='DEX', title='Average Swapped Volume/Day')
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Daily Volume [USD]', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    with c2:
        fig = px.bar(df, x='DEX', y='Swaps', color='DEX', title='Total Swaps')
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Swaps', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.bar(df, x='DEX', y='Swaps/Day', color='DEX', title='Average Swaps/Day')
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Daily Swaps', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    with c3:
        fig = px.bar(df, x='DEX', y='Swappers', color='DEX', title='Total Swappers')
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Swappers', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.bar(df, x='DEX', y='Swappers/Day', color='DEX', title='Average Swappers/Day')
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Daily Swappers', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    c1, c2 = st.columns(2)
    with c1:
        fig = px.bar(df, x='DEX', y='Volume/Swapper', color='DEX', title='Average Volume/Swapper')
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Volume/Swapper [USD]', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = px.bar(df, x='DEX', y='AmountAverage', color='DEX', title='Average Swapped Amount')
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Average [USD]', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    with c2:
        fig = px.bar(df, x='DEX', y='Swaps/Swapper', color='DEX', title='Average Swaps/Swapper')
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Swaps/Swapper', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.bar(df, x='DEX', y='AmountMedian', color='DEX', title='Median Swapped Amount')
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Median [USD]', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    st.subheader('Market Shares')
    c1, c2, c3 = st.columns(3)
    with c1:
        fig = px.pie(df, values='Volume', names='DEX', title='Share of Total Swapped Volume')
        fig.update_layout(legend_title=None, legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    with c2:
        fig = px.pie(df, values='Swaps', names='DEX', title='Share of Total Swaps')
        fig.update_layout(legend_title=None, legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    with c3:
        fig = px.pie(df, values='Swappers', names='DEX', title='Share of Total Swappers')
        fig.update_layout(legend_title=None, legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    st.subheader('Activity Over Time')
    df = swaps_dexs_daily.query('Blockchain == @options')
    c1, c2 = st.columns(2)
    with c1:
        fig = px.line(df, x='Date', y='Volume', color='DEX', title='Daily Swapped Volume', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Volume [USD]')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.line(df, x='Date', y='Swaps', color='DEX', title='Daily Swaps', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Swaps')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.line(df, x='Date', y='Swappers', color='DEX', title='Daily Swappers', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Swappers')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.line(df, x='Date', y='AmountAverage', color='DEX', title='Daily Average Swapped Amount', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Average [USD]')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    with c2:
        fig = go.Figure()
        for i in df['DEX'].unique():
            fig.add_trace(go.Scatter(
                name=i,
                x=df.query("DEX == @i")['Date'],
                y=df.query("DEX == @i")['Volume'],
                mode='lines',
                stackgroup='one',
                groupnorm='percent'
            ))
        fig.update_layout(title='Daily Share of Swapped Volume')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = go.Figure()
        for i in df['DEX'].unique():
            fig.add_trace(go.Scatter(
                name=i,
                x=df.query("DEX == @i")['Date'],
                y=df.query("DEX == @i")['Swaps'],
                mode='lines',
                stackgroup='one',
                groupnorm='percent'
            ))
        fig.update_layout(title='Daily Share of Swaps')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = go.Figure()
        for i in df['DEX'].unique():
            fig.add_trace(go.Scatter(
                name=i,
                x=df.query("DEX == @i")['Date'],
                y=df.query("DEX == @i")['Swappers'],
                mode='lines',
                stackgroup='one',
                groupnorm='percent'
            ))
        fig.update_layout(title='Daily Share of Swappers')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.line(df, x='Date', y='AmountMedian', color='DEX', title='Daily Median Swapped Amount', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Median [USD]')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Cross Chain Comparison
else:
    st.subheader('Overview')
    df = swaps_dexs_overview.query('Blockchain == @options')

    fig = px.bar(df, x='DEX', y='Volume', color='Blockchain', title='Total Swapped Volume', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Volume [USD]', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    fig = px.bar(df, x='DEX', y='Swaps', color='Blockchain', title='Total Swaps', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Swaps', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    fig = px.bar(df, x='DEX', y='Swappers', color='Blockchain', title='Total Swappers', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Swappers', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    fig = px.histogram(df, x='DEX', y='AmountAverage', color='Blockchain', histfunc='avg', title='Average Swapped Amount', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Average [USD]', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    fig = px.histogram(df, x='DEX', y='AmountMedian', color='Blockchain', histfunc='avg', title='Median Swapped Amount', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Median [USD]', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
    st.subheader('Market Shares')
    c1, c2, c3 = st.columns(3)
    with c1:
        df = swaps_dexs_overview.query('Blockchain == @options')
        df = df.groupby(['DEX']).agg(
            {'Swaps': 'sum', 'Swappers': 'sum', 'Volume': 'sum', 'AmountAverage': 'mean', 'AmountMedian': 'mean'}).reset_index()
        df['RowNumber'] = df['Volume'].rank(method='max', ascending=False)
        df.loc[df['RowNumber'] > 7, 'DEX'] = 'Other'
        fig = px.pie(df, values='Volume', names='DEX', title='Share of Swapped Volume')
        fig.update_layout(legend_title=None, legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    with c2:
        df = swaps_dexs_overview.query('Blockchain == @options')
        df = df.groupby(['DEX']).agg(
            {'Swaps': 'sum', 'Swappers': 'sum', 'Volume': 'sum', 'AmountAverage': 'mean', 'AmountMedian': 'mean'}).reset_index()
        df['RowNumber'] = df['Swaps'].rank(method='max', ascending=False)
        df.loc[df['RowNumber'] > 7, 'DEX'] = 'Other'
        fig = px.pie(df, values='Swaps', names='DEX', title='Share of Swaps')
        fig.update_layout(legend_title=None, legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    with c3:
        df = swaps_dexs_overview.query('Blockchain == @options')
        df = df.groupby(['DEX']).agg(
            {'Swaps': 'sum', 'Swappers': 'sum', 'Volume': 'sum', 'AmountAverage': 'mean', 'AmountMedian': 'mean'}).reset_index()
        df['RowNumber'] = df['Swappers'].rank(method='max', ascending=False)
        df.loc[df['RowNumber'] > 7, 'DEX'] = 'Other'
        fig = px.pie(df, values='Swappers', names='DEX', title='Share of Swappers')
        fig.update_layout(legend_title=None, legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
