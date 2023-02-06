# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import data

# Global Variables
theme_plotly = None # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Config
st.set_page_config(page_title='NFT Marketplaces - Cross Chain Monitoring', page_icon=':bar_chart:', layout='wide')

# Title
st.title('🛒 NFT Marketplaces')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Data Sources
nfts_marketplaces_overview = data.get_data('NFTs Marketplaces Overview')
nfts_marketplaces_daily = data.get_data('NFTs Marketplaces Daily')

# Filter
options = st.multiselect(
    '**Select your desired blockchains:**',
    options=nfts_marketplaces_overview['Blockchain'].unique(),
    default=nfts_marketplaces_overview['Blockchain'].unique(),
    key='marketplaces_options'
)

# Selected Blockchain
if len(options) == 0:
    st.warning('Please select at least one blockchain to see the metrics.')

# Single Chain Analysis
elif len(options) == 1:
    st.subheader('Overview')
    df = nfts_marketplaces_overview.query('Blockchain == @options')
    c1, c2 = st.columns(2)
    with c1:
        fig = px.bar(df, x='Marketplace', y='Volume', color='Marketplace', title='Total Sales Volume', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Volume [USD]', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    with c2:
        fig = px.bar(df, x='Marketplace', y='Sales', color='Marketplace', title='Total Sales', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Sales', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    c1, c2, c3 = st.columns(3)
    with c1:
        fig = px.bar(df, x='Marketplace', y='Buyers', color='Marketplace', title='Total Buyers', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Buyers', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.bar(df, x='Marketplace', y='PriceAverage', color='Marketplace', title='Average NFT Prices', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Average [USD]', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    with c2:
        fig = px.bar(df, x='Marketplace', y='NFTs', color='Marketplace', title='Total Traded NFTs', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='NFTs', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.bar(df, x='Marketplace', y='PriceMedian', color='Marketplace', title='Median NFT Prices', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Median [USD]', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    with c3:
        fig = px.bar(df, x='Marketplace', y='Collections', color='Marketplace', title='Total Traded Collections', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Collections', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.bar(df, x='Marketplace', y='PriceMax', color='Marketplace', title='Maximum NFT Prices', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Maximum [USD]', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
    st.subheader('Market Shares')
    c1, c2 = st.columns(2)
    with c1:
        fig = px.pie(df, values='Volume', names='Marketplace', title='Share of Total Sales Volume')
        fig.update_layout(legend_title=None, legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    with c2:
        fig = px.pie(df, values='Sales', names='Marketplace', title='Share of Total Sales')
        fig.update_layout(legend_title=None, legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    c1, c2, c3 = st.columns(3)
    with c1:
        fig = px.pie(df, values='Buyers', names='Marketplace', title='Share of Total Buyers')
        fig.update_layout(legend_title=None, legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    with c2:
        fig = px.pie(df, values='NFTs', names='Marketplace', title='Share of Traded NFTs')
        fig.update_layout(legend_title=None, legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    with c3:
        fig = px.pie(df, values='Collections', names='Marketplace', title='Share of Total Traded Collections')
        fig.update_layout(legend_title=None, legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
    st.subheader('Activity Over Time')
    df = nfts_marketplaces_daily.query('Blockchain == @options')
    c1, c2 = st.columns(2)
    with c1:
        fig = px.line(df, x='Date', y='Volume', color='Marketplace', title='Daily Sales Volume', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Volume [USD]')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.line(df, x='Date', y='Sales', color='Marketplace', title='Daily Sales', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Sales')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = px.line(df, x='Date', y='Buyers', color='Marketplace', title='Daily Buyers', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Buyers')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = px.line(df, x='Date', y='NFTs', color='Marketplace', title='Daily Traded NFTs', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='NFTs')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = px.line(df, x='Date', y='Collections', color='Marketplace', title='Daily Traded Collections', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Collections')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    with c2:
        fig = go.Figure()
        for i in df['Marketplace'].unique():
            fig.add_trace(go.Scatter(
                name=i,
                x=df.query("Marketplace == @i")['Date'],
                y=df.query("Marketplace == @i")['Volume'],
                mode='lines',
                stackgroup='one',
                groupnorm='percent'
            ))
        fig.update_layout(title='Daily Share of Sales Volume')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = go.Figure()
        for i in df['Marketplace'].unique():
            fig.add_trace(go.Scatter(
                name=i,
                x=df.query("Marketplace == @i")['Date'],
                y=df.query("Marketplace == @i")['Sales'],
                mode='lines',
                stackgroup='one',
                groupnorm='percent'
            ))
        fig.update_layout(title='Daily Share of Sales')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = go.Figure()
        for i in df['Marketplace'].unique():
            fig.add_trace(go.Scatter(
                name=i,
                x=df.query("Marketplace == @i")['Date'],
                y=df.query("Marketplace == @i")['Buyers'],
                mode='lines',
                stackgroup='one',
                groupnorm='percent'
            ))
        fig.update_layout(title='Daily Share of Buyers')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = go.Figure()
        for i in df['Marketplace'].unique():
            fig.add_trace(go.Scatter(
                name=i,
                x=df.query("Marketplace == @i")['Date'],
                y=df.query("Marketplace == @i")['NFTs'],
                mode='lines',
                stackgroup='one',
                groupnorm='percent'
            ))
        fig.update_layout(title='Daily Share of Traded NFTs')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = go.Figure()
        for i in df['Marketplace'].unique():
            fig.add_trace(go.Scatter(
                name=i,
                x=df.query("Marketplace == @i")['Date'],
                y=df.query("Marketplace == @i")['Collections'],
                mode='lines',
                stackgroup='one',
                groupnorm='percent'
            ))
        fig.update_layout(title='Daily Share of Traded Collections')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
    fig = px.line(df, x='Date', y='PriceAverage', color='Marketplace', title='Daily Average NFT Prices', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Collections')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    c1, c2 = st.columns(2)
    with c1:
        fig = px.line(df, x='Date', y='PriceMedian', color='Marketplace', title='Daily Median NFT Prices', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Collections')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    with c2:
        fig = px.line(df, x='Date', y='PriceMax', color='Marketplace', title='Daily Maximum NFT Prices', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Collections')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Cross Chain Comparison
else:
    subtab_overview, subtab_prices = st.tabs(['Overview', 'Prices'])
    with subtab_overview:
        st.subheader('Overview')
        df = nfts_marketplaces_overview.query('Blockchain == @options')

        fig = px.bar(df, x='Marketplace', y='Sales', color='Blockchain', title='Total Sales Volume', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Volume [USD]', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        c1, c2 = st.columns(2)
        with c1:
            fig = px.bar(df, x='Marketplace', y='Sales', color='Blockchain', title='Total Sales', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Sales', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.bar(df, x='Marketplace', y='NFTs', color='Blockchain', title='Total Traded NFTs', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='NFTs', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = px.bar(df, x='Marketplace', y='Buyers', color='Blockchain', title='Total Buyers', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Buyers', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.bar(df, x='Marketplace', y='Collections', color='Blockchain', title='Total Traded Collections', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Collections', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        st.subheader('Market Shares')
        c1, c2 = st.columns(2)
        with c1:
            df = nfts_marketplaces_overview.query('Blockchain == @options')
            df = df.groupby(['Marketplace']).agg(
                {'Sales': 'sum', 'Buyers': 'sum', 'Volume': 'sum', 'NFTs': 'sum', 'Collections': 'sum',
                    'PriceAverage': 'mean', 'PriceMedian': 'mean', 'PriceMax': 'mean'}).reset_index()
            df['RowNumber'] = df['Volume'].rank(method='max', ascending=False)
            df.loc[df['RowNumber'] > 7, 'Marketplace'] = 'Other'
            fig = px.pie(df, values='Volume', names='Marketplace', title='Share of Total Sales Volume')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            df = nfts_marketplaces_overview.query('Blockchain == @options')
            df = df.groupby(['Marketplace']).agg(
                {'Sales': 'sum', 'Buyers': 'sum', 'Volume': 'sum', 'NFTs': 'sum', 'Collections': 'sum',
                    'PriceAverage': 'mean', 'PriceMedian': 'mean', 'PriceMax': 'mean'}).reset_index()
            df['RowNumber'] = df['Sales'].rank(method='max', ascending=False)
            df.loc[df['RowNumber'] > 7, 'Marketplace'] = 'Other'
            fig = px.pie(df, values='Sales', names='Marketplace', title='Share of Total Sales')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        c1, c2, c3 = st.columns(3)
        with c1:
            df = nfts_marketplaces_overview.query('Blockchain == @options')
            df = df.groupby(['Marketplace']).agg(
                {'Sales': 'sum', 'Buyers': 'sum', 'Volume': 'sum', 'NFTs': 'sum', 'Collections': 'sum',
                    'PriceAverage': 'mean', 'PriceMedian': 'mean', 'PriceMax': 'mean'}).reset_index()
            df['RowNumber'] = df['Buyers'].rank(method='max', ascending=False)
            df.loc[df['RowNumber'] > 7, 'Marketplace'] = 'Other'
            fig = px.pie(df, values='Buyers', names='Marketplace', title='Share of Total Buyers')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            df = nfts_marketplaces_overview.query('Blockchain == @options')
            df = df.groupby(['Marketplace']).agg(
                {'Sales': 'sum', 'Buyers': 'sum', 'Volume': 'sum', 'NFTs': 'sum', 'Collections': 'sum',
                    'PriceAverage': 'mean', 'PriceMedian': 'mean', 'PriceMax': 'mean'}).reset_index()
            df['RowNumber'] = df['NFTs'].rank(method='max', ascending=False)
            df.loc[df['RowNumber'] > 7, 'Marketplace'] = 'Other'
            fig = px.pie(df, values='NFTs', names='Marketplace', title='Share of Traded NFTs')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c3:
            df = nfts_marketplaces_overview.query('Blockchain == @options')
            df = df.groupby(['Marketplace']).agg(
                {'Sales': 'sum', 'Buyers': 'sum', 'Volume': 'sum', 'NFTs': 'sum', 'Collections': 'sum',
                    'PriceAverage': 'mean', 'PriceMedian': 'mean', 'PriceMax': 'mean'}).reset_index()
            df['RowNumber'] = df['Collections'].rank(method='max', ascending=False)
            df.loc[df['RowNumber'] > 7, 'Marketplace'] = 'Other'
            fig = px.pie(df, values='Collections', names='Marketplace', title='Share of Total Traded Collections')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        st.subheader('Activity Over Time')

        df = nfts_marketplaces_daily.query('Blockchain == @options')
        df = df.groupby(['Date', 'Marketplace']).agg(
            {'Sales': 'sum', 'Buyers': 'sum', 'Volume': 'sum', 'NFTs': 'sum', 'Collections': 'sum',
                'PriceAverage': 'mean', 'PriceMedian': 'mean', 'PriceMax': 'mean'}).reset_index()
        df['RowNumber'] = df.groupby(['Date'])['Volume'].rank(method='max', ascending=False)
        df.loc[df['RowNumber'] > 5, 'Marketplace'] = 'Other'
        df = df.groupby(['Date', 'Marketplace']).agg(
            {'Sales': 'sum', 'Buyers': 'sum', 'Volume': 'sum', 'NFTs': 'sum', 'Collections': 'sum',
                'PriceAverage': 'mean', 'PriceMedian': 'mean', 'PriceMax': 'mean'}).reset_index()

        c1, c2 = st.columns(2)
        with c1:
            fig = px.bar(df.sort_values(['Date', 'Volume'], ascending=[True, False]), x='Date', y='Volume', color='Marketplace', title='Daily Sales Volume of Top Marketplaces By Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Volume [USD]')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.bar(df.sort_values(['Date', 'Sales'], ascending=[True, False]), x='Date', y='Sales', color='Marketplace', title='Daily Sales of Top Marketplaces By Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Sales')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = px.bar(df.sort_values(['Date', 'Buyers'], ascending=[True, False]), x='Date', y='Buyers', color='Marketplace', title='Daily Buyers of Top Marketplaces By Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Buyers')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = px.bar(df.sort_values(['Date', 'NFTs'], ascending=[True, False]), x='Date', y='NFTs', color='Marketplace', title='Daily Traded NFTs of Top Marketplaces By Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='NFTs')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = px.bar(df.sort_values(['Date', 'Collections'], ascending=[True, False]), x='Date', y='Collections', color='Marketplace', title='Daily Traded Collections of Top Marketplaces By Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Collections')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
           
        with c2:
            fig = go.Figure()
            for i in df['Marketplace'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Marketplace == @i")['Date'],
                    y=df.query("Marketplace == @i")['Volume'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Sales Volume of Top Marketplaces By Volume')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = go.Figure()
            for i in df['Marketplace'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Marketplace == @i")['Date'],
                    y=df.query("Marketplace == @i")['Sales'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Sales of Top Marketplaces By Volume')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = go.Figure()
            for i in df['Marketplace'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Marketplace == @i")['Date'],
                    y=df.query("Marketplace == @i")['Buyers'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Buyers of Top Marketplaces By Volume')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = go.Figure()
            for i in df['Marketplace'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Marketplace == @i")['Date'],
                    y=df.query("Marketplace == @i")['NFTs'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Traded NFTs of Top Marketplaces By Volume')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = go.Figure()
            for i in df['Marketplace'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Marketplace == @i")['Date'],
                    y=df.query("Marketplace == @i")['Collections'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Traded Collections of Top Marketplaces By Volume')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
    with subtab_prices:
        st.subheader('Overview')
        df = nfts_marketplaces_overview.query('Blockchain == @options')
        
        fig = px.histogram(df, x='Marketplace', y='PriceAverage', color='Blockchain', histfunc='avg', title='Average NFT Prices', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Average [USD]', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        c1, c2 = st.columns(2)
        with c1:
            fig = px.histogram(df, x='Marketplace', y='PriceMedian', color='Blockchain', histfunc='avg', title='Median NFT Prices', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Median [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = px.histogram(df, x='Marketplace', y='PriceMax', color='Blockchain', histfunc='avg', title='Maximum NFT Prices', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Maximum [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        st.subheader('Activity Over Time')

        df = nfts_marketplaces_daily.query('Blockchain == @options')
        df = df.groupby(['Date', 'Marketplace']).agg(
            {'Sales': 'sum', 'Buyers': 'sum', 'Volume': 'sum', 'NFTs': 'sum', 'Collections': 'sum',
                'PriceAverage': 'mean', 'PriceMedian': 'mean', 'PriceMax': 'mean'}).reset_index()
        df['RowNumber'] = df.groupby(['Date'])['Volume'].rank(method='max', ascending=False)
        df.loc[df['RowNumber'] > 5, 'Marketplace'] = 'Other'
        df = df.groupby(['Date', 'Marketplace']).agg(
            {'Sales': 'sum', 'Buyers': 'sum', 'Volume': 'sum', 'NFTs': 'sum', 'Collections': 'sum',
                'PriceAverage': 'mean', 'PriceMedian': 'mean', 'PriceMax': 'mean'}).reset_index()

        fig = px.line(df.sort_values(['Date', 'PriceAverage'], ascending=[True, False]), x='Date', y='PriceAverage', color='Marketplace', log_y=True, title='Daily Average NFT Prices of Top Marketplaces By Volume')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Average Price [USD]')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        c1, c2 = st.columns(2)
        with c1:
            fig = px.line(df.sort_values(['Date', 'PriceMedian'], ascending=[True, False]), x='Date', y='PriceMedian', color='Marketplace', log_y=True, title='Daily Median NFT Prices of Top Marketplaces By Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Median Price [USD]')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = px.line(df.sort_values(['Date', 'PriceMax'], ascending=[True, False]), x='Date', y='PriceMax', color='Marketplace', log_y=True, title='Daily Maximum NFT Prices of Top Marketplaces By Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Maximum Price [USD]')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)