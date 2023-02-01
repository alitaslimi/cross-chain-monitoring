# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Global Variables
theme_plotly = None # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Macro - Cross Chain Monitoring', page_icon=':bar_chart:', layout='wide')
st.title('🌍 Macro KPIs')

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
def get_data(query):
    if query == 'Transactions Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/579714e6-986e-421a-85dd-c32a8b41b25c/data/latest')
    elif query == 'Transactions Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4e0c69ff-9395-43c1-af49-f590f864d339/data/latest')
    elif query == 'Transactions Heatmap':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/9d8d54d4-b700-4d85-af17-8c29aa29d334/data/latest')
    elif query == 'Transactions Fee Payers':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7eae69ea-2387-420d-b4b9-6eceeb5ef22d/data/latest')
    elif query == 'Transactions New Users':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d81c5861-0792-43ec-9f92-d89fbcf85e79/data/latest')
    return None

transactions_overview = get_data('Transactions Overview')
transactions_daily = get_data('Transactions Daily')
transactions_heatmap = get_data('Transactions Heatmap')
transactions_new_users = get_data('Transactions New Users')

# Filter the blockchains
options = st.multiselect(
    '**Select your desired blockchains:**',
    options=transactions_overview['Blockchain'].unique(),
    default=transactions_overview['Blockchain'].unique(),
    key='macro_options'
)

# Selected Blockchain
if len(options) == 0:
    st.warning('Please select at least one blockchain to see the metrics.')

# Single chain Analysis
elif len(options) == 1:
    st.subheader('Overview')
    df = transactions_overview.query("Blockchain == @options")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label='**Total Blocks**', value=str(df['Blocks'].map('{:,.0f}'.format).values[0]))
        st.metric(label='**Average Transactions/Block**', value=str(df['Transactions/Block'].map('{:,.0f}'.format).values[0]))
    with c2:
        st.metric(label='**Total Transactions**', value=str(df['Transactions'].map('{:,.0f}'.format).values[0]))
        st.metric(label='**Average TPS**', value=str(df['TPS'].map('{:,.2f}'.format).values[0]))
    with c3:
        st.metric(label='**Total Unique Addresses**', value=str(df['Users'].map('{:,.0f}'.format).values[0]))
        st.metric(label='**Average Daily Active Users**', value=str(df['Users/Day'].map('{:,.0f}'.format).values[0]))
    
    st.subheader('Activity Over Time')
    df = transactions_daily.query("Blockchain == @options")
    dfnu = transactions_new_users.query("Blockchain == @options")
    
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df['Date'], y=df['Transactions'], name='Transactions'), secondary_y=False)
    fig.add_trace(go.Line(x=df['Date'], y=df['Blocks'], name='Blocks'), secondary_y=True)
    fig.update_layout(title_text='Daily Transactions and Blocks')
    fig.update_yaxes(title_text='Transactions', secondary_y=False)
    fig.update_yaxes(title_text='Blocks', secondary_y=True)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    fig = sp.make_subplots()
    fig.add_trace(go.Bar(x=df['Date'], y=df['Users'], name='Active Users'))
    fig.add_trace(go.Line(x=dfnu['Date'], y=dfnu['NewUsers'], name='New Users'))
    fig.update_layout(title_text='Daily Active and New Addresses')
    fig.update_yaxes(title_text='Users')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df['Date'], y=df['TPS'], name='TPS'), secondary_y=False)
    fig.add_trace(go.Line(x=df['Date'], y=df['Transactions/Block'], name='Transactions/Block'), secondary_y=True)
    fig.update_layout(title_text='Daily Average TPS and Transactions/Block')
    fig.update_yaxes(title_text='Transactions/Second', secondary_y=False)
    fig.update_yaxes(title_text='Transactions/Block', secondary_y=True)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    st.subheader('Activity Heatmap')
    df = transactions_heatmap.query('Blockchain == @options')

    fig = px.density_heatmap(df, x='Hour', y='Day', z='Transactions', histfunc='avg', title='Heatmap of Transactions', nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 1}, coloraxis_colorbar=dict(title='Transactions'))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    fig = px.density_heatmap(df, x='Hour', y='Day', z='Users', histfunc='avg', title='Heatmap of Active Addresses', nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 1}, coloraxis_colorbar=dict(title='Users'))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    fig = px.density_heatmap(df, x='Hour', y='Day', z='Blocks', histfunc='avg', title='Heatmap of Blocks', nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 1}, coloraxis_colorbar=dict(title='Blocks'))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Cross Chain Comparison
else:
    st.subheader('Overview')
    df = transactions_overview.query('Blockchain == @options')
    c1, c2 = st.columns(2)
    with c1:
        fig = px.bar(df, x='Blockchain', y='Transactions', color='Blockchain', title='Total Transactions', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Transactions', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.bar(df, x='Blockchain', y='TPS', color='Blockchain', title='Average TPS', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Transactions/Second', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    with c2:
        fig = px.bar(df, x='Blockchain', y='Users', color='Blockchain', title='Total Active Addresses', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Users', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.bar(df, x='Blockchain', y='Blocks', color='Blockchain', title='Total Blocks', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Blocks', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    st.subheader('Activity Over Time')
    df = transactions_daily.query('Blockchain == @options')
    dfnu = transactions_new_users.query("Blockchain == @options")

    fig = px.line(df, x='Date', y='Transactions', color='Blockchain', title='Daily Total Transactions', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Transactions')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    fig = px.line(df, x='Date', y='Users', color='Blockchain', title='Daily Active Addresses', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Active Users')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    fig = px.line(dfnu, x='Date', y='NewUsers', color='Blockchain', title='Daily New Addresses', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='New Users')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
    fig = px.line(df, x='Date', y='Blocks', color='Blockchain', title='Daily Blocks', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Blocks')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    st.subheader('Activity Heatmap')

    c1, c2 = st.columns(2)
    with c1:
        df = transactions_heatmap.query('Blockchain == @options')
        df['Transactions'] = df.groupby('Blockchain')['Transactions'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
        fig = px.density_heatmap(df, x='Blockchain', y='Day', z='Transactions', histfunc='avg', title='Daily Heatmap of Normalized Transactions')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
        fig.update_xaxes(categoryorder='category ascending')
        fig.update_yaxes(categoryorder='array', categoryarray=week_days)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        df = transactions_heatmap.query('Blockchain == @options')
        df['Users'] = df.groupby('Blockchain')['Users'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
        fig = px.density_heatmap(df, x='Blockchain', y='Day', z='Users', histfunc='avg', title='Daily Heatmap of Normalized Users')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
        fig.update_xaxes(categoryorder='category ascending')
        fig.update_yaxes(categoryorder='array', categoryarray=week_days)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        df = transactions_heatmap.query('Blockchain == @options')
        df['Blocks'] = df.groupby('Blockchain')['Blocks'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
        fig = px.density_heatmap(df, x='Blockchain', y='Day', z='Blocks', histfunc='avg', title='Daily Heatmap of Normalized Blocks')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
        fig.update_xaxes(categoryorder='category ascending')
        fig.update_yaxes(categoryorder='array', categoryarray=week_days)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    with c2:
        df = transactions_heatmap.query('Blockchain == @options')
        df['Transactions'] = df.groupby('Blockchain')['Transactions'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
        fig = px.density_heatmap(df, x='Blockchain', y='Hour', z='Transactions', histfunc='avg', title='Hourly Heatmap of Normalized Transactions', nbinsy=24)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
        fig.update_xaxes(categoryorder='category ascending')
        fig.update_yaxes(categoryorder='array', categoryarray=week_days, dtick=2)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        df = transactions_heatmap.query('Blockchain == @options')
        df['Users'] = df.groupby('Blockchain')['Users'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
        fig = px.density_heatmap(df, x='Blockchain', y='Hour', z='Users', histfunc='avg', title='Hourly Heatmap of Normalized Users', nbinsy=24)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
        fig.update_xaxes(categoryorder='category ascending')
        fig.update_yaxes(categoryorder='array', categoryarray=week_days, dtick=2)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        df = transactions_heatmap.query('Blockchain == @options')
        df['Blocks'] = df.groupby('Blockchain')['Blocks'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
        fig = px.density_heatmap(df, x='Blockchain', y='Hour', z='Blocks', histfunc='avg', title='Hourly Heatmap of Normalized Blocks', nbinsy=24)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
        fig.update_xaxes(categoryorder='category ascending')
        fig.update_yaxes(categoryorder='array', categoryarray=week_days, dtick=2)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
