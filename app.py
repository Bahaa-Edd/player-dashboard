import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title='Player Performance Dashboard',
                   layout='wide')

df = pd.read_csv('data/players_clustered.csv')

COLORS = {
    'Forward':      '#534AB7',
    'Midfielder':       '#D85A30',
    'Defender': '#BA7517',
    'Goalkeeper':       '#888780'
}

st.title('Player Performance Dashboard')
st.markdown('Transfermarkt data — K-Means playstyle clustering')

col1, col2, col3 = st.columns(3)
col1.metric('Total players', f"{df.shape[0]:,}")
col2.metric('Playstyle clusters', df['playstyle'].nunique())
col3.metric('Avg market value',
            f"€{df['market_value_in_eur'].mean()/1e6:.1f}M")

st.sidebar.header('Filters')
positions = st.sidebar.multiselect(
    'Position', df['position'].unique(),
    default=df['position'].unique()
)
playstyles = st.sidebar.multiselect(
    'Playstyle', df['playstyle'].unique(),
    default=df['playstyle'].unique()
)


filtered = df[
    df['position'].isin(positions) &
    df['playstyle'].isin(playstyles)
].copy() # Using .copy() prevents warnings when we clean the data below


filtered = filtered.dropna(subset=['market_value_in_eur'])


if not filtered.empty:
    fig = px.scatter(
        filtered,
        x='goals_per90', y='assists_per90',
        color='playstyle', color_discrete_map=COLORS,
        size='market_value_in_eur', size_max=25,
        hover_name='name',
        title='Goals vs Assists per 90 mins',
        opacity=0.7,
        template='plotly_dark' # Optional: looks great with sports dashboards
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No players found with the selected filters. Try widening your search!")
    
player = st.selectbox('Select a player for radar chart',
                      sorted(df['name'].tolist()))
if player:
    row = df[df['name']==player].iloc[0]
    cats = ['goals_per90','assists_per90','gc_per90',
            'yellow_per90','minutes_ratio']
    labels = ['Goals/90','Assists/90','GC/90','Cards/90','Minutes']
    vals = [min(float(row[c])/max(df[c].quantile(0.95),0.001),1)
            for c in cats]
    vals += [vals[0]]
    radar = go.Figure(go.Scatterpolar(
        r=vals, theta=labels+[labels[0]],
        fill='toself',
        line_color=COLORS.get(row['playstyle'],'#534AB7'),
        fillcolor=COLORS.get(row['playstyle'],'#534AB7'),
        opacity=0.4, name=player
    ))
    radar.update_layout(
        polar=dict(radialaxis=dict(visible=True,range=[0,1])),
        title=f'{player} — {row["playstyle"]}',
        height=400
    )
    st.plotly_chart(radar, use_container_width=True)
