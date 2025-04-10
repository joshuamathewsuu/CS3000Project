import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from numba import jit, prange
import time
from scipy.stats import norm

st.set_page_config(page_title="Advanced Startup Valuation Monte Carlo", layout="wide")

# Industry-specific parameters
INDUSTRY_PARAMS = {
    'Technology': {'growth_range': (0.15, 0.40), 'volatility_range': (0.25, 0.50)},
    'Healthcare': {'growth_range': (0.10, 0.30), 'volatility_range': (0.20, 0.40)},
    'Finance': {'growth_range': (0.12, 0.35), 'volatility_range': (0.22, 0.45)},
    'Retail': {'growth_range': (0.08, 0.25), 'volatility_range': (0.15, 0.35)},
    'Manufacturing': {'growth_range': (0.05, 0.20), 'volatility_range': (0.10, 0.30)}
}

@jit(nopython=True, parallel=True)
def monte_carlo_simulation(initial_value, growth_rate, volatility, time_horizon, num_simulations):
    results = np.zeros((num_simulations, time_horizon))
    
    for i in prange(num_simulations):
        current_value = initial_value
        for t in range(time_horizon):
            # Geometric Brownian Motion with industry-specific adjustments
            drift = growth_rate * current_value
            shock = volatility * current_value * np.random.normal(0, 1)
            current_value = current_value + drift + shock
            results[i, t] = current_value
    
    return results

def calculate_valuation_metrics(results):
    final_values = results[:, -1]
    mean_value = np.mean(final_values)
    median_value = np.median(final_values)
    std_dev = np.std(final_values)
    p95 = np.percentile(final_values, 95)
    p5 = np.percentile(final_values, 5)
    
    return {
        'mean': mean_value,
        'median': median_value,
        'std_dev': std_dev,
        'p95': p95,
        'p5': p5
    }

def plot_valuation_distribution(final_values):
    fig = go.Figure()
    
    # Add histogram
    fig.add_trace(go.Histogram(
        x=final_values,
        nbinsx=50,
        name='Final Values',
        histnorm='probability'
    ))
    
    # Add normal distribution curve
    x = np.linspace(min(final_values), max(final_values), 100)
    mu, sigma = np.mean(final_values), np.std(final_values)
    y = norm.pdf(x, mu, sigma)
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='lines',
        name='Normal Distribution',
        line=dict(color='red', width=2)
    ))
    
    fig.update_layout(
        title="Distribution of Final Valuations",
        xaxis_title="Final Valuation ($)",
        yaxis_title="Probability Density",
        showlegend=True
    )
    
    return fig

def main():
    st.title("Advanced Startup Valuation Monte Carlo Simulation")
    
    # Sidebar inputs
    st.sidebar.header("Simulation Parameters")
    
    # Industry selection
    industry = st.sidebar.selectbox(
        "Industry",
        list(INDUSTRY_PARAMS.keys()),
        index=0
    )
    
    # Get industry-specific ranges
    growth_range = INDUSTRY_PARAMS[industry]['growth_range']
    volatility_range = INDUSTRY_PARAMS[industry]['volatility_range']
    
    initial_value = st.sidebar.number_input(
        "Initial Valuation ($)",
        min_value=100000,
        value=1000000,
        step=100000
    )
    
    growth_rate = st.sidebar.slider(
        "Expected Growth Rate (%)",
        min_value=float(growth_range[0] * 100),
        max_value=float(growth_range[1] * 100),
        value=float(np.mean(growth_range) * 100),
        step=0.1
    ) / 100
    
    volatility = st.sidebar.slider(
        "Volatility (%)",
        min_value=float(volatility_range[0] * 100),
        max_value=float(volatility_range[1] * 100),
        value=float(np.mean(volatility_range) * 100),
        step=0.1
    ) / 100
    
    time_horizon = st.sidebar.slider(
        "Time Horizon (years)",
        min_value=1,
        max_value=10,
        value=5
    )
    
    num_simulations = st.sidebar.slider(
        "Number of Simulations",
        min_value=100,
        max_value=10000,
        value=1000,
        step=100
    )
    
    if st.sidebar.button("Run Simulation"):
        with st.spinner("Running Monte Carlo Simulation..."):
            start_time = time.time()
            results = monte_carlo_simulation(
                initial_value,
                growth_rate,
                volatility,
                time_horizon,
                num_simulations
            )
            end_time = time.time()
            
            st.success(f"Simulation completed in {end_time - start_time:.2f} seconds")
            
            # Calculate metrics
            metrics = calculate_valuation_metrics(results)
            
            # Display statistics
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.metric("Mean Valuation", f"${metrics['mean']:,.2f}")
            with col2:
                st.metric("Median Valuation", f"${metrics['median']:,.2f}")
            with col3:
                st.metric("Standard Deviation", f"${metrics['std_dev']:,.2f}")
            with col4:
                st.metric("95th Percentile", f"${metrics['p95']:,.2f}")
            with col5:
                st.metric("5th Percentile", f"${metrics['p5']:,.2f}")
            
            # Plot results
            fig = go.Figure()
            
            # Plot individual paths
            for i in range(min(100, num_simulations)):
                fig.add_trace(go.Scatter(
                    y=results[i],
                    mode='lines',
                    line=dict(width=1),
                    showlegend=False
                ))
            
            # Plot mean path
            mean_path = np.mean(results, axis=0)
            fig.add_trace(go.Scatter(
                y=mean_path,
                mode='lines',
                line=dict(width=3, color='red'),
                name='Mean Path'
            ))
            
            fig.update_layout(
                title="Monte Carlo Simulation Results",
                xaxis_title="Time (years)",
                yaxis_title="Valuation ($)",
                showlegend=True
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Display distribution analysis
            st.subheader("Distribution Analysis")
            dist_fig = plot_valuation_distribution(results[:, -1])
            st.plotly_chart(dist_fig, use_container_width=True)
            
            # Display industry insights
            st.subheader("Industry Insights")
            st.write(f"""
            **{industry} Industry Analysis:**
            - Typical growth rate range: {growth_range[0]*100:.1f}% to {growth_range[1]*100:.1f}%
            - Typical volatility range: {volatility_range[0]*100:.1f}% to {volatility_range[1]*100:.1f}%
            - Current simulation parameters are within industry norms
            """)

if __name__ == "__main__":
    main() 