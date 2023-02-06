# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import data

# Global Variables
theme_plotly = None # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Config
st.set_page_config(page_title='Swaps - Cross Chain Monitoring', page_icon=':bar_chart:', layout='wide')

# Title
st.title('🔄 Swaps')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Data Sources
swaps_overview = data.get_data('Swaps Overview')
swaps_daily = data.get_data('Swaps Daily')
swaps_heatmap = data.get_data('Swaps Heatmap')

# Filter
options = st.multiselect(
    '**Select your desired blockchains:**',
    options=swaps_overview['Blockchain'].unique(),
    default=swaps_overview['Blockchain'].unique(),
    key='swaps_options'
)

# Selected Blockchain
if len(options) == 0:
    st.warning('Please select at least one blockchain to see the metrics.')

# Single Chain Analysis
elif len(options) == 1:
    st.subheader('Overview')
    df = swaps_overview.query('Blockchain == @options')
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label='**Total Swapped Volume**', value=str(df['Volume'].map('{:,.0f}'.format).values[0]), help='USD')
        st.metric(label='**Average Swapped Volume/Day**', value=str(df['Volume/Day'].map('{:,.0f}'.format).values[0]), help='USD')
    with c2:
        st.metric(label='**Total Swaps**', value=str(df['Swaps'].map('{:,.0f}'.format).values[0]))
        st.metric(label='**Average Swaps/Day**', value=str(df['Swaps/Day'].map('{:,.0f}'.format).values[0]))
    with c3:
        st.metric(label='**Total Swappers**', value=str(df['Swappers'].map('{:,.0f}'.format).values[0]))
        st.metric(label='**Average Swappers/Day**', value=str(df['Swappers/Day'].map('{:,.0f}'.format).values[0]))
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(label='**Average Swapped Amount**', value=str(df['AmountAverage'].map('{:,.2f}'.format).values[0]), help='USD')
    with c2:
        st.metric(label='**Median Swapped Amount**', value=str(df['AmountMedian'].map('{:,.2f}'.format).values[0]), help='USD')
    with c3:
        st.metric(label='**Average Volume/Swapper**', value=str(df['Volume/Swapper'].map('{:,.0f}'.format).values[0]), help='USD')
    with c4:
        st.metric(label='**Average Swaps/Swapper**', value=str(df['Swaps/Swapper'].map('{:,.0f}'.format).values[0]))

    st.subheader('Activity Over Time')
    df = swaps_daily.query('Blockchain == @options')

    fig = px.area(df, x='Date', y='Volume', title='Daily Swapped Volume of')
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Volume [USD]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    c1, c2 = st.columns(2)
    with c1:
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df['Date'], y=df['Swaps'], name='Swaps'), secondary_y=False)
        fig.add_trace(go.Line(x=df['Date'], y=df['Swappers'], name='Swappers'), secondary_y=True)
        fig.update_layout(title_text='Daily Swaps and Swappers')
        fig.update_yaxes(title_text='Swaps', secondary_y=False)
        fig.update_yaxes(title_text='Swappers', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    with c2:
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df['Date'], y=df['AmountAverage'], name='Average'), secondary_y=False)
        fig.add_trace(go.Line(x=df['Date'], y=df['AmountMedian'], name='Median'), secondary_y=True)
        fig.update_layout(title_text='Daily Average and Median Swapped Amount')
        fig.update_yaxes(title_text='Average [USD]', secondary_y=False)
        fig.update_yaxes(title_text='Median [USD]', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    st.subheader('Activity Heatmap')
    df = swaps_heatmap.query('Blockchain == @options')

    fig = px.density_heatmap(df, x='Hour', y='Day', z='Volume', histfunc='avg', title='Heatmap of Swapped Volume', nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 1}, coloraxis_colorbar=dict(title='Volume [USD]'))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    c1, c2 = st.columns(2)
    with c1:
        fig = px.density_heatmap(df, x='Hour', y='Day', z='Swaps', histfunc='avg', title='Heatmap of Swaps', nbinsx=24)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 2}, coloraxis_colorbar=dict(title='Swaps'))
        fig.update_yaxes(categoryorder='array', categoryarray=week_days)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.density_heatmap(df, x='Hour', y='Day', z='AmountAverage', histfunc='avg', title='Heatmap of Average Swapped Amount', nbinsx=24)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 2}, coloraxis_colorbar=dict(title='Average [USD]'))
        fig.update_yaxes(categoryorder='array', categoryarray=week_days)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    with c2:
        fig = px.density_heatmap(df, x='Hour', y='Day', z='Swappers', histfunc='avg', title='Heatmap of Swappers', nbinsx=24)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 2}, coloraxis_colorbar=dict(title='Swappers'))
        fig.update_yaxes(categoryorder='array', categoryarray=week_days)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.density_heatmap(df, x='Hour', y='Day', z='AmountMedian', histfunc='avg', title='Heatmap of Median Swapped Amount', nbinsx=24)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 2}, coloraxis_colorbar=dict(title='Median [USD]'))
        fig.update_yaxes(categoryorder='array', categoryarray=week_days)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Cross Chain Comparison
else:
    subtab_overview, subtab_heatmap = st.tabs(['Overview', 'Heatmap'])
    with subtab_overview:
        st.subheader('Overview')
        df = swaps_overview.query('Blockchain == @options')
        c1, c2, c3 = st.columns(3)
        with c1:
            fig = px.bar(df, x='Blockchain', y='Volume', color='Blockchain', title='Total Swapped Volume', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Volume [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.bar(df, x='Blockchain', y='Volume/Day', color='Blockchain', title='Average Swapped Volume/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Daily Volume [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        with c2:
            fig = px.bar(df, x='Blockchain', y='Swaps', color='Blockchain', title='Total Swaps', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Swaps', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.bar(df, x='Blockchain', y='Swaps/Day', color='Blockchain', title='Average Swaps/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Daily Swaps', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        with c3:
            fig = px.bar(df, x='Blockchain', y='Swappers', color='Blockchain', title='Total Swappers', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Swappers', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.bar(df, x='Blockchain', y='Swappers/Day', color='Blockchain', title='Average Swappers/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Daily Swappers', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        c1, c2 = st.columns(2)
        with c1:
            fig = px.bar(df, x='Blockchain', y='Volume/Swapper', color='Blockchain', title='Average Volume/Swapper', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Volume/Swapper [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = px.bar(df, x='Blockchain', y='AmountAverage', color='Blockchain', title='Average Swapped Amount', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Average [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = px.bar(df, x='Blockchain', y='Swaps/Swapper', color='Blockchain', title='Average Swaps/Swapper', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Swaps/Swapper', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.bar(df, x='Blockchain', y='AmountMedian', color='Blockchain', title='Median Swapped Amount', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Median [USD]', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        st.subheader('Market Shares')
        c1, c2, c3 = st.columns(3)
        with c1:
            fig = px.pie(df, values='Volume', names='Blockchain', title='Share of Total Swapped Volume')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c2:
            fig = px.pie(df, values='Swaps', names='Blockchain', title='Share of Total Swaps')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        with c3:
            fig = px.pie(df, values='Swappers', names='Blockchain', title='Share of Total Swappers')
            fig.update_layout(legend_title=None, legend_y=0.5)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        st.subheader('Activity Over Time')
        df = swaps_daily.query('Blockchain == @options')
        c1, c2 = st.columns(2)
        with c1:
            fig = px.line(df, x='Date', y='Volume', color='Blockchain', title='Daily Swapped Volume', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Volume [USD]')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df, x='Date', y='Swaps', color='Blockchain', title='Daily Swaps', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Swaps')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df, x='Date', y='Swappers', color='Blockchain', title='Daily Swappers', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Swappers')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df, x='Date', y='AmountAverage', color='Blockchain', title='Daily Average Swapped Amount', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Average [USD]')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        with c2:
            fig = go.Figure()
            for i in options:
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Blockchain == @i")['Date'],
                    y=df.query("Blockchain == @i")['Volume'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swapped Volume')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
            
            fig = go.Figure()
            for i in options:
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Blockchain == @i")['Date'],
                    y=df.query("Blockchain == @i")['Swaps'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swaps')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = go.Figure()
            for i in options:
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Blockchain == @i")['Date'],
                    y=df.query("Blockchain == @i")['Swappers'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swappers')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df, x='Date', y='AmountMedian', color='Blockchain', title='Daily Median Swapped Amount', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Median [USD]')
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    with subtab_heatmap:
        st.subheader('Heatmap of Swaps')
        c1, c2 = st.columns(2)
        with c1:
            df = swaps_heatmap.query("Blockchain == @options")
            df['Volume'] = df.groupby('Blockchain')['Volume'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Day', z='Volume', histfunc='avg', title='Daily Heatmap of Normalized Swapped Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            df = swaps_heatmap.query("Blockchain == @options")
            df['Swaps'] = df.groupby('Blockchain')['Swaps'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Day', z='Swaps', histfunc='avg', title='Daily Heatmap of Normalized Swaps')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            df = swaps_heatmap.query("Blockchain == @options")
            df['Swappers'] = df.groupby('Blockchain')['Swappers'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Day', z='Swappers', histfunc='avg', title='Daily Heatmap of Normalized Swappers')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            df = swaps_heatmap.query("Blockchain == @options")
            df['AmountAverage'] = df.groupby('Blockchain')['AmountAverage'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Day', z='AmountAverage', histfunc='avg', title='Daily Heatmap of Normalized Average Swapped Amount')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            df = swaps_heatmap.query("Blockchain == @options")
            df['AmountMedian'] = df.groupby('Blockchain')['AmountMedian'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Day', z='AmountMedian', histfunc='avg', title='Daily Heatmap of Normalized Median Swapped Amount')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        with c2:
            df = swaps_heatmap.query("Blockchain == @options")
            df['Volume'] = df.groupby('Blockchain')['Volume'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Hour', z='Volume', histfunc='avg', title='Hourly Heatmap of Normalized Swapped Volume', nbinsy=24)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days, dtick=2)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            df = swaps_heatmap.query("Blockchain == @options")
            df['Swaps'] = df.groupby('Blockchain')['Swaps'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Hour', z='Swaps', histfunc='avg', title='Hourly Heatmap of Normalized Swaps', nbinsy=24)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days, dtick=2)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            df = swaps_heatmap.query("Blockchain == @options")
            df['Swappers'] = df.groupby('Blockchain')['Swappers'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Hour', z='Swappers', histfunc='avg', title='Hourly Heatmap of Normalized Swappers', nbinsy=24)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days, dtick=2)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            df = swaps_heatmap.query("Blockchain == @options")
            df['AmountAverage'] = df.groupby('Blockchain')['AmountAverage'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Hour', z='AmountAverage', histfunc='avg', title='Hourly Heatmap of Normalized Average Swapped Amount', nbinsy=24)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days, dtick=2)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            df = swaps_heatmap.query("Blockchain == @options")
            df['AmountMedian'] = df.groupby('Blockchain')['AmountMedian'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
            fig = px.density_heatmap(df, x='Blockchain', y='Hour', z='AmountMedian', histfunc='avg', title='Hourly Heatmap of Normalized Average Swapped Amount', nbinsy=24)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, coloraxis_colorbar=dict(title='Min/Max'))
            fig.update_xaxes(categoryorder='category ascending')
            fig.update_yaxes(categoryorder='array', categoryarray=week_days, dtick=2)
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)